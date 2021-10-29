from tkinter import *


def board():
    c_x = 0
    while c_x != width:
        can.create_line(c_x, 0, c_x, height, width=1, fill='black')
        c_x += cell_size
    c_y = 0
    while c_y != height:
        can.create_line(0, c_y, width, c_y, width=1, fill='black')
        c_y += cell_size


def middle_click(event):  # Tue un membre
    x = event.x - (event.x % cell_size)
    y = event.y - (event.y % cell_size)
    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='white')
    cells[x, y] = 0


def left_click(event):  # Ajoute un membre rouge
    x = event.x - (event.x % cell_size)
    y = event.y - (event.y % cell_size)
    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='red')
    cells[x, y] = 1


def right_click(event):  # Ajoute un membre bleu
    x = event.x - (event.x % cell_size)
    y = event.y - (event.y % cell_size)
    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='blue')
    cells[x, y] = 2


def go():
    global flag
    if flag == 0:
        flag = 1
        play()


def stop():
    global flag
    flag = 0


def play():
    global flag, speed
    v = 0
    while v != width / cell_size:
        w = 0
        while w != height / cell_size:
            x = v * cell_size
            y = w * cell_size
            # coins
            if x == 0 and y == 0:  # coin en haut à gauche
                count_red = 0
                count_blue = 0
                if cells[x, y + cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y] == 1:
                    count_red += 1
                if cells[x + cell_size, y + cell_size] == 1:
                    count_red += 1
                if cells[x, y + cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y] == 2:
                    count_blue += 1
                if cells[x + cell_size, y + cell_size] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            elif x == 0 and y == int(height - cell_size):  # coin en bas à gauche
                count_red = 0
                count_blue = 0
                if cells[x, y - cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y - cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y] == 1:
                    count_red += 1
                if cells[x, y - cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y - cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            elif x == int(width - cell_size) and y == 0:  # coin en haut à droite
                count_red = 0
                count_blue = 0
                if cells[x - cell_size, y] == 1:
                    count_red += 1
                if cells[x - cell_size, y + cell_size] == 1:
                    count_red += 1
                if cells[x, y + cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y] == 2:
                    count_blue += 1
                if cells[x - cell_size, y + cell_size] == 2:
                    count_blue += 1
                if cells[x, y + cell_size] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            elif x == int(width - cell_size) and y == int(height - cell_size):  # coin en bas à droite
                count_red = 0
                count_blue = 0
                if cells[x - cell_size, y - cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y] == 1:
                    count_red += 1
                if cells[x, y - cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y - cell_size] == 2:
                    count_blue += 1
                if cells[x - cell_size, y] == 2:
                    count_blue += 1
                if cells[x, y - cell_size] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            # bords
            elif x == 0 and 0 < y < int(height - cell_size):  # bord de gauche
                count_red = 0
                count_blue = 0
                if cells[x, y - cell_size] == 1:
                    count_red += 1
                if cells[x, y + cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y - cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y] == 1:
                    count_red += 1
                if cells[x + cell_size, y + cell_size] == 1:
                    count_red += 1
                if cells[x, y - cell_size] == 2:
                    count_blue += 1
                if cells[x, y + cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y - cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y] == 2:
                    count_blue += 1
                if cells[x + cell_size, y + cell_size] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            elif x == int(width - cell_size) and 0 < y < int(height - cell_size):  # bord de droite
                count_red = 0
                count_blue = 0
                if cells[x - cell_size, y - cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y] == 1:
                    count_red += 1
                if cells[x - cell_size, y + cell_size] == 1:
                    count_red += 1
                if cells[x, y - cell_size] == 1:
                    count_red += 1
                if cells[x, y + cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y - cell_size] == 2:
                    count_blue += 1
                if cells[x - cell_size, y] == 2:
                    count_blue += 1
                if cells[x - cell_size, y + cell_size] == 2:
                    count_blue += 1
                if cells[x, y - cell_size] == 2:
                    count_blue += 1
                if cells[x, y + cell_size] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            elif 0 < x < int(width - cell_size) and y == 0:  # bord du haut
                count_red = 0
                count_blue = 0
                if cells[x - cell_size, y] == 1:
                    count_red += 1
                if cells[x - cell_size, y + cell_size] == 1:
                    count_red += 1
                if cells[x, y + cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y] == 1:
                    count_red += 1
                if cells[x + cell_size, y + cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y] == 2:
                    count_blue += 1
                if cells[x - cell_size, y + cell_size] == 2:
                    count_blue += 1
                if cells[x, y + cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y] == 2:
                    count_blue += 1
                if cells[x + cell_size, y + cell_size] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            elif 0 < x < int(width - cell_size) and y == int(height - cell_size):  # bord du bas
                count_red = 0
                count_blue = 0
                if cells[x - cell_size, y - cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y] == 1:
                    count_red += 1
                if cells[x, y - cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y - cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y] == 1:
                    count_red += 1
                if cells[x - cell_size, y - cell_size] == 2:
                    count_blue += 1
                if cells[x - cell_size, y] == 2:
                    count_blue += 1
                if cells[x, y - cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y - cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            # cellules sans bord
            else:
                count_red = 0
                count_blue = 0
                if cells[x - cell_size, y - cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y] == 1:
                    count_red += 1
                if cells[x - cell_size, y + cell_size] == 1:
                    count_red += 1
                if cells[x, y - cell_size] == 1:
                    count_red += 1
                if cells[x, y + cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y - cell_size] == 1:
                    count_red += 1
                if cells[x + cell_size, y] == 1:
                    count_red += 1
                if cells[x + cell_size, y + cell_size] == 1:
                    count_red += 1
                if cells[x - cell_size, y - cell_size] == 2:
                    count_blue += 1
                if cells[x - cell_size, y] == 2:
                    count_blue += 1
                if cells[x - cell_size, y + cell_size] == 2:
                    count_blue += 1
                if cells[x, y - cell_size] == 2:
                    count_blue += 1
                if cells[x, y + cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y - cell_size] == 2:
                    count_blue += 1
                if cells[x + cell_size, y] == 2:
                    count_blue += 1
                if cells[x + cell_size, y + cell_size] == 2:
                    count_blue += 1
                nb_life[x, y] = {'red': count_red, 'blue': count_blue}
            w += 1
        v += 1
    redraw()
    if flag > 0:
        fen.after(speed, play)


def redraw():
    can.delete(ALL)
    board()
    t = 0
    while t != width / cell_size:
        u = 0
        while u != height / cell_size:
            x = t * cell_size
            y = u * cell_size
            if nb_life[x, y]['red'] + nb_life[x, y]['blue'] == 3:
                if nb_life[x, y]['red'] > nb_life[x, y]['blue']:
                    cells[x, y] = 1
                    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='red')
                elif nb_life[x, y]['red'] < nb_life[x, y]['blue']:
                    cells[x, y] = 2
                    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='blue')
                else:
                    cells[x, y] = 0
                    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='white')
            if nb_life[x, y]['red'] + nb_life[x, y]['blue'] == 2:
                if cells[x, y] == 1 and nb_life[x, y]['red'] == 2:
                    cells[x, y] = 1
                    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='red')
                elif cells[x, y] == 2 and nb_life[x, y]['blue'] == 2:
                    cells[x, y] = 2
                    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='blue')
                else:
                    cells[x, y] = 0
                    can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='white')
            if cells[x, y] == 1 and nb_life[x, y]['red'] < 2 or nb_life[x, y]['red'] > 3:
                cells[x, y] = 0
                can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='white')
            if cells[x, y] == 2 and nb_life[x, y]['blue'] < 2 or nb_life[x, y]['blue'] > 3:
                cells[x, y] = 0
                can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='white')
            if cells[x, y] == 1:
                can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='red')
            if cells[x, y] == 2:
                can.create_rectangle(x, y, x + cell_size, y + cell_size, fill='blue')
            u += 1
        t += 1


height = 500
width = 500
cell_size = 10
speed = 100
flag = 0
nb_life = {}  # Nombre de cellules vivantes autour de chaque cellule
cells = {}  # Coordonnées de chaques cellules et leur état/couleur
i = 0
while i != width / cell_size:
    j = 0
    while j != height / cell_size:
        x = i * cell_size
        y = j * cell_size
        cells[x, y] = 0
        j += 1
    i += 1
fen = Tk()
can = Canvas(fen, width=width, height=height, bg='white')
can.bind("<Button-1>", left_click)
can.bind("<Button-2>", middle_click)
can.bind("<Button-3>", right_click)
can.pack(side=TOP, padx=5, pady=5)
board()
b1 = Button(fen, text='Go!', command=go)
b2 = Button(fen, text='Stop', command=stop)
b1.pack(side=LEFT, padx=3, pady=3)
b2.pack(side=LEFT, padx=3, pady=3)
fen.mainloop()
