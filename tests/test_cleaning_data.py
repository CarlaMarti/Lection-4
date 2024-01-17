import unittest
import pandas as pd

# Importa la función clean_dataframe del módulo donde se encuentra
from scripts.cleaning_data import clean_dataframe


class TestCleanDataFrame(unittest.TestCase):
    def setUp(self):
        # DataFrame de prueba
        data = {"Column1": [1, 2, 3, None, 2], "Column2": ["A", "B", "C", "D", "B"]}
        self.df = pd.DataFrame(data)

    def test_dropna(self):
        # Se eliminan los valores nulos?
        cleaned_df = clean_dataframe(self.df)
        self.assertFalse(
            cleaned_df.isnull().values.any(),
            "La función no elimina correctamente los valores nulos",
        )

    def test_drop_duplicates(self):
        # Se eliminan los duplicados?
        cleaned_df = clean_dataframe(self.df)
        self.assertFalse(
            cleaned_df.duplicated().any(),
            "La función no elimina correctamente los duplicados",
        )

    def test_row_count(self):
        # El numero de filas se actualiza correctamente?
        cleaned_df = clean_dataframe(self.df)
        expected_rows = len(self.df.dropna().drop_duplicates())
        self.assertEqual(
            len(cleaned_df),
            expected_rows,
            "El número de filas no se actualiza correctamente",
        )


if __name__ == "__main__":
    unittest.main()
