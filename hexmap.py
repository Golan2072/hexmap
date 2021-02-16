# Hexagon Map Test.

import stellagama


class World:
    def __init__(self, worldtype, gas_giant, starport, naval, scout):
        self.worldtype = worldtype
        self.gas_giant = gas_giant
        self.starport = starport
        self.naval = naval
        self.scout = scout


def blank_map():
    starmap = {}
    for column in range(0, 9):
        starmap[column] = {}
        for row in range(0, 11):
            starmap[column][row] = World(" ", " ", " ", " ", " ")
    return starmap


def hex_number(column, row, worldtype):
    if column % 2 == 0:
        if (row == 1) or (row == 0):
            return "    "
        elif worldtype == " ":
            return "    "
        elif row == 11:
            return f"0{column}10"
        else:
            return f"0{column}0{row - 1}"
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


def starmap_string(starmap):
    global row
    stellagama.clear_screen()
    star_string = f"HEXACORP NEUROCORE OS v.21.1\n December 21st 2221 11:32AM\n\nS T A R M A P  V I E W\n\n {base_row('  _____       ')}\n"

    for row in range(1, 11):
        star_string += f"  /  {starmap[1][row].starport} {starmap[1][row].gas_giant}\{starmap[2][row - 1].scout} {hex_number(2, row, starmap[2][row - 1].worldtype)} /  {starmap[3][row].starport} {starmap[3][row].gas_giant}\{starmap[4][row - 1].scout} {hex_number(4, row, starmap[4][row - 1].worldtype)} /  {starmap[5][row].starport} {starmap[5][row].gas_giant}\{starmap[6][row - 1].scout} {hex_number(6, row, starmap[6][row - 1].worldtype)} /  {starmap[7][row].starport} {starmap[7][row].gas_giant}\{starmap[8][row - 1].scout} {hex_number(8, row, starmap[8][row - 1].worldtype)} / \n"
        star_string += f" /{starmap[1][row].naval}  {starmap[1][row].worldtype}   \_____/{starmap[3][row].naval}  {starmap[3][row].worldtype}   \_____/{starmap[5][row].naval}  {starmap[5][row].worldtype}   \_____/{starmap[7][row].naval}  {starmap[7][row].worldtype}   \_____/ \n"
        star_string += f" \{starmap[1][row].scout} {hex_number(1, row, starmap[1][row].worldtype)} /  {starmap[2][row].starport} {starmap[2][row].gas_giant}\{starmap[3][row].scout} {hex_number(3, row, starmap[3][row].worldtype)} /  {starmap[4][row].starport} {starmap[4][row].gas_giant}\{starmap[5][row].scout} {hex_number(5, row, starmap[5][row].worldtype)} /  {starmap[6][row].starport} {starmap[6][row].gas_giant}\{starmap[7][row].scout} {hex_number(7, row, starmap[7][row].worldtype)} /  {starmap[8][row].starport} {starmap[8][row].gas_giant}\ \n"
        star_string += f"  \_____/{starmap[2][row].naval}  {starmap[2][row].worldtype}   \_____/{starmap[4][row].naval}  {starmap[4][row].worldtype}   \_____/{starmap[6][row].naval}  {starmap[6][row].worldtype}   \_____/{starmap[8][row].naval}  {starmap[8][row].worldtype}   \ \n"
    star_string += f"        \{starmap[2][10].scout} {hex_number(2, row, starmap[2][row - 1].worldtype)} /     \{starmap[4][10].scout} {hex_number(4, row, starmap[4][row - 1].worldtype)} /     \{starmap[6][10].scout} {hex_number(6, row, starmap[6][row - 1].worldtype)} /     \{starmap[8][10].scout} {hex_number(8, row, starmap[8][row - 1].worldtype)} /\n"
    star_string += f"         \_____/       \_____/       \_____/       \_____/\n\n"
    return star_string


if __name__ == "__main__":
    starmap = blank_map()
    starmap[1][2] = World("@", "*", "A", "*", "^")
    print(starmap_string(starmap))
