# Hexagon Map Test.

import stellagama


class World:
    def __init__(self, worldtype, gas_giant, starport, naval, scout):
        self.worldtype = worldtype
        self.gas_giant = gas_giant
        self.starport = starport
        self.naval = naval
        self.scout = scout


# Placeholder Test Sector Data


starmap = {0: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0},
           1: {1: World("O", "*", "A", "*", "^"), 2: World("@", " ", "C", "*", "^"),
               3: World(" ", " ", " ", " ", " "), 4: World("O", "*", "D", " ", " "),
               5: World("@", " ", "B", " ", " "), 6: World("O", " ", "B", " ", " "),
               7: World("O", " ", "C", " ", " "), 8: World("O", "*", "E", " ", " "),
               9: World("O", " ", "C", " ", " "), 10: World(" ", " ", " ", " ", " ")},
           2: {1: World("O", " ", " ", " ", "^"), 2: World(" ", " ", " ", " ", " "),
               3: World(" ", " ", " ", " ", " "), 4: World("@", "*", "D", " ", " "),
               5: World("@", " ", "E", " ", " "), 6: World("O", " ", "B", " ", " "),
               7: World("O", " ", "C", " ", " "), 8: World("O", "*", "C", " ", " "),
               9: World(" ", " ", " ", " ", " "), 10: World("O", " ", "C", " ", " ")},
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


def hex_number(column, row, worldtype):
    if column % 2 == 0:
        if row == 1 or 0:
            return "    "
        elif worldtype == " ":
            return "    "
        elif row == 10:
            return f"0{column}10"
        else:
            return f"0{column}0{row-1}"
    else:
        if worldtype == " ":
            return "    "
        elif row == 10:
            return f"0{column}10"
        else:
            return f"0{column}0{row}"


def base_row(base_row_string):
    row_string = ""
    for i in range(0, 4):
        row_string += base_row_string
    return row_string


def even_row(column, row):
    if column % 2 == 0:
        if row == 1:
            return 1
        else:
            return row - 1
    else:
        return row


stellagama.clear_screen()
print(" HEXACORP NEUROCORE OS v.21.1\nDecember 21st 2221 11:32AM")
print("")
print(" S T A R M A P  V I E W")
print("")

print(base_row("   _____      "))
for row in range(1, 11):
    print(
        f"  /  {starmap[1][row].starport} {starmap[1][row].gas_giant}\{starmap[2][even_row(2, row)].scout} {hex_number(2, even_row(2, row), starmap[2][even_row(2, row)].worldtype)} /  {starmap[3][row].starport} {starmap[3][row].gas_giant}\{starmap[4][even_row(4, row)].scout} {hex_number(4, even_row(4, row), starmap[4][even_row(4, row)].worldtype)} /  {starmap[5][row].starport} {starmap[5][row].gas_giant}\{starmap[6][even_row(6, row)].scout} {hex_number(6, row, starmap[6][even_row(6, row)].worldtype)} /  {starmap[7][row].starport} {starmap[7][row].gas_giant}\{starmap[8][even_row(8, row)].scout} {hex_number(8, even_row(8, row), starmap[8][even_row(8, row)].worldtype)} / ")
    print(
        f" /{starmap[1][row].naval}  {starmap[1][row].worldtype}   \_____/{starmap[3][row].naval}  {starmap[3][row].worldtype}   \_____/{starmap[5][row].naval}  {starmap[5][row].worldtype}   \_____/{starmap[7][row].naval}  {starmap[7][row].worldtype}   \_____/ ")
    print(
        f" \{starmap[1][row].scout} {hex_number(1, row, starmap[1][row].worldtype)} /  {starmap[2][even_row(2, row)].starport} {starmap[2][even_row(2, row)].gas_giant}\{starmap[3][row].scout} {hex_number(3, row, starmap[3][row].worldtype)} /  {starmap[4][even_row(4, row)].starport} {starmap[4][even_row(4, row)].gas_giant}\{starmap[5][row].scout} {hex_number(5, row, starmap[5][row].worldtype)} /  {starmap[6][even_row(6, row)].starport} {starmap[6][even_row(6, row)].gas_giant}\{starmap[7][row].scout} {hex_number(7, row, starmap[7][row].worldtype)} /  {starmap[8][even_row(8, row)].starport} {starmap[8][even_row(8, row)].gas_giant}\ ")
    print(
        f"  \_____/{starmap[2][even_row(2, row)].naval}  {starmap[2][even_row(2, row)].worldtype}   \_____/{starmap[4][even_row(4, row)].naval}  {starmap[4][even_row(4, row)].worldtype}   \_____/{starmap[6][even_row(6, row)].naval}  {starmap[6][even_row(6, row)].worldtype}   \_____/{starmap[8][even_row(8, row)].naval}  {starmap[8][even_row(8, row)].worldtype}   \ ")
print(
    f"        \{starmap[2][10].scout} 0210 /     \{starmap[4][10].scout} 0410 /     \{starmap[6][10].scout} 0610 /     \{starmap[8][10].scout} 0810 /")
print(f"         \_____/       \_____/       \_____/       \_____/")
print("")

