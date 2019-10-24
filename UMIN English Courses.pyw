from tkinter import *
from tkinter import scrolledtext
import datetime
import time as time_module


def get_number():
    f = open(r"dates with numbers of lessons fixed.txt", "r")
    date = str(datetime.date.today())
    number_local = ''
    for line in f:
        if date in line:
            arr = line.split(' ')
            number_local = arr[1]
            break
    number.delete('1.0', END)
    number.insert(1.0, number_local)


def start_program():
    i = int(number.get(1.0, END))
    if i == 1:
        main_text.insert(INSERT, "\n    А,Б,В,Г,Д,Е,Ж - Л1")
    elif i == 2:
        main_text.insert(INSERT, ("\n    П1:\n    А – (Л1, Л2 – 2-3);\n"
                                  "    Б – (Л1 – 3-5)"))
    elif i == 3:
        main_text.insert(INSERT, ("\n    П2:\n    А – (Л1, Л2, Л3, Л4 – 2-3)\n"
                                  "    П1:\n    Б – (Л1, Л2 – 2-3);\n"
                                  "    В – (Л1 – 3-5)"))
    elif i in range(4, 10 + 1):
        main_text.insert(INSERT, p4(i))
    elif i in range(11, 21 + 1):
        main_text.insert(INSERT, p5(i))
        main_text.insert(INSERT, p4(i))
    elif i == 22:
        main_text.insert(INSERT, ("\n    С1\n"
                                  "    01А – Л5\n"
                                  "    02Б – Л5\n"
                                  "    …\n"
                                  "    21Х – Л5"))
    elif i == 23:
        main_text.insert(INSERT, ("\n    С1\n"
                                  "    Sounds – Л1\n"
                                  "    Sounds – Л2\n"
                                  "    Sounds – Л6:2\n"))
    elif i == 24:
        main_text.insert(INSERT,"\n    Sounds – Л6:3\n")
        main_text.insert(INSERT, p5(i-2))
        main_text.insert(INSERT, p4(i-2))

    elif i == 25:
        main_text.insert(INSERT, p5(i - 2))
        main_text.insert(INSERT, p4(i - 2))
        main_text.insert(INSERT, ("\n    The hardest one - Л10\n"
                                  "    С1\n"
                                  "    The hardesе one - Л10(fix errors in pronouns)\n"))
    elif i == 26:
        main_text.insert(INSERT, p5(i - 2))
        main_text.insert(INSERT, p4(i - 2))
        main_text.insert(INSERT, "    The hardest one – Л10:2\n")
        main_text.insert(INSERT, "    The hardest one – Л11\n")
    elif i == 27:
        main_text.insert(INSERT, p5(i - 2))
        main_text.insert(INSERT, p4(i - 2))
        main_text.insert(INSERT, "    The hardest one – Л11:3\n")
    elif i in range(28,35+1):
        main_text.insert(INSERT, p5(i - 2))
        main_text.insert(INSERT, p4(i - 2))
        main_text.insert(INSERT, "\n    Л12\n")


def clear():
    main_text.delete('1.0', END)


def get_time():
    time.delete('1.0', END)
    time.insert(INSERT, time_module.strftime("%H.%M.%S", time_module.localtime()))


def p4(number_of_lesson):
    pattern = """
    П4
    {}{} – (Л2, Л4 – 1-3, Л5);
    {}{} – (Л1, Л2, Л3, Л4 – 2-3);
    {}{} – (Л1,  Л2 – 2-3);
    {}{} – (Л1 – 3-5)"""
    alphabet = ab = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    # 11 занятие === 'З'(7 в списке с 0)
    n = number_of_lesson
    nfl = (n-4)%len(ab)
    return pattern.format(n-3, ab[nfl], n-2, ab[nfl + 1], n-1,  ab[nfl + 2], n, ab[nfl + 3])


def p5(number_of_lesson):
    pattern = ("\n"
               "    П5\n"
               "    {} – (Л7, Л8 – 2-3, Л9)\n"
               "    {} – (Л6 – 1-2, Л7 – 2-3)\n"
               "    {} – (Л2, Л5, Л6 – 3-5)")
    alphabet = ab = "А1А2Б1Б2В1В2Г1Г2Д1Д2Е1Е2Ж1Ж2З1З2И1И2К1К2Л1Л2М1М2Н1Н2О1О2П1П2Р1Р2С1С2Т1Т2У1У2Ф1Ф2Х1Х2Ц1Ц2Ч1Ч2Ш1Ш2Щ1Щ2Ъ1Ъ2Ы1Ы2Ь1Ь2Э1Э2Ю1Ю2Я1Я2"
    # 11 занятие === 'A'(0 в списке с 0)
    i = number_of_lesson - 11
    nfl = 2 * i
    return pattern.format(ab[nfl:nfl + 2], ab[nfl + 2:nfl + 4], ab[nfl + 4:nfl + 6])


window = Tk()
window.title("UMIN English Courses")
window.geometry('745x330')
lbl_number = Label(window, text="Number of lesson", font=("Arial Bold", 12))
lbl_date = Label(window, text="Date", font=("Arial Bold", 12))
number = Text(window, height=1, width=5, font='Arial 14', wrap=WORD)
time = Text(window, height=1, width=8, font='Arial 14', wrap=WORD)
date = Text(window, height=1, width=10, font='Arial 14', wrap=WORD)
main_text = scrolledtext.ScrolledText(window, width=60, height=20)
btn_time = Button(window, text="Start time?", command=get_time)
btn_get = Button(window, text="Start program", command=start_program)
btn_number = Button(window, text="Get number", command=get_number)
btn_clear = Button(window, text="Clear", command=clear)
# ----------------------------------------
main_text.grid(column=0, row=0, rowspan=5)
lbl_date.grid(column=1, row=0)
date.grid(column=2, row=0)

lbl_number.grid(column=1, row=1)
number.grid(column=2, row=1)

btn_number.grid(column=1, row=2)

btn_get.grid(column=1, row=3)
time.grid(column=2, row=3)

btn_time.grid(column=2, row=4)
btn_clear.grid(column=1, row=4)
# ----------------------------------------
date.insert(1.0, str(datetime.date.today()))
window.iconbitmap('py.ico')

window.mainloop()
