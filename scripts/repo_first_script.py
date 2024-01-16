#COMAND LINE OPTIONS

#if I want to work on a given dataset: -id NameDataset
#if I want to save the result in a given folder: -o NameofFolder   
   #(if I want to save it in a new folder: -o NewName)
#if I want to filter: -f
#if I want to filter by year: -y 2003
#if I want to filter by month: -m July
#if I want to filter by price: -p 4.8
#if I want to filter by genre: -g Action
#if I want to filter by number of tickets sold: -t number
#if I want to filter by all at once: -y 2003 -m July -p 4.8
#if I want to name the filtered data in a given way: -n name

#if I want to see the options: --help

#examples (all included):

# DATASET 1:
#python scripts/repo_first_script.py -id datasets/BooksDatasetClean.csv -f -y 2000 -m July -p 5.8 -n holaquetal -o NUEVACARPETA

#DATASET 2:
#python scripts/repo_first_script.py -id datasets/FilmGenreStats.csv -f -y 2000 -g Action -n holaquetal -o NUEVACARPETA

import os
import click
import pandas as pd 
from filtering_data import filter_data
from loading_datasets import load_dataset
 
@click.command(short_help='Parser to manage inputs for BooksDataset')
@click.option('-id','--input_data', required=True, help='Path to my input dataset')
@click.option('-o','--output', default="outputs", help="Folder to save all outputs")
@click.option('-f','--filtering', is_flag=True, help="Set a filtering or not")
@click.option('-p', '--price', help = "Set a minimum price like this: 5.29")
@click.option('-m', '--month', help = "Set a month (you have to write the month like this: July)")
@click.option('-y', '--year', help = "Set a year (you have to write it like this: 2002)")
@click.option('-g', "--genre", help="Set a genre (you have to write the genre like this: Action)")
@click.option('-t', "--tickets_sold", help="Set a minimum number of tickets sold (you have to write the genre like this: 2889395823)")
@click.option('-n', '--name', help = "Set a name to your result")
@click.option('-c', '--cleaning', is_flag=True, help = "Clean the dataset or not")


def main(input_data, output, filtering, price, month, year, genre, name, tickets_sold, cleaning):
    """
    Deal with the input data and send to other functions, in this case inside the class filter_data.
    """
    
    print("WE WILL BE WORKING WITH THIS DATASET:", input_data)
    print("\n\n\n")

    try:
        df = load_dataset(input_data)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CAUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n\n FILE COULDN'T BE FOUND: {e}\n\n\n\n")

    print("Sample of the dataframe:\n\n\n",df.sample(3))
    
    print("\n\n\nNumber of rows: ", len(df))
    
    print("\n\n\nNumber of columns: ", len(df.columns))
    
    print("\n\n\nColumns: ", list(df.columns))
    
    print("\n\n\nDescriptive statistics of the DataFrame:\n\n\n", df.describe())

    print("\n\n\nNull values in each column:\n\n\n", df.isnull().sum())

    if cleaning:
        
        print("\n\n\nI AM CLEANING!")
        
        df_cleaned = df.dropna()

        df_cleaned = df_cleaned.drop_duplicates()

        df = df_cleaned

        print("\n\n\nNew number of rows: ", len(df))


    if filtering:
        print("\n\n\nI AM FILTERING!\n")
        
        filter_obj = filter_data(df)  # Create a single instance of filter_data

        if year:
            df = filter_obj.filter_by_year(year)
            print("\n\nNumber of rows (year filter):      ", len(df))
        
        if month:
            df = filter_obj.filter_by_month(month)
            print("\n\nNumber of rows (month filter):      ", len(df))
        
        if price:
            df = filter_obj.filter_by_price(price)
            print("\n\nNumber of rows (price filter):      ", len(df))
        
        if genre:
            df = filter_obj.filter_by_genre(genre) 
            print("\n\nNumber of rows (genre filter):      ", len(df))
        
        if tickets_sold:
            df = filter_obj.filter_by_tickets(tickets_sold) 
            print("\n\nNumber of rows (tickets sold filter):      ", len(df))
    
       
        print("DATA SAVED! \n\nTotal number of rows:      ", df.shape)
    
#if the directory output is not found, we will generate one called as the user said
        
    if not os.path.exists(output):              
        os.makedirs(output)
    
    # we save the file where the user wants (output) or it will save it in "outputs"

    df.to_csv(f'{output}/{name}.csv', index=None) 

if __name__ == '__main__':
    print('\n\n\nTHIS IS WORKING!!\n\n\n')
    main()