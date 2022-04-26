import pandas as pd
from os import system, path, makedirs
import click
import requests
import json
from sys import argv


print(
    "Please make sure sra-toolkit is installed on your system"
    " and the path to it is added to your PATH variable"
)


def run(csv, out_dir):
    """TODO: Docstring for run.
    Please remove partial download file to initiate new download

    :csv: TODO
    :out_dir: TODO
    :returns: TODO

    """
    df = pd.read_csv(argv[1])
    projects = df["REPOSITORY ID"].unique()

    for pr in projects:
        makedirs(pr, exist_ok=True)
        samples = df[df["REPOSITORY ID"] == pr]["REPOSITORY ID"].unique()
        for s in samples:
            # TODO: add command to download fastq files
            if not s.startswith("m"):  # M is for mg-rast sequences
                system(f"fastq-dump --split-3 -O {pr} --gzip {s}")
            # TODO: Check if files are paired
            else:
                link = f"https://api.mg-rast.org/download/{s}"
                f = requests.get(link)
                json_text = f.text
                for k in json.loads(json_text)["data"]:
                    if k["stage_name"] == "upload":
                        system(f"wget -c {k['url']} -O {pr}/{k['file_name']}")
