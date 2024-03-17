import app.io.input as input
import app.io.output as output


def main():
    console_text = input.input_text_from_console()
    output.output_text_to_console(console_text)
    output.write_text_to_file("data/output.txt", console_text)
    file_text = input.read_text_from_file("data/input.txt")
    output.output_text_to_console(file_text)

    output.write_text_to_file_pandas("data/output_pandas.txt", console_text)
    pandas_file_text = input.read_text_from_file_pandas("data/input_pandas.txt")
    output.output_text_to_console(pandas_file_text)


if __name__ == "__main__":
    main()
