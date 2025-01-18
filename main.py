#!/bin/python3

import sys

filename = 'dash.clips'

def _clean():
    with open(filename, 'w') as f:
        f.write('')

def _write(str):
    with open(filename, 'a') as f:
        f.write(str)

def _read():
    with open(filename, 'r') as f:
        return f.read()

def copy(string):
    _write(string)

def paste(string):
    return _read()

if sys.argv[-1] in ('c', 'copy'):
    _clean()
    if sys.stdin.isatty():
        print("Type anything you want to copy. Press ^C to confirm.")
        try:
            while True:
                _write(input() + '\n')
        except KeyboardInterrupt:
            print("\nCopying finished.")
    else:
        #write(input())
        for line in sys.stdin:
            print(line, end='')
            _write(line)
            
        print("\nCopying finished.")

else:
    print(_read())
