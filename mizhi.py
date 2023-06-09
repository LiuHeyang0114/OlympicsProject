import os
import sys


class Printer():
    def __init__(self, filename="run.log"):
        self.terminal = sys.stdout
        self.filename = filename
        with open(self.filename, 'w'):
            pass

    def write(self, message):
        self.terminal.write(message)
        with open(self.filename, 'a') as f:
            f.write(message)

    def flush(self):
        pass


class Errorer():
    def __init__(self, filename="run.error"):
        self.terminal = sys.stderr
        self.filename = filename
        with open(self.filename, 'w'):
            pass

    def write(self, message):
        self.terminal.write(message)
        with open(self.filename, 'a') as f:
            f.write(message)

    def flush(self):
        pass
