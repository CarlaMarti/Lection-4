"""
Script that loads a dataset.
10/10
"""

import pandas as pd


def load_dataset(filename):
    """
    Function that loads a dataset.
    """
    extension = filename.rsplit(".", 1)[-1]
    if (
        extension.lower() == "csv"
    ):  # added .lower() in case the extension is in capital letters
        return pd.read_csv(filename)
    raise TypeError(f"The extension is {extension} and not CSV!")
