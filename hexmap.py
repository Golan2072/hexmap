# Cepheus Light Retro Hexagon Map Generator.

import stellagama
import json
import sys


class World:
    def __init__(self, worldtype, gas_giant, starport, naval, scout, names):
        self.worldtype = worldtype
        self.gas_giant = gas_giant
        self.starport = starport
        self.naval = naval
        self.scout = scout
        self.names = names


def name_converter(name):
    new_name = f"{name: <{7}}".upper()
    new_name = (new_name[:7]) if len(new_name) > 7 else new_name
    return new_name


def read_json_subsector(jsonfile):
    starmap = blank_map()
    with open(jsonfile, 'r') as subsector:
        data = json.load(subsector)
        for column in data:
            for row in data[column]:
                if row in data[column]:
                    if data[column][row]["hydrographics"] > 0:
                        world_type = "@"
                    elif data[column][row]["size"] == 0:
                        world_type = "#"
                    else:
                        world_type = "O"
                    if data[column][row]["gas_giants"] == "G":
                        gas_giant = "*"
                    else:
                        gas_giant = " "
                    if data[column][row]["base"] == "N":
                        naval_base = "*"
                    else:
                        naval_base = " "
                    if data[column][row]["base"] == "S":
                        scout_base = "^"
                    else:
                        scout_base = "_"
                    starmap[int(column)][int(row)] = World(world_type, gas_giant, data[column][row]["starport"],
                                                           naval_base, scout_base,
                                                           name_converter(data[column][row]["name"]))
                else:
                    starmap[int(column)][int(row)] = World(" ", " ", " ", " ", "_", "       ")
    for column in starmap:
        for row in starmap[column]:
            if row not in starmap[column]:
                starmap[column][row] = World(" ", " ", " ", " ", "_", "       ")
    return starmap


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


def starmap_string(starmap):
    global row
    # stellagama.clear_screen()
    star_string = f" UNIVERSAL OS v.21.1\n\n A U T O N O M O U S    R E G I O N\n\n {base_row('  _____       ')}\n"

    for row in range(1, 11):
        star_string += f"  /  {starmap[1][row].starport} {starmap[1][row].gas_giant}\{starmap[2][row - 1].names}/  {starmap[3][row].starport} {starmap[3][row].gas_giant}\{starmap[4][row - 1].names}/  {starmap[5][row].starport} {starmap[5][row].gas_giant}\{starmap[6][row - 1].names}/  {starmap[7][row].starport} {starmap[7][row].gas_giant}\{starmap[8][row - 1].names}/ \n"
        star_string += f" /{starmap[1][row].naval}  {starmap[1][row].worldtype}   \{starmap[2][row - 1].scout}{hex_number(2, row, starmap[2][row - 1].worldtype)}/{starmap[3][row].naval}  {starmap[3][row].worldtype}   \{starmap[4][row - 1].scout}{hex_number(4, row, starmap[4][row - 1].worldtype)}/{starmap[5][row].naval}  {starmap[5][row].worldtype}   \{starmap[6][row - 1].scout}{hex_number(6, row, starmap[6][row - 1].worldtype)}/{starmap[7][row].naval}  {starmap[7][row].worldtype}   \{starmap[8][row - 1].scout}{hex_number(8, row, starmap[8][row - 1].worldtype)}/ \n"
        star_string += f" \{starmap[1][row].names}/  {starmap[2][row].starport} {starmap[2][row].gas_giant}\{starmap[3][row].names}/  {starmap[4][row].starport} {starmap[4][row].gas_giant}\{starmap[5][row].names}/  {starmap[6][row].starport} {starmap[6][row].gas_giant}\{starmap[7][row].names}/  {starmap[8][row].starport} {starmap[8][row].gas_giant}\ \n"
        star_string += f"  \{starmap[1][row].scout}{hex_number(1, row, starmap[1][row].worldtype)}/{starmap[2][row].naval}  {starmap[2][row].worldtype}   \{starmap[3][row].scout}{hex_number(3, row, starmap[3][row].worldtype)}/{starmap[4][row].naval}  {starmap[4][row].worldtype}   \{starmap[5][row].scout}{hex_number(5, row, starmap[5][row].worldtype)}/{starmap[6][row].naval}  {starmap[6][row].worldtype}   \{starmap[7][row].scout}{hex_number(7, row, starmap[7][row].worldtype)}/{starmap[8][row].naval}  {starmap[8][row].worldtype}   \ \n"
    star_string += f"        \{starmap[2][10].names}/     \{starmap[4][10].names}/     \{starmap[6][10].names}/     \{starmap[8][10].names}/\n"
    star_string += f"         \{starmap[2][10].scout}{hex_number(2, 11, starmap[2][row].worldtype)}/       \{starmap[4][10].scout}{hex_number(4, 11, starmap[4][10].worldtype)}/       \{starmap[6][10].scout}{hex_number(6, 11, starmap[6][10].worldtype)}/       \{starmap[8][10].scout}{hex_number(8, 11, starmap[8][10].worldtype)}/\n\n"
    return star_string


def starmap_string_v2(starmap):
    global row
    # stellagama.clear_screen()
    star_string = f" UNIVERSAL OS v.21.1\n\n A U T O N O M O U S    R E G I O N\n\n {base_row('  _____       ')}\n"
    
    # Convert starmap to preliminary format.
    # Format is a 3d array, Row, Column, Line
    printmap = [[[] for i in range(8)] for j in range(10)]
    
    for row in range(1,11):
        for column in range(1,9):
            printmap[row][column][1] = f"  {starmap[column][row].starport} {starmap[column][row].gas_giant}"
            printmap[row][column][2] = f"{starmap[column][row].naval}  {starmap[column][row].worldtype}   "
            printmap[row][column][3] = f"{starmap[column][row].names}"
            printmap[row][column][4] = f"{starmap[column][row].scout}{hex_number(column, row, starmap[column][row].worldtype)}"
    

    # Each cell has 4 lines with 5,7,7,5 cells.
    for row in range(1, 11):
        star_string += f"  /{printmap[row][1][1]}\{printmap[row-1][2][3]}/{printmap[row][3][1]}\{printmap[row-1][4][3]}/{printmap[row][5][1]}\{printmap[row-1][6][3]}/{printmap[row][7][1]}\{printmap[row-1][8][3]}/ \n"
        star_string += f" /{printmap[row][1][2]}\{printmap[row-1][2][4]}/{printmap[row][3][2]}\{printmap[row-1][4][4]}/{printmap[row][5][2]}\{printmap[row-1][6][4]}/{printmap[row][7][2]}\{printmap[row-1][8][4]}/ \n"
        star_string += f" \{printmap[row][1][3]}/{printmap[row][2][1]}\{printmap[row][3][3]}/{printmap[row][4][1]}\{printmap[row][5][3]}/{printmap[row][6][1]}\{printmap[row][7][3]}/{printmap[row][8][1]}\ \n"
        star_string += f"  \{printmap[row][1][4]}/{printmap[row][2][2]}\{printmap[row][3][4]}/{printmap[row][4][2]}\{printmap[row][5][4]}/{printmap[row][6][2]}\{printmap[row][7][4]}/{printmap[row][8][2]}\ \n"
    star_string += f"        \{printmap[row][2][3]}/     \{printmap[row][4][3]}/     \{printmap[row][6][3]}/     \{printmap[row][8][3]}/\n"
    star_string += f"         \{printmap[row][2][4]}/       \{printmap[row][4][4]}/       \{printmap[row][6][4]}/       \{printmap[row][8][4]}/\n\n"
    return star_string


if __name__ == "__main__":
    try:
        if not sys.argv[1]:
            print("Error: no files selected.")
        elif not sys.argv[2]:
            print("Error: no output file selected.")
        else:
            textfile = stellagama.savefile_command_line(sys.argv[2])
            with open(textfile, 'w') as output:
                output.write(starmap_string(read_json_subsector(sys.argv[1])))
                print("File successfully processed.")
    except IndexError:
        print("Error: no files selected.")
    except json.decoder.JSONDecodeError:
        print("Error: Invalid JSON file.")
