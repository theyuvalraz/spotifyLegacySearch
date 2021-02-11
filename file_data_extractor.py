from os import listdir
from string import digits

remove_digits = str.maketrans('', '', digits)


def list_files(my_path):
    file_list = listdir(my_path)
    parsed_list = [name
                       .replace(".mp3", "")
                       .replace("_", " ")

                       .translate(remove_digits)
                       .lstrip("- ").split("-")
                   for name in file_list]
    parsed_list_final = []

    for i in parsed_list:
        current_name = [part.lstrip("-.").rstrip("-.") for part in i]
        parsed_list_final.append(''.join(current_name))
    return parsed_list_final
