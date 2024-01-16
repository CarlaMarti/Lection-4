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


if __name__ == "__main__":
    pass