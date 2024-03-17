import pandas as pd


def input_text_from_console():
    """
    Функція призначена для зчитування тексту від з консолі.

    Returns:
        str: Введений текст.
    """

    return input("Введіть текст: ")


def read_text_from_file(filename):
    """
   Функція призначена для зчитування тексту з файлу.

   Args:
       filename: Шлях до файлу.

   Returns:
       str: Зчитаний текст з файлу.
   """

    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""


def read_text_from_file_pandas(filename):
    """
    Функція призначена для зчитування тексту з файлу за допомогою бібліотеки Pandas.

    Args:
        filename: Шлях до файлу.

    Returns:
        str: Зчитаний текст з файлу.
    """

    try:
        df = pd.read_csv(filename)
        if 'Text' in df.columns:
            return str(df['Text'].iloc[0])
        else:
            return ""
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(e)
        return ""
