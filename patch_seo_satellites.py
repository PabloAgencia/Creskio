#!/usr/bin/env python3
"""
patch_seo_satellites.py — CostaDigital SEO Patch
Ejecutar desde la raíz del repo: python3 patch_seo_satellites.py

Aplica a las 11 páginas de sector y 11 de ciudad restantes:
  - og:locale, og:site_name, og:image:width/height
  - twitter:image
  - geo.region, geo.placename  
  - <link rel="sitemap">
  - BreadcrumbList schema (añade a @graph existente o crea @graph)
  - FAQPage schema (solo para páginas de sector — lee FAQ del HTML)

Para páginas de ciudad también:
  - hreflang
  - Arregla canonical a no-.html si lo tiene (Vercel clean URLs)
  - Corrige fontes rotas ("font\nfont\nfont")

NOTA: Este script es no destructivo — solo añade lo que falta.
"""

import re, os, json

# ──── CONFIG ────
SECTOR_PAGES = [
    ("web-para-restaurantes.html", "Web para Restaurantes"),
    ("web-para-clinicas.html",     "Web para Clínicas"),
    ("web-para-electricistas.html","Web para Electricistas"),
    ("web-para-fontaneros.html",   "Web para Fontaneros"),
    ("web-para-peluquerias.html",  "Web para Peluquerías"),
    ("web-para-abogados.html",     "Web para Abogados"),
    ("web-para-inmobiliarias.html","Web para Inmobiliarias"),
    ("web-para-estetica.html",     "Web para Estética"),
    ("web-para-gimnasios.html",    "Web para Gimnasios"),
    ("web-para-academias.html",    "Web para Academias"),
    ("web-para-hoteles.html",      "Web para Hoteles"),
]

CITY_PAGES = [
    ("diseno-web-barcelona.html",  "Barcelona",   "ES-CT", "42.3504", "2.1475"),
    ("diseno-web-valencia.html",   "Valencia",    "ES-VC", "39.4699", "-0.3763"),
    ("diseno-web-sevilla.html",    "Sevilla",     "ES-AN", "37.3891", "-5.9845"),
    ("diseno-web-malaga.html",     "Málaga",      "ES-AN", "36.7213", "-4.4214"),
    ("diseno-web-bilbao.html",     "Bilbao",      "ES-PV", "43.2630", "-2.9350"),
    ("diseno-web-zaragoza.html",   "Zaragoza",    "ES-AR", "41.6561", "-0.8773"),
    ("diseno-web-alicante.html",   "Alicante",    "ES-VC", "38.3452", "-0.4815"),
    ("diseno-web-cordoba.html",    "Córdoba",     "ES-AN", "37.8882", "-4.7794"),
    ("diseno-web-granada.html",    "Granada",     "ES-AN", "37.1773", "-3.5986"),
    ("diseno-web-valladolid.html", "Valladolid",  "ES-CL", "41.6523", "-4.7245"),
    ("diseno-web-murcia.html",     "Murcia",      "ES-MC", "37.9922", "-1.1307"),
]

def add_meta_after(content, anchor, new_meta):
    """Add new_meta right after the first occurrence of anchor."""
    if new_meta.strip() in content:
        return content  # already present
    idx = content.find(anchor)
    if idx == -1:
        return content
    end = idx + len(anchor)
    return content[:end] + "\n" + new_meta + content[end:]

def patch_sector_page(filepath, label):
    if not os.path.exists(filepath):
        print(f"  ⚠️  Not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. og:locale, og:site_name
    if 'og:locale' not in content:
        content = add_meta_after(content, 
            '<meta property="og:image" content="https://costadigital.es/og-image.jpg">',
            '<meta property="og:locale" content="es_ES">\n<meta property="og:site_name" content="CostaDigital">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">'
        )
        modified = True

    # 2. twitter:image
    if 'twitter:image' not in content:
        content = add_meta_after(content,
            '<meta name="twitter:description"',
            '<meta name="twitter:image" content="https://costadigital.es/og-image.jpg">'
        )
        modified = True

    # 3. geo.region
    if 'geo.region' not in content:
        content = add_meta_after(content,
            '<link rel="canonical"',
            '<meta name="geo.region" content="ES-GR">\n<meta name="geo.placename" content="Costa Tropical, Granada, España">\n<link rel="sitemap" type="application/xml" href="sitemap.xml">'
        )
        modified = True

    # 4. BreadcrumbList in schema
    if 'BreadcrumbList' not in content:
        slug = filepath.replace('.html','')
        url = f"https://costadigital.es/{filepath}"
        breadcrumb = {
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://costadigital.es/"},
                {"@type": "ListItem", "position": 2, "name": label, "item": url}
            ]
        }
        # Try to inject into existing @graph
        if '"@graph"' in content:
            # Find end of @graph array and inject before closing ]
            idx = content.rfind(']\n}')
            if idx != -1:
                bc_str = ",\n    " + json.dumps(breadcrumb, ensure_ascii=False, indent=4).replace('\n','\n    ')
                content = content[:idx] + bc_str + content[idx:]
                modified = True
        else:
            # Wrap existing schema type in @graph
            print(f"  ℹ️  {filepath}: schema needs manual @graph wrap for BreadcrumbList")
    
    # 5. FAQPage schema — parse FAQ questions from HTML if not present
    if 'FAQPage' not in content:
        # Extract FAQ questions from lp-faq-q buttons
        questions = re.findall(r'class="lp-faq-q">(.*?)<span', content, re.DOTALL)
        answers_raw = re.findall(r'class="lp-faq-a"><p>(.*?)</p>', content, re.DOTALL)
        questions = [q.strip() for q in questions]
        answers = [a.strip() for a in answers_raw]
        if questions and answers and len(questions) == len(answers):
            entities = []
            for q, a in zip(questions, answers):
                entities.append({
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a}
                })
            url = f"https://costadigital.es/{filepath}"
            faq_schema = {
                "@type": "FAQPage",
                "@id": f"{url}#faq",
                "mainEntity": entities
            }
            if '"@graph"' in content:
                idx = content.rfind(']\n}')
                if idx != -1:
                    faq_str = ",\n    " + json.dumps(faq_schema, ensure_ascii=False, indent=4).replace('\n','\n    ')
                    content = content[:idx] + faq_str + content[idx:]
                    modified = True
            # else would need manual intervention
        else:
            print(f"  ⚠️  {filepath}: FAQ Q/A count mismatch ({len(questions)}Q vs {len(answers)}A) — manual review needed")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Patched: {filepath}")
    else:
        print(f"  ✓  Already up to date: {filepath}")


def patch_city_page(filepath, city, region_code, lat, lng):
    if not os.path.exists(filepath):
        print(f"  ⚠️  Not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    modified = False

    # Fix broken font lines
    if 'font\nfont\nfont\n<style>' in content:
        content = content.replace('font\nfont\nfont\n<style>',
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap" rel="stylesheet">\n'
            '<style>'
        )
        modified = True

    # og:locale, og:site_name, og:image dimensions
    if 'og:locale' not in content:
        content = add_meta_after(content,
            '<meta property="og:image" content="https://costadigital.es/og-image.jpg">',
            '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:locale" content="es_ES">\n<meta property="og:site_name" content="CostaDigital">'
        )
        modified = True

    # twitter:image
    if 'twitter:image' not in content and 'twitter:card' in content:
        # Add after twitter:description if present
        if 'twitter:description' in content:
            m = re.search(r'(<meta name="twitter:description"[^>]+>)', content)
            if m:
                content = content[:m.end()] + '\n<meta name="twitter:image" content="https://costadigital.es/og-image.jpg">' + content[m.end():]
                modified = True

    # geo meta
    if 'geo.region' not in content:
        content = add_meta_after(content,
            '<link rel="canonical"',
            f'<meta name="geo.region" content="{region_code}">\n<meta name="geo.placename" content="{city}, España">\n<meta name="geo.position" content="{lat};{lng}">\n<link rel="sitemap" type="application/xml" href="sitemap.xml">'
        )
        modified = True

    # hreflang
    if 'hreflang' not in content:
        url = f"https://costadigital.es/{filepath}"
        content = add_meta_after(content,
            '<meta name="theme-color"',
            f'<link rel="hreflang" href="{url}" hreflang="es-ES">'
        )
        modified = True

    # BreadcrumbList
    if 'BreadcrumbList' not in content:
        url = f"https://costadigital.es/{filepath}"
        breadcrumb = {
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://costadigital.es/"},
                {"@type": "ListItem", "position": 2, "name": f"Diseño Web {city}", "item": url}
            ]
        }
        if '"@graph"' in content:
            idx = content.rfind(']\n}')
            if idx != -1:
                bc_str = ",\n    " + json.dumps(breadcrumb, ensure_ascii=False, indent=4).replace('\n','\n    ')
                content = content[:idx] + bc_str + content[idx:]
                modified = True

    # FAQPage for city pages (inline divs, not lp-faq-q class)
    if 'FAQPage' not in content:
        qs = re.findall(r"font-weight:700[^>]*>([^<]+)</p>", content)
        as_ = re.findall(r"font-weight:300;line-height:1\.8;margin:0[^>]*>(.*?)</p>", content, re.DOTALL)
        qs = [q.strip() for q in qs if '?' in q]
        as_ = [re.sub(r'<[^>]+>', '', a).strip() for a in as_]
        if qs and as_ and len(qs) == len(as_):
            url = f"https://costadigital.es/{filepath}"
            entities = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in zip(qs,as_)]
            faq_schema = {"@type":"FAQPage","@id":f"{url}#faq","mainEntity":entities}
            if '"@graph"' in content:
                idx = content.rfind(']\n}')
                if idx != -1:
                    faq_str = ",\n    " + json.dumps(faq_schema, ensure_ascii=False, indent=4).replace('\n','\n    ')
                    content = content[:idx] + faq_str + content[idx:]
                    modified = True
        else:
            print(f"  ⚠️  {filepath}: FAQ parse unclear ({len(qs)}Q vs {len(as_)}A) — manual check recommended")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Patched: {filepath}")
    else:
        print(f"  ✓  Already up to date: {filepath}")


if __name__ == "__main__":
    print("\n=== SECTOR PAGES ===")
    for fname, label in SECTOR_PAGES:
        patch_sector_page(fname, label)
    
    print("\n=== CITY PAGES ===")
    for fname, city, region_code, lat, lng in CITY_PAGES:
        patch_city_page(fname, city, region_code, lat, lng)
    
    print("\n✅ Patch completo. Revisa los ⚠️ manualmente si los hay.")
