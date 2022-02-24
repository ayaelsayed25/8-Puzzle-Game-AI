from tkinter import *

from algorithms import *


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("8 Puzzle Solver")
        self.root.configure(background='white')
        self.colors = {'0': "#ffffff", '1': "#CCBFE9", '2': "#B8E9E4", '3': "#FEF3D8", '4': "#FFD3CC", '5': "#FFF8C2",
                       '6': "#CFF3CA", '7': "#A9D4C5", '8': "#F8EAD7"}
        self.Labels = []
        self.nodes = Label(self.root, text="", bg="white", font=("Constantia", 14))
        self.nodes.grid(row=3, column=0)
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
        self.depth = Label(self.root, text="", bg="white", font=("Constantia", 14))
        self.depth.grid(row=1, column=4, padx=5)
        self.time = Label(self.root, text="", bg="white", font=("Constantia", 14))
        self.time.grid(row=2, column=4, padx=5)
        # Text Field to Enter Initial State
        self.Label = Label(self.root, text="Initial State", bg="white", font=("Constantia", 14))
        self.Label.grid(row=4, column=0, pady=5)
        self.entry = Entry(self.root)
        self.entry.grid(row=4, column=1, pady=5)
        # Algorithms Buttons
        self.button = Button(self.root, text="BFS", border="0", bg="#CEE5D0", command=lambda: self.update_states(BFS))
        self.button.grid(row=5, column=0, pady=(0, 5))
        self.button = Button(self.root, text="DFS", border="0", bg="#CEE5D0", command=lambda: self.update_states(DFS))
        self.button.grid(row=5, column=2, pady=(0, 5))
        self.button = Button(self.root, text="A* Euclidean", border="0", bg="#CEE5D0", command=lambda: self.update_states(AStarEuclidean))
        self.button.grid(row=6, column=0)
        self.button = Button(self.root, text="A* Manhattan", border="0", bg="#CEE5D0", command=lambda: self.update_states(AStarManhattan))
        self.button.grid(row=6, column=2)
        self.button = Button(self.root, text="Stop", border="0", bg="#CEE5D0", command=self.stop_expansion)
        self.button.grid(row=7, column=1, pady=(0, 5))
        self.stop = False

        self.root.mainloop()

    def stop_expansion(self):
        self.stop = True

    def update_states(self, search_algorithm):
        self.stop = False
        self.root.update()
        path = []
        for i in range(9):
            if self.entry.get()[i] == '0':
                initial_state = State(self.entry.get(), i)
                break
        response = search_algorithm(initial_state)
        if response[0]:
            self.time["text"] = "Total Running time = " + str("{:.2f}".format(response[1]))
            path = response[2]
            self.cost["text"] = "Total Cost = " + str(response[3])
            expansion = response[4]
            self.depth["text"] = "Search Depth = " + str(response[5]) + " Levels"
        else:
            self.time["text"] = "Total Running time = " + str("{:.2f}".format(response[1]))
            expansion = response[2]
            self.cost["text"] = "Can't Be Solved"
            self.nodes["text"] = ""
            self.depth["text"] = "Search Depth = " + str(response[3]) + " Levels"
        for j in range(len(path)):
            if self.stop or not response[0]: break
            self.nodes["text"] = "Path to Goal"
            time.sleep(0.5)
            for i in range(9):
                if path[j][i] != '0':
                    num = path[j][i]
                else:
                    num = ""
                self.Labels[i]["text"] = num
                self.Labels[i]["bg"] = self.colors[path[j][i]]
            self.root.update()
        time.sleep(2)
        for j in range(len(expansion)):
            if self.stop: break
            self.nodes["text"] = "Nodes Expansion"
            self.nodes["bg"] = "#FFD3CC"
            time.sleep(0.5)
            for i in range(9):
                if expansion[j][i] != '0':
                    num = expansion[j][i]
                else:
                    num = ""
                self.Labels[i]["text"] = num
                self.Labels[i]["bg"] = self.colors[expansion[j][i]]
            self.root.update()


app = GUI()
