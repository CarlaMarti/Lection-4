class filter_data:
    """
    Class to filter data by year and month of publication.
    """
    def __init__(self, df): 
        """
        Aceptar un DataFrame (df) como argumento y asignarlo al atributo df del objeto.
        """
        self.df = df    

# In both datasets you can filter by year, the issue here is that the columns are called differently
# I solved this issue with the following code:

    def filter_by_year(self, year): 
        """
        Filter books or films by a given minimum year.
        """
        year = int(year)
        relevant_column = 'Publish Date (Year)' if 'Publish Date (Year)' in self.df.columns else 'Year'
        return self.df[self.df[relevant_column] > year]

    
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
    
    def filter_by_genre(self, genre):
        """
        Filter the DataFrame based on a specified genre.
        """
        return self.df[self.df["Genre"] == genre]
    
    def filter_by_tickets(self, tickets_sold):
        """
        Filter a minimum number of tickets sold.
        """
        return self.df[self.df['Tickets Sold'] > int(tickets_sold)]
    
        #ARREGLAR
         

if __name__ == "__main__":
    pass