from pathlib import Path


class Site(self, source, dest):


    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)


    def create_dir(self, path):
        directory = self.dest + "/" + Path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        paths = self.source.rglob("*")
        for path in paths:
            if path.is_dir():
                self.create_dir(path)
