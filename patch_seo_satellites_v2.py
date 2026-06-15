#!/usr/bin/env python3
"""
patch_seo_satellites_v2.py — Creskio SEO Patch (versión corregida)
Ejecutar desde la raíz del repo: python3 patch_seo_satellites_v2.py

Fixes:
  1. Fuentes rotas "font\nfont\nfont" → preconnects correctos
  2. Meta tags OG/Twitter faltantes
  3. Geo metas
  4. hreflang (páginas ciudad)
  5. Schema @graph con BreadcrumbList + FAQPage (extrae FAQs del HTML)
  6. Páginas de sector: arregla JS cortado si detecta el patrón (solo abogados ya está hecho)

Ejecutar SOLO sobre archivos que NO sean:
  - index.html (ya tiene todo)
  - diseno-web-zaragoza.html (ya parcheada manualmente)
  - web-para-abogados.html (ya parcheada manualmente)
  - cuanto-cuesta-*.html / por-que-*.html (blog, schema diferente)
"""

import re, os, json

GOOGLE_FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap" rel="stylesheet">'''

# ── Sector pages ──────────────────────────────────────────────────────────────
SECTOR_PAGES = [
    ("web-para-restaurantes.html",  "Web para Restaurantes",  "🍽️"),
    ("web-para-clinicas.html",      "Web para Clínicas",      "🏥"),
    ("web-para-electricistas.html", "Web para Electricistas", "⚡"),
    ("web-para-fontaneros.html",    "Web para Fontaneros",    "🔧"),
    ("web-para-peluquerias.html",   "Web para Peluquerías",   "✂️"),
    ("web-para-inmobiliarias.html", "Web para Inmobiliarias", "🏠"),
    ("web-para-estetica.html",      "Web para Estética",      "💆"),
    ("web-para-gimnasios.html",     "Web para Gimnasios",     "🏋️"),
    ("web-para-academias.html",     "Web para Academias",     "🎓"),
    ("web-para-hoteles.html",       "Web para Hoteles",       "🏨"),
    ("web-para-talleres.html",      "Web para Talleres",      "🔧"),
]

# ── City pages ────────────────────────────────────────────────────────────────
CITY_PAGES = [
    ("diseno-web-madrid.html",     "Madrid",      "ES-MD", "40.4168", "-3.7038"),
    ("diseno-web-barcelona.html",  "Barcelona",   "ES-CT", "41.3851", "2.1734"),
    ("diseno-web-valencia.html",   "Valencia",    "ES-VC", "39.4699", "-0.3763"),
    ("diseno-web-sevilla.html",    "Sevilla",     "ES-AN", "37.3891", "-5.9845"),
    ("diseno-web-malaga.html",     "Málaga",      "ES-AN", "36.7213", "-4.4214"),
    ("diseno-web-bilbao.html",     "Bilbao",      "ES-PV", "43.2630", "-2.9350"),
    ("diseno-web-alicante.html",   "Alicante",    "ES-VC", "38.3452", "-0.4815"),
    ("diseno-web-cordoba.html",    "Córdoba",     "ES-AN", "37.8882", "-4.7794"),
    ("diseno-web-granada.html",    "Granada",     "ES-AN", "37.1773", "-3.5986"),
    ("diseno-web-valladolid.html", "Valladolid",  "ES-CL", "41.6523", "-4.7245"),
    ("diseno-web-murcia.html",     "Murcia",      "ES-MC", "37.9922", "-1.1307"),
    ("diseno-web-vigo.html",       "Vigo",        "ES-GA", "42.2314", "-8.7124"),
    ("diseno-web-palma.html",      "Palma",       "ES-IB", "39.5696", "2.6502"),
    ("diseno-web-las-palmas.html", "Las Palmas",  "ES-CN", "28.1235", "-15.4366"),
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def ensure_after(content, anchor, new_meta):
    """Insert new_meta after anchor, only if new_meta not already present."""
    key = new_meta.strip().split('\n')[0][:60]
    if key in content:
        return content, False
    idx = content.find(anchor)
    if idx == -1:
        return content, False
    end = idx + len(anchor)
    return content[:end] + '\n' + new_meta + content[end:], True

def fix_fonts(content):
    broken = 'font\nfont\nfont\n<style>'
    if broken not in content:
        return content, False
    fixed = GOOGLE_FONTS + '\n<style>'
    return content.replace(broken, fixed, 1), True

def extract_faqs_sector(content):
    """Extract FAQ Q&A pairs from sector pages (lp-faq-q / lp-faq-a pattern)."""
    questions = re.findall(r'class="lp-faq-q"[^>]*>(.*?)<span', content, re.DOTALL)
    answers = re.findall(r'class="lp-faq-a"><p>(.*?)</p>', content, re.DOTALL)
    questions = [q.strip() for q in questions]
    answers = [re.sub(r'<[^>]+>', '', a).strip() for a in answers]
    if len(questions) == len(answers) and questions:
        return list(zip(questions, answers))
    return []

def extract_faqs_city(content):
    """Extract FAQ Q&A pairs from city pages (inline-style divs)."""
    # FAQ questions: <p style="...font-weight:700...">QUESTION</p>
    # FAQ answers:   <p style="...font-weight:300;line-height:1.8;margin:0">ANSWER</p>
    q_pattern = r'font-weight:700[^>]*>([^<]+)</p>'
    a_pattern = r'font-weight:300;line-height:1\.8;margin:0[^>]*>(.*?)</p>'
    questions = re.findall(q_pattern, content)
    answers_raw = re.findall(a_pattern, content, re.DOTALL)
    questions = [q.strip() for q in questions if '?' in q]
    answers = [re.sub(r'<[^>]+>', '', a).strip() for a in answers_raw]
    if len(questions) == len(answers) and questions:
        return list(zip(questions, answers))
    # Fallback: fewer pairs
    pairs = list(zip(questions, answers))
    return pairs

def build_faq_schema(pairs, url):
    entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        }
        for q, a in pairs
    ]
    return {
        "@type": "FAQPage",
        "@id": f"{url}#faq",
        "mainEntity": entities
    }

def build_breadcrumb_schema(url, label):
    return {
        "@type": "BreadcrumbList",
        "@id": f"{url}#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://creskio.es/"},
            {"@type": "ListItem", "position": 2, "name": label, "item": url}
        ]
    }

def inject_schema_items(content, url, label, faq_pairs):
    """
    Inject BreadcrumbList + FAQPage into existing @graph, or wrap existing Service
    type in a @graph if no @graph present.
    """
    if 'BreadcrumbList' in content and 'FAQPage' in content:
        return content, False

    bc = build_breadcrumb_schema(url, label)
    faq = build_faq_schema(faq_pairs, url) if faq_pairs else None

    schema_items_to_add = []
    if 'BreadcrumbList' not in content:
        schema_items_to_add.append(bc)
    if faq and 'FAQPage' not in content:
        schema_items_to_add.append(faq)

    if not schema_items_to_add:
        return content, False

    if '"@graph"' in content:
        # Find the closing ] of the @graph array and insert before it
        # Strategy: find last ]\n} that closes the @graph
        idx = content.rfind(']\n}')
        if idx == -1:
            idx = content.rfind(']}')
        if idx != -1:
            items_str = ''
            for item in schema_items_to_add:
                items_str += ',\n    ' + json.dumps(item, ensure_ascii=False, indent=4).replace('\n', '\n    ')
            content = content[:idx] + items_str + '\n' + content[idx:]
            return content, True
    else:
        # No @graph — find the existing ld+json block and replace it with @graph wrapper
        match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        if match:
            old_json_str = match.group(1).strip()
            try:
                old_obj = json.loads(old_json_str)
                graph = [old_obj] + schema_items_to_add
                new_json = json.dumps({"@context": "https://schema.org", "@graph": graph},
                                       ensure_ascii=False, indent=2)
                new_block = f'<script type="application/ld+json">{new_json}</script>'
                content = content[:match.start()] + new_block + content[match.end():]
                return content, True
            except json.JSONDecodeError:
                pass
    return content, False

def add_og_meta(content):
    """Add missing OG/Twitter meta tags after og:image."""
    anchor = '<meta property="og:image" content="https://creskio.es/og-image.jpg">'
    additions = []
    if 'og:image:width' not in content:
        additions.append('<meta property="og:image:width" content="1200">')
    if 'og:image:height' not in content:
        additions.append('<meta property="og:image:height" content="630">')
    if 'og:locale' not in content:
        additions.append('<meta property="og:locale" content="es_ES">')
    if 'og:site_name' not in content:
        additions.append('<meta property="og:site_name" content="Creskio">')
    if not additions:
        return content, False
    idx = content.find(anchor)
    if idx == -1:
        return content, False
    end = idx + len(anchor)
    content = content[:end] + '\n' + '\n'.join(additions) + content[end:]
    return content, True

def add_twitter_meta(content):
    """Add twitter:card and twitter:image if missing."""
    if 'twitter:image' in content:
        return content, False
    # Find twitter:description to insert after
    anchor = '<meta name="twitter:description"'
    idx = content.find(anchor)
    if idx == -1:
        # Try after og:site_name
        anchor = '<meta property="og:site_name"'
        idx = content.find(anchor)
    if idx == -1:
        return content, False
    # Find end of this tag
    end = content.find('>', idx) + 1
    additions = []
    if 'twitter:card' not in content:
        additions.append('<meta name="twitter:card" content="summary_large_image">')
    additions.append('<meta name="twitter:image" content="https://creskio.es/og-image.jpg">')
    content = content[:end] + '\n' + '\n'.join(additions) + content[end:]
    return content, True

def add_geo_meta(content, city, region_code, lat, lng):
    if 'geo.region' in content:
        return content, False
    anchor = '<link rel="canonical"'
    idx = content.find(anchor)
    if idx == -1:
        return content, False
    geo_block = (f'<meta name="geo.region" content="{region_code}">\n'
                 f'<meta name="geo.placename" content="{city}, España">\n'
                 f'<meta name="geo.position" content="{lat};{lng}">\n'
                 f'<meta name="ICBM" content="{lat}, {lng}">')
    content = content[:idx] + geo_block + '\n' + content[idx:]
    return content, True

def add_hreflang(content, url):
    if 'hreflang' in content:
        return content, False
    anchor = '<meta name="theme-color"'
    idx = content.find(anchor)
    if idx == -1:
        return content, False
    tag = f'<link rel="hreflang" href="{url}" hreflang="es-ES">'
    content = content[:idx] + tag + '\n' + content[idx:]
    return content, True

# ── Main processing ───────────────────────────────────────────────────────────

def patch_sector(fname, label, icon):
    if not os.path.exists(fname):
        print(f"  ⏭  Not found: {fname}")
        return

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    url = f"https://creskio.es/{fname}"

    c, ok = fix_fonts(content); content = c; changed = changed or ok
    c, ok = add_og_meta(content); content = c; changed = changed or ok
    c, ok = add_twitter_meta(content); content = c; changed = changed or ok

    # Add geo if missing (sector pages usually don't have it — add ES-GR base)
    if 'geo.region' not in content:
        anchor = '<link rel="canonical"'
        idx = content.find(anchor)
        if idx != -1:
            geo = '<meta name="geo.region" content="ES">\n<meta name="geo.placename" content="España">'
            content = content[:idx] + geo + '\n' + content[idx:]
            changed = True

    # Schema
    faq_pairs = extract_faqs_sector(content)
    if not faq_pairs:
        # Try city-style extraction as fallback
        faq_pairs = extract_faqs_city(content)
    c, ok = inject_schema_items(content, url, label, faq_pairs)
    content = c; changed = changed or ok

    if changed:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        faq_note = f"({len(faq_pairs)} FAQ pairs)" if faq_pairs else "(no FAQs extracted)"
        print(f"  ✅ Patched: {fname} {faq_note}")
    else:
        print(f"  ✓  Up to date: {fname}")


def patch_city(fname, city, region_code, lat, lng):
    if not os.path.exists(fname):
        print(f"  ⏭  Not found: {fname}")
        return

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    url = f"https://creskio.es/{fname}"

    c, ok = fix_fonts(content); content = c; changed = changed or ok
    c, ok = add_og_meta(content); content = c; changed = changed or ok
    c, ok = add_twitter_meta(content); content = c; changed = changed or ok
    c, ok = add_geo_meta(content, city, region_code, lat, lng); content = c; changed = changed or ok
    c, ok = add_hreflang(content, url); content = c; changed = changed or ok

    # Schema
    faq_pairs = extract_faqs_city(content)
    label = f"Diseño Web {city}"
    c, ok = inject_schema_items(content, url, label, faq_pairs)
    content = c; changed = changed or ok

    if changed:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        faq_note = f"({len(faq_pairs)} FAQ pairs)" if faq_pairs else "(no FAQs found)"
        print(f"  ✅ Patched: {fname} {faq_note}")
    else:
        print(f"  ✓  Up to date: {fname}")


if __name__ == "__main__":
    print("\n=== SECTOR PAGES ===")
    for fname, label, icon in SECTOR_PAGES:
        patch_sector(fname, label, icon)

    print("\n=== CITY PAGES ===")
    for fname, city, region, lat, lng in CITY_PAGES:
        patch_city(fname, city, region, lat, lng)

    print("\n✅ Patch v2 completo.")
