class ptable:
    def __init__ (self, rows):
        self.horizontal_str = ""
        self.rows = rows
        flattened_row = [item for sublist in rows for item in sublist]
        self.max_col_width = max(map(len, flattened_row))

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