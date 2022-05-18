# https://stackoverflow.com/questions/69297359/is-there-a-way-to-run-all-jupyter-notebooks-inside-a-directory
import papermill as pm
from glob import glob

for nb in glob('*.ipynb'):
    pm.execute_notebook(
        input_path=nb,
        output_path=nb  # Path to save executed notebook
    )
