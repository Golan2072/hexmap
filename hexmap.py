# Cepheus Light Retro Hexagon Map Generator.

import stellagama
import json
import sys

def number_to_hex(number):
    if number < 10:
        return number
    if number == 10:
        return "A"
    if number == 11:
        return "B"
    if number == 12:
        return "C"
    if number == 13:
        return "D"
    if number == 14:
        return "E"
    if number == 15:
        return "F"
    if number == 16:
        return "G"

class World2:
    def __init__(self, json_data):
        self.name = json_data["name"]
        self.location_hex = json_data["hex"]
        self.starport = json_data["starport"]
        self.size = json_data["size"]
        self.atmosphere = json_data["atmosphere"]
        self.hydrographics = json_data["hydrographics"]
        self.population = json_data["population"]
        self.government = json_data["government"]
        self.law = json_data["law"]
        self.tl = json_data["tl"]
        self.zone = json_data["zone"]
        self.base = json_data["base"]
        self.gas_giants = json_data["gas_giants"]
        self.trade = json_data["trade"]
    
    def worldtype(self):
        if self.hydrographics > 0:
            worldtype = "@"
        elif self.size == 0:
            worldtype = "#"
        else:
            worldtype = "O"
        return worldtype
    
    def naval_base(self):
        return "*" if "N" in self.base else " "
    
    def scout_base(self):
        return "^" if "S" in self.base else " "
        
    def uwp(self):
        return f"{self.starport}{number_to_hex(self.size)}{number_to_hex(self.atmosphere)}{number_to_hex(self.hydrographics)}{number_to_hex(self.population)}{number_to_hex(self.government)}{number_to_hex(self.law)}-{number_to_hex(self.tl)}"
    
    def __str__(self):
        return f"{self.location_hex} {self.name} - {self.uwp()}"


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
                    starmap[int(column)][int(row)] = World(data[column][row])
    return starmap


def blank_map():
    starmap = {}
    for column in range(0, 9):
        starmap[column] = {}
        for row in range(0, 11):
            starmap[column][row] = None
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
    
    # Convert starmap to preliminary format.
    # Format is a 3d array, Row, Column, Line
    printmap = [[[] for i in range(9)] for j in range(11)]
    print("Created Array")
    for row in range(0,11):
        for column in range(1,9):
            if starmap[column][row] is not None:
                printmap[row][column].append(f"  {starmap[column][row].starport} {starmap[column][row].gas_giants}")
                printmap[row][column].append(f"{starmap[column][row].naval_base()}  {starmap[column][row].worldtype()}   ")
                printmap[row][column].append(f"{name_converter(starmap[column][row].name)}")
                printmap[row][column].append(f"{starmap[column][row].scout_base()}{hex_number(column, row, starmap[column][row].worldtype)}")
            else:
                printmap[row][column].append("     ")
                printmap[row][column].append("       ")
                printmap[row][column].append("       ")
                printmap[row][column].append("_____")
    
    print("Filled Array")

    # Each cell has 4 lines with 5,7,7,5 cells.
    for row in range(1, 11):
        star_string += f"  /{printmap[row][1][0]}\{printmap[row-1][2][2]}/{printmap[row][3][0]}\{printmap[row-1][4][2]}/{printmap[row][5][0]}\{printmap[row-1][6][2]}/{printmap[row][7][0]}\{printmap[row-1][8][2]}/ \n"
        star_string += f" /{printmap[row][1][1]}\{printmap[row-1][2][3]}/{printmap[row][3][1]}\{printmap[row-1][4][3]}/{printmap[row][5][1]}\{printmap[row-1][6][3]}/{printmap[row][7][1]}\{printmap[row-1][8][3]}/ \n"
        star_string += f" \{printmap[row][1][2]}/{printmap[row][2][0]}\{printmap[row][3][2]}/{printmap[row][4][0]}\{printmap[row][5][2]}/{printmap[row][6][0]}\{printmap[row][7][2]}/{printmap[row][8][0]}\ \n"
        star_string += f"  \{printmap[row][1][3]}/{printmap[row][2][1]}\{printmap[row][3][3]}/{printmap[row][4][1]}\{printmap[row][5][3]}/{printmap[row][6][1]}\{printmap[row][7][3]}/{printmap[row][8][1]}\ \n"
    star_string += f"        \{printmap[row][2][2]}/     \{printmap[row][4][2]}/     \{printmap[row][6][2]}/     \{printmap[row][8][2]}/\n"
    star_string += f"         \{printmap[row][2][3]}/       \{printmap[row][4][3]}/       \{printmap[row][6][3]}/       \{printmap[row][8][3]}/\n\n"
    
    print("Created map")
    return star_string


if __name__ == "__main__":
    try:
        if not sys.argv[1]:
            print("Error: no files selected.")
        else:
            if not sys.argv[2]:
                textfile = ".\default_output.txt"
                print(f"No output file selected. Using {textfile} as default.")
            textfile = stellagama.savefile_command_line(sys.argv[2])
            with open(textfile, 'w') as output:
                output.write(starmap_string(read_json_subsector(sys.argv[1])))
                print("File successfully processed.")
    except IndexError:
        print("Error: no files selected.")
    except json.decoder.JSONDecodeError:
        print("Error: Invalid JSON file.")
