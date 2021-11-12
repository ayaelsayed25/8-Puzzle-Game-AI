import time
from tkinter import *


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("8 Puzzle Solver")
        self.root.configure(background='white')
        self.colors = {'0': "#ffffff", '1': "#CCBFE9", '2': "#B8E9E4", '3': "#FEF3D8", '4': "#FFD3CC", '5': "#FFF8C2",
                       '6': "#CFF3CA", '7': "#A9D4C5", '8': "#F8EAD7"}
        self.Labels = []
        self.default = "012345678"
        # Grid Initialization
        for i in range(9):
            if self.default[i] != '0':
                num = self.default[i]
            else:
                num = ""
            self.Labels.append(
                Label(self.root, text=num, bg=self.colors[self.default[i]], width=20, height=10, relief=RAISED, bd=3))
            self.Labels[i].grid(row=int(i / 3), column=int(i % 3))
        # Labels to view : cost of path, nodes expanded, and search depth–running time
        self.cost = Label(self.root, text="", bg="white", font=("Constantia", 14))
        self.cost.grid(row=0, column=4, padx=5)
        self.expansion = Label(self.root, text="", bg="white", font=("Constantia", 14))
        self.expansion.grid(row=1, column=4, padx=5)
        self.time = Label(self.root, text="", bg="white", font=("Constantia", 14))
        self.time.grid(row=3, column=0, padx=5)
        # Text Field to Enter Initial State
        self.Label = Label(self.root, text="Initial State", bg="white", font=("Constantia", 14))
        self.Label.grid(row=3, column=0, pady=5)
        self.entry = Entry(self.root, textvariable=self.default)
        self.entry.grid(row=3, column=1, pady=5)
        # Algorithms Buttons
        self.button = Button(self.root, text="BFS", border="0", bg="#CEE5D0", command=self.update_states)
        self.button.grid(row=5, column=0, pady=(0, 5))
        self.button = Button(self.root, text="DFS", border="0", bg="#CEE5D0", command=self.update_states)
        self.button.grid(row=5, column=2, pady=(0, 5))
        self.button = Button(self.root, text="A* Euclidean", border="0", bg="#CEE5D0", command=self.update_states)
        self.button.grid(row=6, column=0, pady=(0, 5))
        self.button = Button(self.root, text="A* Manhattan", border="0", bg="#CEE5D0", command=self.update_states)
        self.button.grid(row=6, column=2, pady=(0, 5))

        self.root.mainloop()

    def update_states(self):
        path = ["056781234", "012345678"]

        for j in range(len(path)):
            for i in range(9):
                if path[j][i] != '0':
                    num = path[j][i]
                else:
                    num = ""
                # Labels[i].pack()
                print(self.Labels[i]["text"])
                self.Labels[i]["text"] = num
                self.Labels[i]["bg"] = self.colors[path[j][i]]
            self.root.update()
            time.sleep(5)


app = GUI()
