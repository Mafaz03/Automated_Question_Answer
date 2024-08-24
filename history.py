# Code that I prolly wont use, but good to have reference 


class test_repl:
    def __init__(self) -> None:
        self.hardness = 0
        self.subject = ""
    def start(self):
        if self.hardness == 0: self.hardness = int(input("Set your hardness (0-10): "))
        if self.subject == "": self.subject = str(input("Select your subject ('help' for assistance): "))
        print(self.subject)
        # import pdb; pdb.set_trace()
        while self.subject.lower() == "help":
            rows = [["Physics", "Chemistry", "Math", "Biology"], ["Computer Science", "Soft Skills", "Aptitude", "English"], ["French", "Machine Learning", "Data Mining", "Statistics"]]
            pt = ptable(rows)
            pt.make_row()
            print(pt.horizontal_str)

            self.subject = str(input("\nSelect your subject ('help' for assistance): "))
        while True:
            str(input("hello: "))


            