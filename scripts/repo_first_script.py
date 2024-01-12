"""
Script to make uptdates to github"""

import click
import pandas as pandas

@click.command(short_help='Parser to import dataset')
@click.option('-f','--filename', required=True, help='File to import')


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
    
    def filter_price(self,price):
        """
        Filter by price
        """
        price = float(price)
        return self.df[self.df['Price Starting With ($)'] > price]


def main(filename):

    """
    Main function
    """
    pass

    df = pd.read_csv(filename)
    response=filter_data.filter_price(12)

if __name__ =="__main__":
    main()

#hola

