from glob import glob
import pandas as pd
from os import path


with open("NoteBookTemplates/template.ipynb") as fin:
    template = fin.read()

for fl in glob("../Originals/Fragmented/*.csv"):
    flb = path.split(fl)[-1].split(".")[0]
    with open(f"../Notebooks/{flb}.ipynb", "w") as fout:
        fout.write(template % (flb, flb))
