"""Main code. I had to modify it to complete the task."""
import os
import click
import pandas as pd
from filtering_data import FilterData


# Click command and options
@click.command(short_help="Parser to manage inputs for BooksDataset")
@click.option("-id", "--input_data", required=True, help="Path to dataset")
@click.option("-o", "--output", default="outputs", help="Folder")
@click.option("-f", "--filtering", is_flag=True, help="Enable filtering")
@click.option("-y", "--year", help="Set a year (e.g., 2002)")
def main(input_data, output, filtering, year):
    """
    Deal with the input data and send it to other functions.
    """
    df = pd.read_csv(input_data)
    print(f"WORKING WITH THIS DATASET: {input_data}")
    print("\nSample of the dataframe:\n", df.sample(3))
    print("\nNumber of rows:", len(df))
    print("\nColumns:", list(df.columns))
    print("\nDescriptive statistics of the DataFrame:\n", df.describe())

    if filtering:
        print("\nI AM FILTERING!\n")
        filter_obj = FilterData(df)

        if year:
            df = filter_obj.filter_by_year(year)

        print("\nDATA SAVED!\nTotal number of rows:", df.shape)

    if not os.path.exists(output):
        os.makedirs(output)

    df.to_csv(f"{output}/{'Result'}.csv", index=None)


if __name__ == "__main__":
    main()
