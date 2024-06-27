import os
import re


def generate_all_ui2py(path: str):
    files = os.listdir(path)
    ui_list = []
    pattern = re.compile(r'.*\.ui')
    for it in files:
        if pattern.match(it):
            ui_list.append(it)
    print(ui_list)

    for it in ui_list:
        file_path = os.path.join(path, it)
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyuic5 {file_name_without_extension}.ui -o ui_{file_name_without_extension}.py'
        print(cmd)
        os.popen(cmd)


if __name__ == '__main__':
    generate_all_ui2py(os.path.dirname((os.path.abspath(__file__))))