"""Actualiza el lastmod de sitemap.xml con la fecha real del último commit de cada archivo.
Ejecutar antes de cada deploy: python update-sitemap-lastmod.py
"""
import re
import subprocess
import os

base = os.path.dirname(os.path.abspath(__file__))
sitemap_path = os.path.join(base, "sitemap.xml")

with open(sitemap_path, "r", encoding="utf-8") as f:
    content = f.read()

def last_commit_date(filename):
    result = subprocess.run(
        ["git", "log", "-1", "--format=%ad", "--date=short", "--", filename],
        cwd=base, capture_output=True, text=True
    )
    date = result.stdout.strip()
    return date or None

def replace_lastmod(match):
    loc = match.group("loc")
    filename = "index.html" if loc.rstrip("/").endswith("creskio.com") else loc.split("/")[-1]
    date = last_commit_date(filename)
    if not date:
        return match.group(0)
    return f'<url><loc>{loc}</loc><lastmod>{date}</lastmod>{match.group("rest")}</url>'

pattern = re.compile(r'<url><loc>(?P<loc>[^<]+)</loc><lastmod>[^<]+</lastmod>(?P<rest><changefreq>[^<]+</changefreq><priority>[^<]+</priority>)</url>')
new_content, count = pattern.subn(replace_lastmod, content)

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Actualizadas {count} URLs en sitemap.xml")
