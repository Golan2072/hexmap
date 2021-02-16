# Hexagon Map Test.

import stellagama


class World:
    def __init__(self, worldtype, gas_giant, starport, naval, scout, names):
        self.worldtype = worldtype
        self.gas_giant = gas_giant
        self.starport = starport
        self.naval = naval
        self.scout = scout
        self.names = names.upper()


def blank_map():
    starmap = {}
    for column in range(0, 9):
        starmap[column] = {}
        for row in range(0, 11):
            starmap[column][row] = World(" ", " ", " ", " ", "_", "       ")
    return starmap


def hex_number(column, row, worldtype):
    if column % 2 == 0:
        if (row == 1) or (row == 0):
            return "____"
        elif worldtype == " ":
            return "____"
        elif row == 11:
            return f"0{column}10"
        else:
            return f"0{column}0{row - 1}"
    else:
        if worldtype == " ":
            return "____"
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
    star_string = f"HEXACORP NEUROCORE OS v.21.1\nDecember 21st 2221 11:32AM\n\nS T A R M A P  V I E W\n\n {base_row('  _____       ')}\n"

    for row in range(1, 11):
        star_string += f"  /  {starmap[1][row].starport} {starmap[1][row].gas_giant}\{starmap[2][row-1].names}/  {starmap[3][row].starport} {starmap[3][row].gas_giant}\{starmap[4][row-1].names}/  {starmap[5][row].starport} {starmap[5][row].gas_giant}\{starmap[6][row-1].names}/  {starmap[7][row].starport} {starmap[7][row] .gas_giant}\{starmap[8][row-1].names}/ \n"
        star_string += f" /{starmap[1][row].naval}  {starmap[1][row].worldtype}   \{starmap[2][row - 1].scout}{hex_number(2, row, starmap[2][row - 1].worldtype)}/{starmap[3][row].naval}  {starmap[3][row].worldtype}   \{starmap[4][row - 1].scout}{hex_number(4, row, starmap[4][row - 1].worldtype)}/{starmap[5][row].naval}  {starmap[5][row].worldtype}   \{starmap[6][row - 1].scout}{hex_number(6, row, starmap[6][row - 1].worldtype)}/{starmap[7][row].naval}  {starmap[7][row].worldtype}   \{starmap[8][row - 1].scout}{hex_number(8, row, starmap[8][row - 1].worldtype)}/ \n"
        star_string += f" \{starmap[1][row].names}/  {starmap[2][row].starport} {starmap[2][row].gas_giant}\{starmap[3][row].names}/  {starmap[4][row].starport} {starmap[4][row].gas_giant}\{starmap[5][row].names}/  {starmap[6][row].starport} {starmap[6][row].gas_giant}\{starmap[7][row].names}/  {starmap[8][row].starport} {starmap[8][row].gas_giant}\ \n"
        star_string += f"  \{starmap[1][row].scout}{hex_number(1, row, starmap[1][row].worldtype)}/{starmap[2][row].naval}  {starmap[2][row].worldtype}   \{starmap[3][row].scout}{hex_number(3, row, starmap[3][row].worldtype)}/{starmap[4][row].naval}  {starmap[4][row].worldtype}   \{starmap[5][row].scout}{hex_number(5, row, starmap[5][row].worldtype)}/{starmap[6][row].naval}  {starmap[6][row].worldtype}   \{starmap[7][row].scout}{hex_number(7, row, starmap[7][row].worldtype)}/{starmap[8][row].naval}  {starmap[8][row].worldtype}   \ \n"
    star_string += f"        \{starmap[2][10].names}/     \{starmap[4][10].names}/     \{starmap[6][10].names}/     \{starmap[8][10].names}/\n"
    star_string += f"         \{starmap[2][10].scout}{hex_number(2, 11, starmap[2][row].worldtype)}/       \{starmap[4][10].scout}{hex_number(4, 11, starmap[4][10].worldtype)}/       \{starmap[6][10].scout}{hex_number(6, 11, starmap[6][10].worldtype)}/       \{starmap[8][10].scout}{hex_number(8, 11, starmap[8][10].worldtype)}/\n\n"
    return star_string


if __name__ == "__main__":
    starmap = blank_map()
    starmap[1][1] = World("O", "*", "E", " ", "^", "Solstic")
    starmap[1][4] = World("@", " ", "B", "*", "_", "Helena ")
    starmap[1][5] = World("@", "*", "B", " ", "_", "Persepo")
    starmap[1][6] = World("@", "*", "C", " ", "_", "Tanith ")
    starmap[1][10] = World("@", " ", "D", " ", "^", "Armaged")
    starmap[2][3] = World("@", "*", "C", " ", "_", "Solomon")
    starmap[2][5] = World("O", "*", "C", " ", "^", "Cyclops")
    starmap[2][8] = World("O", "*", "D", " ", "_", "Retribu")
    starmap[2][9] = World("@", "*", "B", " ", "_", "Priam  ")
    starmap[2][10] = World("@", "*", "E", " ", "_", "Morrow ")
    starmap[3][5] = World("O", "*", "E", " ", "_", "Labyrin")
    starmap[3][6] = World("@", "*", "A", "*", "_", "Orpheus")
    starmap[3][8] = World("@", "*", "C", " ", "_", "Lucifer")
    starmap[3][9] = World("@", "*", "E", " ", "_", "Theta T")
    starmap[4][1] = World("@", " ", "C", "%", "_", "Lantau ")
    starmap[4][4] = World("O", "*", "E", " ", "_", "Monumen")
    starmap[4][4] = World("@", "*", "B", " ", "_", "Centenn")
    starmap[5][2] = World("@", "*", "E", " ", "_", "Paradis")
    starmap[5][4] = World("@", " ", "C", " ", "_", "Midas  ")
    starmap[5][8] = World("O", " ", "X", " ", "_", "LV 508 ")
    starmap[6][1] = World("O", "*", "D", " ", "_", "Ha Long")
    starmap[6][2] = World("@", "*", "C", "*", "^", "Hexis  ")
    starmap[6][4] = World("@", "*", "X", " ", "_", "LV 604 ")
    starmap[6][6] = World("@", " ", "E", " ", "_", "Gamma T")
    starmap[6][8] = World("#", "*", "C", " ", "_", "Telamon")
    starmap[6][10] = World("@", " ", "X", " ", "_", "LV 610 ")
    starmap[7][2] = World("#", " ", "B", " ", "_", "Diomede")
    starmap[7][3] = World("O", "*", "D", " ", "_", "Sterlin")
    starmap[7][4] = World("@", "*", "E", " ", "_", "Delta T")
    starmap[7][7] = World("O", "*", "X", " ", "_", "LV 707 ")
    starmap[7][9] = World("O", "*", "D", " ", "_", "Forge  ")
    starmap[7][10] = World("@", "*", "E", " ", "_", "Absolom")
    starmap[8][5] = World("O", " ", "E", " ", "_", "Nemesis")
    starmap[8][10] = World("@", "*", "X", " ", "_", "LV 810 ")

    with open('1977.txt', 'w') as text_starmap:
        text_starmap.write(starmap_string(starmap))
    print("file saved")
