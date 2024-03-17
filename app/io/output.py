import pandas as pd


def output_text_to_console(text):
    """
    Функція для виведення тексту в консоль.

    Args:
        text: Текст, який буде виведено на консоль.
    """

    print(text)


def write_text_to_file(filename, text):
    """
    Функція для запису тексту у файл.

    Args:
        filename: Шлях до файлу.
        text: Текст, який буде записано у файл.
    """

    with open(filename, 'w') as file:
        file.write(text)


def write_text_to_file_pandas(filename, text):
    """
    Функція для запису тексту у файл за допомогою бібліотеки Pandas.

    Args:
      filename: Шлях до файлу.
      text: Текст, який буде записано у файл.
    """

    try:
        df = pd.DataFrame({'Text': [text]})
        df.to_csv(filename, index=False)
    except Exception as e:
        print(e)
