import pandas as pd

def load_dataset(filename):

    extension = filename.rsplit(".",1)[-1]
    if extension.lower() == "csv": #added .lower() in case the extension is in capital letters
        return pd.read_csv(filename)
    else:
        raise TypeError(f"\n\n\n\n\n\nThe extension is {extension} and not CSV, please try again!\n\n\n\n\n\n")
