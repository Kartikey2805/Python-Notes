from pathlib import Path

cwd = Path('C:/Users/Karti')

def find(path, name):
    try:
        for dir in path.iterdir():
            if name == dir.name:
                return dir
            if dir.is_dir():
                p = find(dir, name)
                if p is not None:
                    return p
    except PermissionError:
        pass  # Ignore PermissionError and continue traversal

    return None

name = 'pip.ini'
path = find(cwd, name)

print(path)
