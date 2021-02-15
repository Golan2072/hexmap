# Hexagon Map Test.

import sys
from termcolor import colored, cprint


class World:
    def __init__(self, worldtype, gas_giant, starport, naval, scout):
        self.worldtype = worldtype
        self.gas_giant = gas_giant
        self.starport = starport
        self.naval = naval
        self.scout = scout


# Placeholder Test Sector Data


starmap = {1: {1: World("O", "*", "A", "*", "^"), 2: World("@", " ", "C", "*", "^"),
               3: World(" ", " ", " ", " ", " "), 4: World("O", "*", "D", " ", " "),
               5: World("@", " ", "B", " ", " "), 6: World("O", " ", "B", " ", " "),
               7: World("O", " ", "C", " ", " "), 8: World("O", "*", "E", " ", " "),
               9: World("O", " ", "C", " ", " "), 10: World(" ", " ", " ", " ", " ")},
           2: {1: World(" ", " ", " ", " ", " "), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", "@", " ", " ", " "), 4: World("O", "*", "D", " ", " "),
               5: World("@", " ", "E", " ", " "), 6: World("O", " ", "B", " ", " "),
               7: World("O", " ", "C", " ", " "), 8: World("O", "*", "C", " ", " "),
               9: World(" ", " ", " ", " ", " "), 10: World("@", " ", "C", " ", " ")},
           2: {1: World("O", " ", "B", " ", " "), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", "@", " ", " ", " "), 4: World(" ", " ", " ", " ", " "),
               5: World(" ", " ", " ", " ", " "), 6: World(" ", " ", " ", " ", " "),
               7: World("O", " ", " ", " ", " "), 8: World("O", "*", "C", " ", " "),
               9: World("@", "*", "C", " ", " "), 10: World("O", " ", "D", " ", " ")},
           3: {1: World("@", " ", "C", " ", " "), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", " ", " ", " ", " "), 4: World(" ", " ", " ", " ", " "),
               5: World("@", " ", "E", " ", " "), 6: World("O", " ", "B", " ", " "),
               7: World("O", " ", "C", " ", " "), 8: World("O", "*", "C", " ", " "),
               9: World("@", "*", "C", " ", " "), 10: World("O", " ", "E", " ", " ")},
           4: {1: World("@", "*", "D", " ", " "), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", " ", " ", " ", " "), 4: World("@", "*", "A", "*", "^"),
               5: World("@", " ", "E", " ", " "), 6: World(" ", " ", " ", " ", " "),
               7: World("O", " ", "C", " ", " "), 8: World(" ", "*", " ", " ", " "),
               9: World("O", "*", "E", " ", " "), 10: World("@", " ", "A", "*", " ")},
           5: {1: World("@", " ", "E", " ", " "), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", "@", " ", " ", " "), 4: World("@", "*", "A", "*", "^"),
               5: World("@", " ", "E", " ", " "), 6: World(" ", " ", " ", " ", " "),
               7: World("O", " ", "C", " ", " "), 8: World(" ", "*", " ", " ", " "),
               9: World("O", "*", "E", " ", " "), 10: World("@", " ", "B", "*", " ")},
           6: {1: World("@", " ", "A", " ", " "), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", " ", " ", " ", " "), 4: World("@", "*", "C", "*", "^"),
               5: World("@", " ", "E", " ", " "), 6: World(" ", " ", " ", " ", " "),
               7: World(" ", " ", " ", " ", " "), 8: World(" ", "*", " ", " ", " "),
               9: World("O", "*", "D", " ", " "), 10: World("@", " ", "E", "*", " ")
               },
           7: {1: World(" ", " ", " ", " ", " "), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", " ", " ", " ", " "), 4: World("@", "*", "D", "*", "^"),
               5: World(" ", " ", " ", " ", " "), 6: World(" ", " ", " ", " ", " "),
               7: World(" ", " ", " ", " ", " "), 8: World(" ", " ", " ", " ", " "),
               9: World("O", "*", "E", " ", " "), 10: World(" ", " ", " ", " ", " ")
               },
           8: {1: World(" ", " ", " ", " ", " "), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", " ", " ", " ", " "), 4: World("@", "*", "C", "*", "^"),
               5: World(" ", " ", " ", " ", " "), 6: World(" ", " ", " ", " ", " "),
               7: World(" ", " ", " ", " ", " "), 8: World("O", *"D", " ", " ", " "),
               9: World("@", "*", "C", " ", " "), 10: World("O", " ", "D", " ", " "),
               }
}


def column_check(row, column):
    if row == 1:
        if column % 2 == 0:
            return " "
    else:
        return column


def row_check(row):
    if row == 0:
        return " "
    if row == 10:
        return 0
    else:
        return row


def base_row(base_row_string):
    row_string = ""
    for i in range(0, 4):
        row_string += base_row_string
    return row_string


cprint(base_row("  ____     "), 'green')

for row in range (1, 11):
    cprint(
        f" /  {starmap[1][row].starport}{starmap[1][row].gas_giant}\ {column_check(row, 2)} {row_check(row)-1} /  {starmap[3][row].starport}{starmap[3][row].gas_giant}\     /  {starmap[5][row].starport}{starmap[5][row].gas_giant}\     /  {starmap[7][row].starport}{starmap[7][1].gas_giant}\     /", 'green')
    cprint(
        f"({starmap[1][row].naval}  {starmap[1][row].worldtype}  )___(   {starmap[3][row].worldtype}  )___(   {starmap[5][row].worldtype}  )___(   {starmap[7][row].worldtype}  )___(", 'green')
    cprint(
        f" \{starmap[1][row].scout}1 {row_check(row)}/  {starmap[2][row].starport} {starmap[2][row].gas_giant}\ 3 {row_check(row)}/  {starmap[4][row].starport} {starmap[4][row].gas_giant}\ 5 {row_check(row)}/  {starmap[6][row].starport} {starmap[6][row].gas_giant}\ 7 {row_check(row)}/  {starmap[8][row].starport} {starmap[8][row].gas_giant}\ ", 'green')
    cprint(
        f"  ----{starmap[2][row].naval}  {starmap[4][row].worldtype}   ----   {starmap[6][row].worldtype}   ----       ----       )", 'green')
