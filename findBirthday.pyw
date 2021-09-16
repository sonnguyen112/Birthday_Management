from datetime import date
from pathlib import Path
from tkinter import *
from pygame import mixer
import schedule
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

mixer.init()

output_data = []
def open_new_window():
    mixer.music.load(f"{Path(__file__).parent}\\assets\\\HappyBirthday-VA_9ey.mp3")
    mixer.music.play(loops=-1)
    window = Tk()

    window.geometry("750x769")
    window.configure(bg = "#9FC6A6")


    canvas = Canvas(
        window,
        bg = "#9FC6A6",
        height = 769,
        width = 750,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("textArea.png"))
    image_1 = canvas.create_image(
        392.0,
        344.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("window2.png"))
    entry_bg_1 = canvas.create_image(
        372.5,
        422.5,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#2A614A",
        highlightthickness=0,
        font = ("Arial", 25)
    )
    entry_1.place(
        x=155.0,
        y=205.00000000000003,
        width=435.0,
        height=433.0
    )

    for x in output_data:
        entry_1.insert("end", f"{x['name']}........{x['DOB']}")
    window.resizable(False, False)

    window.protocol("WM_DELETE_WINDOW",lambda: mixer.music.stop() or window.destroy())
    window.mainloop()

def gen_output_arr():
    date_now = str(date.today())
    date_now_arr = date_now.split("-")
    day_now = int(date_now_arr[2])
    month_now = int(date_now_arr[1])
    year_now = int(date_now_arr[0])
    file_data = open(f"{Path(__file__).parent}//data.txt", "r", encoding="utf-8")
    lines = file_data.readlines()
    for line in lines:
        data_in_line_arr = line.split("_")
        name_in_line = data_in_line_arr[0]
        date_in_line = data_in_line_arr[1]
        date_in_line_arr = date_in_line.split("/")
        day_in_line = int(date_in_line_arr[0])
        month_in_line = int(date_in_line_arr[1])
        year_in_line = int(date_in_line_arr[2])
        if (day_in_line == day_now and month_in_line == month_now):
            output_data.append({
                "name" : name_in_line,
                "DOB": f"{day_in_line}/{month_in_line}/{year_in_line}"
            })
    file_data.close()

def job():
    gen_output_arr()
    if (len(output_data) > 0):
        open_new_window()

job()
schedule.every().day.at("08:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)