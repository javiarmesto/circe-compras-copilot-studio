#!/usr/bin/env python3
"""Build portable Copilot Studio skill ZIPs. Does not deploy an agent."""
from pathlib import Path
import hashlib,io,json,zipfile,shutil
ROOT=Path(__file__).resolve().parents[1]
skill=ROOT/'demo/skills/circe-reposicion'
out=ROOT/'demo/packages';out.mkdir(exist_ok=True)

def validate(folder):
    """Faults that let a skill upload but never activate: BOM, bad front matter, name, description."""
    import re
    errors=[]
    for f in folder.rglob('*'):
        if f.is_file() and '__pycache__' not in f.parts and f.read_bytes()[:3]==b'\xef\xbb\xbf':
            errors.append(f'BOM en {f.relative_to(folder).as_posix()}')
    text=(folder/'SKILL.md').read_text(encoding='utf-8-sig')
    m=re.match(r'---\r?\n(.*?)\r?\n---',text,re.S)
    if not m: errors.append('SKILL.md sin front matter YAML al inicio')
    else:
        name=re.search(r'^name:\s*(.+)$',m.group(1),re.M); desc=re.search(r'^description:\s*(.+)$',m.group(1),re.M)
        if not name: errors.append('front matter sin name')
        else:
            n=name.group(1).strip()
            if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',n): errors.append(f"name '{n}': solo minúsculas, números y guiones")
            if n!=folder.name: errors.append(f"name '{n}' no coincide con la carpeta '{folder.name}'")
        if not desc or len(desc.group(1).strip())<40: errors.append('description ausente o demasiado corta: la selección depende de ella')
    if b'\r' in (folder/'SKILL.md').read_bytes(): print('Aviso: SKILL.md tiene finales de línea CRLF; revisa .gitattributes')
    if errors: raise SystemExit('Skill no válida:\n- '+'\n- '.join(errors))
    print('Skill válida:',folder.name)

def members(zip_bytes):
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z: return [(n,z.read(n)) for n in z.namelist()]

validate(skill)
for version in (1,2):
    archive=out/f'circe-reposicion-v{version}.zip'
    buf=io.BytesIO()
    with zipfile.ZipFile(buf,'w',compression=zipfile.ZIP_DEFLATED) as z:
        # Case-insensitive order and create_system=0 give the same entries on Windows and Linux.
        for path in sorted(skill.rglob('*'),key=lambda p:p.relative_to(skill).as_posix().lower()):
            if not path.is_file() or '__pycache__' in path.parts: continue
            rel=path.relative_to(skill).as_posix()
            data=path.read_bytes()
            if version==2 and rel=='references/policy.json': data=(ROOT/'demo/data/politica-demo-v2.json').read_bytes()
            if version==2 and rel=='references/policy.md':
                data=data.decode().replace('versión 1.0','versión 2.0').replace('500 EUR','1000 EUR').encode()
            info=zipfile.ZipInfo(rel,date_time=(2026,9,9,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.create_system=0
            z.writestr(info,data)
    new=buf.getvalue()
    names=[n for n,_ in members(new)]
    assert 'SKILL.md' in names
    assert all(not n.startswith('/') and '..' not in Path(n).parts for n in names)
    # Compressed bytes depend on the zlib build, so only rewrite when the content changes.
    unchanged=archive.exists() and members(archive.read_bytes())==members(new)
    if not unchanged: archive.write_bytes(new)
    print(archive.name,hashlib.sha256(archive.read_bytes()).hexdigest(),'(sin cambios)' if unchanged else '(actualizado)')
# A knowledge version that agrees with skill v2.
p=(ROOT/'demo/data/politica-compras.md').read_text(encoding='utf-8')
v2=ROOT/'demo/data/politica-compras-v2.md';text=p.replace('versión 1.0','versión 2.0').replace('500 EUR','1000 EUR')
# LF on every OS (write_text would use CRLF on Windows and dirty the tree) and no rewrite when nothing changed.
if not v2.exists() or v2.read_bytes()!=text.encode('utf-8'): v2.write_text(text,encoding='utf-8',newline='\n')
