# ./source/budou_x.py
def budou_x_convert(input_file, output_file):
    text_file = open(input_file, 'r')
    text = text_file.read()
    text_file.close()

    import budoux

    parser = budoux.load_default_japanese_parser()
    converted_text = parser.translate_html_string(text)
    print(converted_text)

    f = open(output_file, 'w')
    f.write(converted_text)
    f.close()