from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import keyboard

compiler = Tk()
compiler.title('')
file_path = ''
filetypes = [('Python Files', '*.py'),('Java Files', '*.java')]

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    global filetypes
    path = askopenfilename(filetypes=filetypes)
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)
def save_as():
    global filetypes
    if file_path == '':
        path = asksaveasfilename(filetypes=filetypes)
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)
def run():
    global filetypes
    if file_path == '':
        path = asksaveasfilename(filetypes=filetypes)
        set_file_path(path)
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)


def type(word):
    keyboard.write(word)

class Helper:
    # qwerty

    keyboard.add_hotkey('SHIFT+)', lambda: type(")"), timeout=0)
    keyboard.add_hotkey('CTRL+ALT+f', lambda: type("]"), timeout=0)
    keyboard.add_hotkey('CTRL+ALT+b', lambda: type("}"), timeout=0)
    # qwerty

    keyboard.add_hotkey('SHIFT+9', lambda: type(")"), timeout=0)
    keyboard.add_hotkey('[', lambda: type("]"), timeout=0)
    keyboard.add_hotkey('SHIFT+[', lambda: type("}"), timeout=0)
class ShortCuts:
    class main:
        keyboard.add_hotkey('CTRL+b', lambda: run(), timeout=0)
        keyboard.add_hotkey('CTRL+s', lambda: type("]"), timeout=0)
    class python:
        keyboard.add_hotkey('CTRL+ALT+c', lambda: type("class classname:"), timeout=0)
        keyboard.add_hotkey('CTRL+ALT+d', lambda: type("def defname:"), timeout=0)
"""
def java_class_create():
    editor.insert(END,'''class classname {

}''')
"""


menu_bar = Menu(compiler)


class menu:
    class FileMenu:
        global menu_bar
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open', command=open_file)
        file_menu.add_command(label='Save', command=save_as)
        file_menu.add_command(label='Save As', command=save_as)
        file_menu.add_command(label='Exit', command=exit)
        menu_bar.add_cascade(label='File', menu=file_menu)

    class RunMenu:
        global menu_bar
        run_bar = Menu(menu_bar, tearoff=0)
        run_bar.add_command(label='Run', command=run)
        menu_bar.add_cascade(label='Run', menu=run_bar)

    class toolmenu:
        global menu_bar
        tool_bar = Menu(menu_bar, tearoff=0)
        """
        jav_subbar = Menu(tool_bar, tearoff=0)
        jav_subbar.add_command(label='class', command=java_class_create)
        tool_bar.add_cascade(label='Java', menu=jav_subbar)
        """
        menu_bar.add_cascade(label='Tools', menu=tool_bar)

    compiler.config(menu=menu_bar)


editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
