"""
Test of script cleaning_data
(10/10)
"""
import unittest
import pandas as pd

# Importa la función clean_dataframe del módulo donde se encuentra
from scripts.cleaning_data import clean_dataframe


class TestCleanDataFrame(unittest.TestCase):
    """
    Class of the different tests of clean data
    """
    def setUp(self):
        """
        Set Up Testing DataFrame
        """
        data = {"Column1": [1, 2, 3, None, 2],
                "Column2": ["A", "B", "C", "D", "B"]}
        self.df = pd.DataFrame(data)

    def test_dropna(self):
        """
        Testing if null values were deleted
        """
        cleaned_df = clean_dataframe(self.df)
        self.assertFalse(
            cleaned_df.isnull().values.any(),
            "La función no elimina correctamente los valores nulos",
        )

    def test_drop_duplicates(self):
        """
        Testing if duplicated values were repeated
        """
        cleaned_df = clean_dataframe(self.df)
        self.assertFalse(
            cleaned_df.duplicated().any(),
            "La función no elimina correctamente los duplicados",
        )

    def test_row_count(self):
        """
        Tests if the final number of rows displayed are correct
        """
        cleaned_df = clean_dataframe(self.df)
        expected_rows = len(self.df.dropna().drop_duplicates())
        self.assertEqual(
            len(cleaned_df),
            expected_rows,
            "El número de filas no se actualiza correctamente",
        )


if __name__ == "__main__":
    unittest.main()
