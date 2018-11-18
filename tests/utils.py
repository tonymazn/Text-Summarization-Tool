# -*- coding: utf-8 -*-

import os.path


def create_file(folder, file, context):
     #"C:\\CS410\\Data\\duc2004_2\\system"
    f = open(os.path.join(folder, file), "w")
    f.write(context)
    f.close()

def delete_file(folder, file):
    os.remove(os.path.join(folder, file))

def read_file(folder, file):
    f = open(os.path.join(folder, file), "r", encoding="utf-8")
    context = f.read()
    f.close()
    return context

def read_file_with_path(file_with_path):
    f = open(file_with_path, "r", encoding="utf-8")
    context = f.read()
    f.close()
    return context

def get_dir_list(folder):
    return os.listdir(folder)

def get_file_list(folder):
    return os.listdir(folder)

def get_newline():
    return "\n"

