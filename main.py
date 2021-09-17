
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import getpass
import os
import sys
import ctypes
import os
import win32process

#Turn off terminal
hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
if hwnd != 0:      
    ctypes.windll.user32.ShowWindow(hwnd, 0)      
    ctypes.windll.kernel32.CloseHandle(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    os.system('taskkill /PID ' + str(pid) + ' /f')

# determine if the application is a frozen `.exe` (e.g. pyinstaller --onefile) 
if getattr(sys, 'frozen', False):
    OUTPUT_PATH = os.path.dirname(sys.executable)
# or a script file (e.g. `.py` / `.pyw`)
elif __file__:
    OUTPUT_PATH = os.path.dirname(__file__)
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#main functions
def check_input_valid():
    try:
        name = entry_name.get()
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        if (name != "" and day != "" and month != "" and year != ""):
            if (1000 <= year <= 10000):
                if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                    if (1 <= day <= 31):
                        return True
                elif (month == 4 or month == 6 or month == 9 or month == 11):
                    if (1 <= day <= 30):
                        return True
                elif (month == 2):
                    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
                        if (1 <= day <= 28):
                            return True
                    else:
                        if (1 <= day <= 29):
                            return True
        return False
    except:
        return False

def save_data():
    if (check_input_valid()):
        # determine if the application is a frozen `.exe` (e.g. pyinstaller --onefile) 
        if getattr(sys, 'frozen', False):
            file_w = open(f"{os.path.dirname(sys.executable)}/data.txt", "a", encoding="utf-8")
        # or a script file (e.g. `.py` / `.pyw`)
        elif __file__:
            file_w = open(f"{os.path.dirname(__file__)}/data.txt", "a", encoding="utf-8")
        file_w.write(f"{entry_name.get()}_{entry_day.get()}/{entry_month.get()}/{entry_year.get()}\n")
        file_w.close()
    entry_name.delete(0, END)
    entry_day.delete(0, END)
    entry_month.delete(0, END)
    entry_year.delete(0, END)

def write_bat():
    USER = getpass.getuser()
    file_bat = open(f"C:\\Users\\{USER}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\findBirthday.bat", "w", encoding="utf-8")
    # determine if the application is a frozen `.exe` (e.g. pyinstaller --onefile) 
    if getattr(sys, 'frozen', False):
        file_bat.write(f"python {os.path.dirname(sys.executable)}\\findBirthday.pyw")
    # or a script file (e.g. `.py` / `.pyw`)
    elif __file__:
        file_bat.write(f"python {os.path.dirname(__file__)}\\findBirthday.pyw")
    file_bat.close()

try:
    write_bat()
    window = Tk()

    window.geometry("1000x800")
    window.configure(bg = "#2A0404")
    window.title("Birthday Management")
    iconPhoto = PhotoImage(file = "assets/cake.png")
    window.iconphoto(False, iconPhoto)


    canvas = Canvas(
        window,
        bg = "#2A0404",
        height = 800,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        500.0,
        400.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        584.0,
        245.5,
        image=entry_image_1
    )
    entry_name = Entry(
        bd=0,
        bg="#678799",
        highlightthickness=0,
        font = ("Arial", 50)
    )
    entry_name.place(
        x=250.5,
        y=183.0,
        width=667.0,
        height=123.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        85.0,
        247.0,
        image=image_image_2
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        488.5,
        588.0,
        image=entry_image_2
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    save_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=save_data,
        relief="flat"
    )
    save_button.place(
        x=362.0,
        y=672.0,
        width=247.0,
        height=94.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        500.0,
        505.0,
        image=image_image_3
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        138.5,
        587.5,
        image=entry_image_3
    )
    entry_day = Entry(
        bd=0,
        bg="#4294B7",
        highlightthickness=0,
        font = ("ink Free", 40)
    )
    entry_day.place(
        x=100.0,
        y=559.0,
        width=120.0,
        height=55.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        843.0,
        587.5,
        image=entry_image_4
    )
    entry_month = Entry(
        bd=0,
        bg="#C8D075",
        highlightthickness=0,
        font = ("ink Free", 40)
    )
    entry_month.place(
        x=451.0,
        y=540.0,
        width=75.0,
        height=94.0
    )
    entry_year = Entry(
        bd=0,
        bg="#A6B8F8",
        highlightthickness=0,
        font = ("ink Free", 40)
    )
    entry_year.place(
        x=785.0,
        y=559.0,
        width=128.0,
        height=55.0
    )
    window.resizable(False, False)
    window.mainloop()
except Exception:
    print(Exception)
    a = input()
