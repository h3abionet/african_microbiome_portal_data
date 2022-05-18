#!/usr/bin/env python

import pandas as pd
from glob import glob
from os import path

already_known = pd.read_csv("../fixed/project_summary.csv")

new_known = []
for fl in glob("../Corrected/*.csv"):
    flb = path.basename(fl).split(".")[0]
    if flb in already_known['REPOSITORY ID'].values:
        continue
    df = pd.read_csv(fl)
    df = df[["REPOSITORY ID", "PARTICIPANT FEATURES"]].drop_duplicates()
    if len(df) > 1:
        df = df.groupby("REPOSITORY ID")["PARTICIPANT FEATURES"].apply(
            lambda x: ";".join(list(x))).reset_index()
    df = df.rename(columns={"PARTICIPANT FEATURES": "DISCRIPTION"})
    new_known.append(df)
new_known = pd.concat(new_known)
new_known.to_csv("../fixed/project_summary_new.csv", index=False)

print(
    f"Please correct the file project_summary_new.csv before merging to project_summary.csv"
)
