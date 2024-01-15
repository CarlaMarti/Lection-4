#NOTES IN CLASS (SOME OF THEM COMMENTED TO AVOID INTERRRUPTING THE CODE)
#HOMEWORK INCLUDED
#EXTRA: YOU CAN SAVE THE RESULTING DATA WITH THE NAME YOU WANT


# first : I must activate the environment, opening anaconda etc --> conda activate advancedpython24 
# second: open the script --> python script_class_2.py 
# then I add the options I want -id or -name or ...

# in case of wanting to know the options available --> python script_class_2.py --help

#options:

#to choose the dataset in which you want to work: -id BooksDatasetClean.csv 
#if I want to save it in a given folder: -o NameofFolder
    #(if I want to save it in a new folder: -o NewName)

#if I want to filter: -f
#if I want to filter by year: -y 2003
#if I want to filter by month: -m July
#if I want to filter by price: -p 4.8
#if I want to filter by all at once: -y 2003 -m July -p 4.8

#extra: if I want to name the filtered data in a given way: -n name

#example:

#python script_lection2.py -id BooksDatasetClean.csv -f -y 2000 -m July -p 5.8 -n holaquetal -o NUEVACARPETA

import os
import click
import pandas as pd 

class filter_data:
    """
    Class to filter data by year and month of publication.
    """
    def __init__(self, df): 
        """
        En resumen, este constructor está diseñado para aceptar un DataFrame (df) como argumento y asignarlo al atributo df del objeto. 
        Este es un patrón común en la programación orientada a objetos cuando se desea inicializar el estado de un objeto con valores específicos al crearlo.
        """
        self.df = df    

    def filter_by_year(self, year):
        """
        Filter books by a given minimum year.
        """
        
        year = int(year)
        return self.df[self.df['Publish Date (Year)'] > year]
    
    def filter_by_month(self, month):
        """
        Filter books by a given month.
        """
        return self.df[self.df['Publish Date (Month)'] == month]
    
    def filter_by_price(self, price):
        """
        Filter books by a given minimum price.
        """
        
        price = float(price)
        return self.df[self.df['Price Starting With ($)'] > price]
 
def load_dataset(filename):

    extension = filename.rsplit(".",1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    else:
        raise TypeError(f"\n\n\n\n\n\nThe extension is {extension} and not CSV, please try again!\n\n\n\n\n\n")


@click.command(short_help='Parser to manage inputs for BooksDataset')#info
@click.option('-id','--input_data', required=True, help='Path to my input dataset')#
@click.option('-o','--output', default="outputs", help="Folder to save all outputs")
@click.option('-f','--filtering', is_flag=True, help="Set a filtering or not")
@click.option('-p', '--price', help = "Set a minimum price like this: 5.29")
@click.option('-m', '--month', help = "Set a month (you have to write the month like this: July)")
@click.option('-y', '--year', help = "Set a year (you have to write it like this: 2002)")

#extra:
@click.option('-n', '--name', help = "Set a name to your result!")

def main(input_data, output, filtering, price, month, year,name):
    """
    Deal with the input data and send to other functions, in this case inside the class filter_data.
    """
    
    print("WE WILL BE WORKING WITH THIS DATASET:", input_data)
    print("\n\n\n")

    try:
        df = load_dataset(input_data, sep=',')
    except FileNotFoundError as e:
        raise FileNotFoundError(f"\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CAUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n\n FILE COULDN'T BE FOUND: {e}\n\n\n\n")

    print("HERE YOU HAVE A SAMPLE!\n\n\n",df[['Title', 'Price Starting With ($)', 'Publish Date (Month)', 'Publish Date (Year)']].sample())



    if filtering:
        print("\n\n\nI AM FILTERING!\n\n\n")
        filter_obj = filter_data(df)  # Create a single instance of filter_data

        if year:
            df = filter_obj.filter_by_year(year)
        
        if month:
            df = filter_obj.filter_by_month(month) 
        
        if price:
            df = filter_obj.filter_by_price(price)
        
        # df = filter_data(df).filter_by_price(price) 
                    
        # df = df[df['Publish Date (Month)']=='January']
        # df = df[df['Publish Date (Year)'] > 2020]

        print("DATA SAVED! SHAPE OF THE NEW DATASET:      ",df.shape,"\n\n\n")
           
            # debugger
            #import pdb;pdb.set_trace()  --> no lo uso porque de momento todo funciona y prefiero que no se esté parando todo el rato
            # I have everything available before that
            #Una vez se te ha parado puedes poner q(para quit) o c (para continuar)

    
    if not os.path.exists(output):              #if the directory output is not found, we will generate one called as the user said
        os.makedirs(output)
    
    df.to_csv(f'{output}/{name}.csv', index=None)
    #we save the file where we want (output) or it will save it in "outputs"

    

if __name__ == '__main__':
    print('\n\n\nTHIS IS WORKING!!\n\n\n')
    main()