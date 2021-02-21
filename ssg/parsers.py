from typing import List
from pathlib import Path
import shutil


class Parser:
    def __init__(self, extensions):
        self.extensions = extensions


    def valid_extension(self, extension):
        return self.extension in self.extensions


    def parse(self, path, source, dest):
        raise NotImplementedError


    def read(self, path):
        with open(self.path, 'rt', 'utf-8') as file:
            return file.read() 


    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / self.path.with_suffix(ext).name
        with open(full_path, 'rt', 'utf-8') as file:
            file.write(self.content)


    def copy(self, path, source, dest):
        shutil.copy2(self.path, dest / path.relative_to(self.source))


class ResourceParser(Parser):

    def __init__(self):
        super().__init__(List[".jpg", ".png", ".gif", ".css", ".html"])

    
    def parse(self, path, source, dest):
        self.copy(path, source, dest)