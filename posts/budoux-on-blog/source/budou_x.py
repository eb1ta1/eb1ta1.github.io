# ./source/budou_x.py
import sys
args = sys.argv
base_path = args[1]
input_file = args[2]
output_file = args[3] 

def budou_x_convert():
    text_file = open(base_path + input_file, 'r')
    text = text_file.read()
    text_file.close()

    import budoux

    parser = budoux.load_default_japanese_parser()
    converted_text = parser.translate_html_string(text)
    print(converted_text)

    f = open(base_path + output_file, 'w')
    f.write(converted_text)
    f.close()

budou_x_convert()

# usage
# $ python3 budou_x.py base_path input_file output_file