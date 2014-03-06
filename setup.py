#usage python.exe setup.py py2exe <file>
#where <file> is the python file you want to make an exe out of.
from distutils.core import setup
import py2exe

from glob import glob
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]
data_files += [(".", glob(r'.\*.txt'))]

import sys

print sys.argv

file = sys.argv[2]
sys.argv = sys.argv[:-1]

setup(console=[file],data_files=data_files)


