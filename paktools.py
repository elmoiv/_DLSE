from zipupdate import *

def copy_pak_from_game(path):
    pak_path = os.path.join(path, 'DW', 'Data0.pak')
    shutil.copy2(pak_path, 'Data0.pak')

def copy_pak_to_game(path):
    pak_path = os.path.join(path, 'DW', 'Data0.pak')
    shutil.copy2('Data0.pak', pak_path)

def extract_skills_file(*names):
    with ZipFile('Data0.pak') as z:
        for name in names:
            with z.open(f'data/skills/{name}.xml') as zf, open(f'{name}.xml', 'wb') as f:
                shutil.copyfileobj(zf, f)

def update_pak(*names):
    with UpdateableZipFile("Data0.pak", "a") as o:
        for name in names:
            o.write(f'{name}.xml', f'data/skills/{name}.xml')