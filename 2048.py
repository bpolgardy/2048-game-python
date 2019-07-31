from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
from copy import deepcopy
import sys
import os


def starting_table():
    table = [[0] * 4 for row in range(4)]
    starting_coordinates_1 = starting_coordinates_2 = None
    while starting_coordinates_1 == starting_coordinates_2:
        starting_coordinates_1 = [randint(0, 3), randint(0, 3)]
        starting_coordinates_2 = [randint(0, 3), randint(0, 3)]
    two_or_four = (randint(0, 9), randint(0, 9))  # 90% nr 2, 10% nr 4 inserted
    if two_or_four[0] < 9:
        table[starting_coordinates_1[0]][starting_coordinates_1[1]] = 2
    else:
        table[starting_coordinates_1[0]][starting_coordinates_1[1]] = 4
    if two_or_four[1] < 9:
        table[starting_coordinates_2[0]][starting_coordinates_2[1]] = 2
    else:
        table[starting_coordinates_2[0]][starting_coordinates_2[1]] = 4
    return table


def zero_search(table):
    zero_coordinates = []
    for i in range(len(table)):
        for j, zero in enumerate(table[i]):
            if zero == 0:
                zero_coordinates.append([i, j])
    return zero_coordinates


def status_check(table):
    copy_table = [sorted(row, reverse=True) for row in table]
    WINNING_CONDITION = 32
    if max(max(copy_table)) < WINNING_CONDITION:
        if zero_search(table) != []:
            status = "New round"
        elif addable(table):
            status = "New round"
        else:
            status = "End game"
    else:
        status = "You win"
    return status


def addable(table):
    equals = []
    for i in range(len(table)):
        for j in range(4):
            if i != 3 and j != 3:
                if table[i][j] == table[i][j+1] or table[i][j] == table[i+1][j]:
                    equals.append([i, j])
            if i == 3 and j != 3:
                if table[i][j] == table[i][j+1]:
                    equals.append([i, j])
            if i != 3 and j == 3:
                if table[i][j] == table[i+1][j]:
                    equals.append([i, j])
    return True if equals != [] else False


def remove_zeros(table):
    for nested_list in table:
        while 0 in nested_list:
            nested_list.remove(0)


def slide_right(table):
    remove_zeros(table)
    global score
    for rows in table:
        if len(rows) == 2:
            if rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
                score += rows[-1]
        elif len(rows) == 3:
            if rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
                score += rows[-1]
            elif rows[-2] == rows[-3]:
                rows[-2] += rows[-3]
                del rows[-3]
                score += rows[-2]
        elif len(rows) == 4:
            if rows[-1] == rows[-2] and rows[-3] == rows[-4]:
                rows[-1] += rows[-2]
                rows[-2] = rows[-3] + rows[-4]
                del rows[-4]
                del rows[-3]
                score += rows[-1] + rows[-2]
            elif rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
                score += rows[-1]
            elif rows[-2] == rows[-3]:
                rows[-2] += rows[-3]
                del rows[-3]
                score += rows[-2]
            elif rows[-3] == rows[-4]:
                rows[-3] += rows[-4]
                del rows[-4]
                score += rows[-3]
    for i in range(4):
        while len(table[i]) != 4:
            table[i].insert(0, 0)
    return table


def slide_left(table):
    return reverse_rows(slide_right(reverse_rows(table)))


def transpose(table):
    return [list(row) for row in zip(*table)]

def reverse_rows(table):
    return [list(reversed(row)) for row in table]

def slide_up(table):
    return transpose(slide_left(table))


def slide_down(table):
    return transpose(slide_right(transpose(table)))


def insert_number(table):
    zero_coordinates = zero_search(table)
    if zero_coordinates != []:
        number_of_zeroes = len(zero_coordinates)
        random_index = randint(0, number_of_zeroes-1)
        i_j_coordinates = zero_coordinates[random_index]
        i_coordinate = i_j_coordinates[0]
        j_coordinate = i_j_coordinates[1]
        table[i_coordinate][j_coordinate] = 2
    return table


# GUI functions:

def update_GUI_cells():
    if table[0][0] != 0:
        cell_1.set(table[0][0])
    else:
        cell_1.set('')
    if table[0][1] != 0:
        cell_2.set(table[0][1])
    else:
        cell_2.set('  ')
    if table[0][2] != 0:
        cell_3.set(table[0][2])
    else:
        cell_3.set('  ')
    if table[0][3] != 0:
        cell_4.set(table[0][3])
    else:
        cell_4.set('  ')
    if table[1][0] != 0:
        cell_5.set(table[1][0])
    else:
        cell_5.set('  ')
    if table[1][1] != 0:
        cell_6.set(table[1][1])
    else:
        cell_6.set('  ')
    if table[1][2] != 0:
        cell_7.set(table[1][2])
    else:
        cell_7.set('  ')
    if table[1][3] != 0:
        cell_8.set(table[1][3])
    else:
        cell_8.set('  ')
    if table[2][0] != 0:
        cell_9.set(table[2][0])
    else:
        cell_9.set('  ')
    if table[2][1] != 0:
        cell_10.set(table[2][1])
    else:
        cell_10.set('  ')
    if table[2][2] != 0:
        cell_11.set(table[2][2])
    else:
        cell_11.set('  ')
    if table[2][3] != 0:
        cell_12.set(table[2][3])
    else:
        cell_12.set('  ')
    if table[3][0] != 0:
        cell_13.set(table[3][0])
    else:
        cell_13.set('  ')
    if table[3][1] != 0:
        cell_14.set(table[3][1])
    else:
        cell_14.set('  ')
    if table[3][2] != 0:
        cell_15.set(table[3][2])
    else:
        cell_15.set('  ')
    if table[3][3] != 0:
        cell_16.set(table[3][3])
    else:
        cell_16.set('  ')


def callback(event):

    global table, status

    if status == 'New round':

        prev_table = deepcopy(table)

        if event.keysym == 'Up':
            table = slide_up(table)
        elif event.keysym == 'Down':
            table = slide_down(table)
        elif event.keysym == 'Right':
            table = slide_right(table)
        elif event.keysym == 'Left':
            table = slide_left(table)

        if prev_table != table:
            insert_number(table)

        update_GUI_cells()

        if status_check(table) != "New round":
            status = status_check(table)

            if status == 'You win':
                popupmsg('You win!')
            else:
                popupmsg('You lose!')


def popupmsg(msg):
    popup_root = Tk()
    popup_root.wm_title('2048 message')
    popup_root.resizable(False, False)
    popup_mainframe = Frame(popup_root, bg='#351f36')
    popup_mainframe.grid()
    popup_row_1 = Frame(popup_mainframe)
    popup_row_1.grid(row=0, column=0)
    popup_row_2 = Frame(popup_mainframe, bg='#351f36')
    popup_row_2.grid(row=1, column=0)
    label = ttk.Label(popup_row_1, text=msg, padding=20, background='#351f36', foreground='#ccc497', font=("Arial", 35))
    label.grid()
    B1 = Button(popup_row_2, text='Restart', command=restart_game, bg='#363740', fg='#ccc497', font=("Arial", 15))
    B1.grid(row=0, column=1)
    B2 = Button(popup_row_2, text='Quit', command=combine_funcs(root.destroy, popup_root.destroy), bg='#363740', fg='#ccc497', font=("Arial", 15))
    B2.grid(row=0, column=2)
    popup_root.mainloop()


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def restart_game():
    python = sys.executable
    os.execl(python, python, * sys.argv)


table = starting_table()
status = "New round"
score = 0

# ----------   GUI   ----------


# initialize GUI:

root = Tk()
root.title('2048')
root.resizable(False, False)


# initialize GUI variables:

cell_1 = StringVar()
cell_2 = StringVar()
cell_3 = StringVar()
cell_4 = StringVar()
cell_5 = StringVar()
cell_6 = StringVar()
cell_7 = StringVar()
cell_8 = StringVar()
cell_9 = StringVar()
cell_10 = StringVar()
cell_11 = StringVar()
cell_12 = StringVar()
cell_13 = StringVar()
cell_14 = StringVar()
cell_15 = StringVar()
cell_16 = StringVar()

update_GUI_cells()


# frame styles:

gui_style = ttk.Style()
gui_style.configure('TButton', foreground='#334353')
gui_style.configure('outer.TFrame', background='#363740')
gui_style.configure('cell.TFrame', background='#351f36', relief='raised')
gui_style.configure('TLabel', background='#351f36', foreground='#ccc497', font=("Arial", 35))


# main frame:

mainframe = ttk.Frame(root, width=1500, height=600, padding=10, style='outer.TFrame')
mainframe.grid()


# game board frame inside main frame:

game_board = ttk.Frame(mainframe, width=1200, height=600, relief='raised')
game_board.grid(row=0, column=0)


# game board individual frames:

frame_1 = ttk.Frame(game_board, style='cell.TFrame')
frame_1.grid(row=0, column=0)
frame_1.configure(height=100, width=100, padding=50)

frame_2 = ttk.Frame(game_board, style='cell.TFrame')
frame_2.grid(row=0, column=1)
frame_2.configure(height=100, width=100, padding=50)

frame_3 = ttk.Frame(game_board, style='cell.TFrame')
frame_3.grid(row=0, column=2)
frame_3.configure(height=100, width=100, padding=50)

frame_4 = ttk.Frame(game_board, style='cell.TFrame')
frame_4.grid(row=0, column=3)
frame_4.configure(height=100, width=100, padding=50)

frame_5 = ttk.Frame(game_board, style='cell.TFrame')
frame_5.grid(row=1, column=0)
frame_5.configure(height=100, width=100, padding=50)

frame_6 = ttk.Frame(game_board, style='cell.TFrame')
frame_6.grid(row=1, column=1)
frame_6.configure(height=100, width=100, padding=50)

frame_7 = ttk.Frame(game_board, style='cell.TFrame')
frame_7.grid(row=1, column=2)
frame_7.configure(height=100, width=100, padding=50)

frame_8 = ttk.Frame(game_board, style='cell.TFrame')
frame_8.grid(row=1, column=3)
frame_8.configure(height=100, width=100, padding=50)

frame_9 = ttk.Frame(game_board, style='cell.TFrame')
frame_9.grid(row=2, column=0)
frame_9.configure(height=100, width=100, padding=50)

frame_10 = ttk.Frame(game_board, style='cell.TFrame')
frame_10.grid(row=2, column=1)
frame_10.configure(height=100, width=100, padding=50)

frame_11 = ttk.Frame(game_board, style='cell.TFrame')
frame_11.grid(row=2, column=2)
frame_11.configure(height=100, width=100, padding=50)

frame_12 = ttk.Frame(game_board, style='cell.TFrame')
frame_12.grid(row=2, column=3)
frame_12.configure(height=100, width=100, padding=50)

frame_13 = ttk.Frame(game_board, style='cell.TFrame')
frame_13.grid(row=3, column=0)
frame_13.configure(height=100, width=100, padding=50)

frame_14 = ttk.Frame(game_board, style='cell.TFrame')
frame_14.grid(row=3, column=1)
frame_14.configure(height=100, width=100, padding=50)

frame_15 = ttk.Frame(game_board, style='cell.TFrame')
frame_15.grid(row=3, column=2)
frame_15.configure(height=100, width=100, padding=50)

frame_16 = ttk.Frame(game_board, style='cell.TFrame')
frame_16.grid(row=3, column=3)
frame_16.configure(height=100, width=100, padding=50)


# labels for frames on game board:

label_frame_1 = ttk.Label(frame_1, textvariable=cell_1, style='TLabel')
label_frame_1.place(anchor="center")

label_frame_2 = ttk.Label(frame_2, textvariable=cell_2, style='TLabel')
label_frame_2.place(anchor="center")

label_frame_3 = ttk.Label(frame_3, textvariable=cell_3, style='TLabel')
label_frame_3.place(anchor="center")

label_frame_4 = ttk.Label(frame_4, textvariable=cell_4, style='TLabel')
label_frame_4.place(anchor="center")

label_frame_5 = ttk.Label(frame_5, textvariable=cell_5, style='TLabel')
label_frame_5.place(anchor="center")

label_frame_6 = ttk.Label(frame_6, textvariable=cell_6, style='TLabel')
label_frame_6.place(anchor="center")

label_frame_7 = ttk.Label(frame_7, textvariable=cell_7, style='TLabel')
label_frame_7.place(anchor="center")

label_frame_8 = ttk.Label(frame_8, textvariable=cell_8, style='TLabel')
label_frame_8.place(anchor="center")

label_frame_9 = ttk.Label(frame_9, textvariable=cell_9, style='TLabel')
label_frame_9.place(anchor="center")

label_frame_10 = ttk.Label(frame_10, textvariable=cell_10, style='TLabel')
label_frame_10.place(anchor="center")

label_frame_11 = ttk.Label(frame_11, textvariable=cell_11, style='TLabel')
label_frame_11.place(anchor="center")

label_frame_12 = ttk.Label(frame_12, textvariable=cell_12, style='TLabel')
label_frame_12.place(anchor="center")

label_frame_13 = ttk.Label(frame_13, textvariable=cell_13, style='TLabel')
label_frame_13.place(anchor="center")

label_frame_14 = ttk.Label(frame_14, textvariable=cell_14, style='TLabel')
label_frame_14.place(anchor="center")

label_frame_15 = ttk.Label(frame_15, textvariable=cell_15, style='TLabel')
label_frame_15.place(anchor="center")

label_frame_16 = ttk.Label(frame_16, textvariable=cell_16, style='TLabel')
label_frame_16.place(anchor="center")

# event handling:

root.bind('<Key>', callback)

# mainloop:

root.mainloop()
