"""Launches all installers specified in setup/todo.txt, processing the OS tags."""
from sys import platform as _platform
import sys
import os
import subprocess

# get the data
with open("setup/todo.txt") as f:
    text = f.read()

# split by line then by OS and command
lines = text.split("\n")
splitted = list()
for line in lines:
    splitted.append([line.split(" ")[0], line.split(" ")[1:]])

# launch the scripts
for line in splitted:
    if line[0] in ["linux", "darwin", "all"] and _platform in ["linux", "linux2", "darwin"]:
        if line[1].split(".")[-1] == "sh":
            subprocess.check_output(["setup/" + line[1]])
        elif line[1].split(".")[-1] == "py":
            subprocess.check_output(["python3 setup/" + line[1]])
    elif line[0] in ["windows", "all"] and _platform in ["win32", "win64"]:
        if line[1].split(".")[-1] == "py":
            sys.path.append("/".join(("setup/" + line[1]).split("/")[:-1]))
            __import__(line[1].split("/")[-1].split(".")[:-1])
        elif line[1].split(".")[-1] == "bat":
            os.system("setup/" + line[1])
