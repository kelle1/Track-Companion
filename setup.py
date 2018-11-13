from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python37\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python37\\tcl\\tk8.6"

setup(name='Track Companion Test',
      version='0.1',
      options={'build_exe': {'packages': ['PySimpleGUI']}},
      description='Track Companion Test',
      executables=[Executable('Track_Companion.py')])
