from glob import glob
import pandas as pd

for fl in glob("../Originals/*.csv"):
    df = pd.read_csv(fl)
    df = df[~pd.isna(df["REPOSITORY ID"])]
    for project in df["REPOSITORY ID"].unique():
        df_project = df[df["REPOSITORY ID"] == project]
        df_project.to_csv(
            f"../Originals/Fragmented/{project}.csv", index=False)
