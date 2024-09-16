from colors import *
from helper_code import color_text

class Ptable:
    def __init__ (self, rows=None):
        self.horizontal_str = ""
        if rows != None: 
            self.rows = [list(map(str, r)) for r in rows]
            flattened_row = [item for sublist in self.rows for item in sublist]
            self.max_col_width = max(map(len, flattened_row))

    def make_matrix(self, to, skip, prefix = "", correct = [], failed = [], not_attended = []):
        levels = []
        for i in range(1, to+1, skip):
            if prefix != "":
                levels.append(prefix+str(i) for i in list(range(i,i+skip)))
            else: levels.append(i for i in list(range(i,i+skip)))
        pt = Ptable(levels)
        pt.make_row()

        for level in not_attended:
            pt.horizontal_str = pt.horizontal_str.replace(f"Level: {level}", bcolors.NOTATTENDED+f"Level: {level}"+bcolors.RESET, 1)
        for level in correct:
            pt.horizontal_str = pt.horizontal_str.replace(f"Level: {level}", bcolors.CORRECT+f"Level: {level}"+bcolors.RESET, 1)
        for level in failed:
            pt.horizontal_str = pt.horizontal_str.replace(f"Level: {level}", bcolors.FAIL+f"Level: {level}"+bcolors.RESET, 1)

        print(pt.horizontal_str)
        print(color_text("▬", bcolors.CORRECT)," --- Correct")
        print(color_text("▬", bcolors.FAIL)," --- Incorrect")
        print(color_text("▬", bcolors.NOTATTENDED)," --- Not Attended")

    def make_row(self):
        for row in self.rows:
            if len(row) == 0: raise RuntimeError("Make sure row is not empty")
            if self.horizontal_str == "": self.horizontal()
            
            self.horizontal_str += "\n"
            for idx, ele in enumerate(row):
                self.horizontal_str += "|"
                self.horizontal_str += ele.center(self.width)
                if idx == len(row)-1: self.horizontal_str += "|"
            self.horizontal_str += "\n"
            self.horizontal()

    def horizontal(self):
        self.width = self.max_col_width+2
        for idx in range(len(self.rows[0])):
            self.horizontal_str += "+" + "-"*self.width
            if idx == len(self.rows[0])-1: self.horizontal_str += "+"