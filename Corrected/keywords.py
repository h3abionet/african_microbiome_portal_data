from glob import glob
import pandas as pd
from Bio import SeqIO


class Test:
    pass


class Test2:

    def abc():
        return

    pass


for fl in glob("*.csv"):
    df = pd.read_csv(fl)
    print(list(set(df["STUDY TITLE"]))[0])

a = [12, 23]
b = [10, 25]
