#!/usr/bin/env python3
import pathlib
import os
import random
import string
from signal import signal, SIGINT
from sys import exit, maxsize, platform
from argparse import ArgumentParser
import getch
from pynput.keyboard import Controller, Key


class bcolors:
    """
    Terminal Colors
    """
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


class DictionaryAndVariables:
    """
    This class was created to trim long methods.
    """
    def __init__(self, args):
        self.map_dirs = {}
        self.end_level = 4
        self.printed_dirs = 15
        if args.level:
            self.end_level = int(args.level)
        if args.all:
            self.end_level = maxsize


def handler(signal_received, frame):
    """
    Handle any cleanup here.
    """
    exit(0)


def random_chars():
    """
    Returns y random characters
    """
    y = random.choice('23')
    if y == '2':
        return ''.join(random.choice('abcdefghijklmn') for x in range(int(y)))
    return ''.join(random.choice('oprstuvwxyz') for x in range(int(y)))


def find_key(dict, data):
    """
    Find key of dictionary from value.
    """
    for key, value in dict.items():
        if value == data:
            return key


def get_os_name():
    """
     Return OS name.
    """
    return os.name


def insert_shortcut_and_path_to_dictonary(dirs, map_dirs, root):
    """
    Inserts new path (root + dir) to the dictionary with a shortcut. Returns the dictionary.
    """
    for dir in dirs:
        while True:
            dict_key = random_chars().lower()
            if dict_key not in map_dirs:
                if get_os_name() != 'nt':  # choose correct OS
                    map_dirs[dict_key] = root + "/" + dir
                else:
                    map_dirs[dict_key] = root + "\\" + dir
                break
    return map_dirs


def check_if_to_continue_or_not(dict_and_var):
    """
    Reads input char. If it's 'n' print the next 15 dirs/files. If not, go to
    read_input_and_type_command_to_terminal(). Returns variable to be used after.
    """
    char = getch.getch()
    if char != 'n':
        read_input_and_type_command_to_terminal(char, dict_and_var.map_dirs)
        handler("", "")
    dict_and_var.printed_dirs = 16  # this is 16 because of the -1 after the call of this method
    return dict_and_var.printed_dirs


def handle_dirs(dirs, level, root, dict_and_var):
    """
    Inserts new path to dictionary if the root has dirs. Then, prints the path with shortcut if
    there is. Returns dictonary to be used after.
    """
    indent = (' ' * 2 * level + ' ' * (level - 1) + '|~')
    if dirs:
        dict_and_var.map_dirs = insert_shortcut_and_path_to_dictonary(dirs, dict_and_var.map_dirs,
                                                                   root)
    dict_key = find_key(dict_and_var.map_dirs, root)
    if dict_key == None:
        dict_key = ''
    print(bcolors.OKBLUE + '{}{}/'.format(indent, os.path.basename(
        root)) + bcolors.OKCYAN + '   {}'.format(dict_key) + bcolors.ENDC)
    return dict_and_var.map_dirs


def handle_files(args, files, level):
    """
    Prints File paths.
    """
    if not args.directories:
        subindent = ' ' * 2 * (level + 1) + ' ' * (level) + '|-'
        for f in files:
            print('{}{}'.format(subindent, f))


def print_tree_and_get_dict_of_path_and_shortcuts(args, startpath, dict_and_var):
    """
    Starts a loop to parse the whole file tree of the startpath, it updates the dictionary where
    the paths and shortcuts are, prints dirs and files and checks how to respond based on the
    terminal arguments. Returns dictionary with the paths.
    """
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if level > dict_and_var.end_level:
            continue
        dict_and_var.map_dirs = handle_dirs(dirs, level, root, dict_and_var)
        handle_files(args, files, level)
        if args.control and dict_and_var.printed_dirs == 0:
            dict_and_var.printed_dirs = check_if_to_continue_or_not(dict_and_var)
        dict_and_var.printed_dirs = dict_and_var.printed_dirs - 1
    return dict_and_var.map_dirs


def get_dict_of_paths(startpath, args):
    """
    Prints the File Tree of the startpath and returns a dictionary with shortcuts as a key and the
    path as a value.
    """
    dict_and_var = DictionaryAndVariables(args)
    if args.control:
        print("Type shortcut, " + bcolors.WARNING + 'n' + bcolors.ENDC + " to continue" + " or "
              + bcolors.WARNING + 'q' + bcolors.ENDC + " to quit.. : ")
    return print_tree_and_get_dict_of_path_and_shortcuts(args, startpath, dict_and_var)


def parse_input():
    """ Parse input. """
    parser = ArgumentParser(__doc__)
    parser.add_argument('-p', '--path', action='store',
                        required=False, help='Prints from the path you want to navigate from.')
    parser.add_argument('-l', '--level', action='store',
                        required=False, help='Prints x levels. Default is 4.')
    parser.add_argument('-a', '--all', action='store_true',
                        required=False, help='Prints the whole tree.')
    parser.add_argument('-d', '--directories', action='store_true',
                        required=False, help='Prints only directories.')
    parser.add_argument('-c', '--control', action='store_true',
                        required=False, help='Prints 15 directories and with n the next 15 etc.')
    return parser.parse_args()


def clear_promt_text():
    """
    Prints <backspace> to clear pormt text.
    """
    for i in range(3):
        print("\b \b", end='', flush=True)


def type_command_and_clear_screen_text(map_dirs, shortcut):
    """
    Gets selected path and types the cd command, so user can go to selected dir.
    """
    final_path = map_dirs[shortcut].split('\\')
    keyboard = Controller()
    for char in "cd " + ('/'.join(final_path)):
        keyboard.press(char)
        keyboard.release(char)
        clear_promt_text()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def read_input_and_type_command_to_terminal(char, map_dirs):
    """
    Reads chars. If 'q' quits and if input is a proper shortcut it types the command.
    """
    if char == 'q':
        handler("", "")
    shortcut = char + getch.getch()
    while len(shortcut) < 4:
        if shortcut in map_dirs.keys():
            type_command_and_clear_screen_text(map_dirs, shortcut)
            break
        shortcut = shortcut + getch.getch()


def main():
    """
    1. Receive the Arguments.
    2. Call print_tree() to get the dictionary
    3. Read Input
    4. Type cd <destination path>
    """
    args = parse_input()
    startpath = str(os.getcwd())
    if args.path:
        startpath = args.path
    map_dirs = get_dict_of_paths(startpath, args)
    print("Type shortcut or " + bcolors.WARNING + 'q' + bcolors.ENDC + " to quit.. : ")
    char = getch.getch()
    read_input_and_type_command_to_terminal(char, map_dirs)


if __name__ == "__main__":
    signal(SIGINT, handler)
    main()
