# stellagama.py
# A module with various useful functions by Omer Golan-Joel
# v3.1 - July 19th, 2020
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# import modules
import random
import os
import platform

# functions


def yn():
    query = 1
    while query == 1:
        answer = input("Y/N: ")
        if answer.lower() == "y":
            return True
            break
        if answer.lower() == "n":
            return False
            break
        else:
            print("Invalid Answer")


def dice(n, sides):
    die = 0
    roll = 0
    while die < n:
        roll = roll + random.randint(1, sides)
        die += 1
    return roll


def pseudo_hex(num):
    num = int(num)
    code = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num = code[num]
    return num


def current_dir():
    if platform.system() == "Windows":
        directory = os.listdir(".\\")
    else:
        directory = os.getcwd()
    return directory


def check_file_exists(check_file):
    if check_file in current_dir():
        file_exists = True
    else:
        file_exists = False
    return file_exists


def savefile(extension):
    filename = str(input("Please enter file name to generate: "))
    filecheck = filename + "." + extension
    if check_file_exists(filecheck):
        print(" ")
        print("File already exists. Overwrite?")
        overwrite = yn()
        if overwrite == "y":
            return filename
        if overwrite == "n":
            filename = input("Please enter new file name to generate: ")
    return filename



def savefile_command_line(file):
    if check_file_exists(file):
        print("\nFile already exists. Overwrite?")
        overwrite = yn()
        if overwrite:
            return file
        if not overwrite:
            filename = input("Please enter new file name to generate: ")
            return filename
    else:
        return file


def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def random_line(filename):
    with open(filename, "r", encoding='utf-8', errors='ignore') as line_list:
        line = random.choice(line_list.readlines())
        line = line.strip()
    return line


class Getch:
    def __init__(self):
        try:
            self.impl = GetchWindows()
        except ImportError:
            self.impl = GetchUnix()

    def __call__(self):
        return self.impl()


class GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


def getkeypress():
    if platform.system() == "Windows":
        directory = os.listdir(".\\")
        key = Getch()
        return key().decode()
    else:
        key = Getch()
        return key()


def list_stringer(input_list):
    output_list = []
    for item in input_list:
        output_list.append(str(item))
    return ' '.join(output_list)


def second_highest(number_list):
    secondary = 0
    maximal = max(number_list)
    for number in number_list:
        if maximal > number > secondary:
            secondary = number
        else:
            number = number
    return secondary
