#! /usr/bin/python3

import path

# With a fixed path
# import local_lib.path as path

def main():
    directory = path.Path('local_lib/tmp')
    directory.mkdir_p()
    file_tmp = path.Path('local_lib/tmp/tmp.txt')
    file_tmp.touch()
    file_tmp.write_text("toto")
    print(file_tmp.text())


if __name__ == '__main__':
    main()