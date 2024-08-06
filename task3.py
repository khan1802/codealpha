import tkinter as tk
from random import shuffle

class MemoryPuzzleGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Memory Puzzle Game")
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.cards = list(range(8)) * 2
        shuffle(self.cards)
        self.buttons = []
        self.clicked = []
        self.matches = 0
        self.time_left = 60

        for i in range(16):
            button = tk.Button(self.frame, text="", command=lambda i=i: self.click(i), height=3, width=6)
            button.grid(row=i//4, column=i%4)
            self.buttons.append(button)

        self.time_label = tk.Label(self.root, text="Time left: 60")
        self.time_label.pack()

        self.update_time()

    def click(self, i):
        if len(self.clicked) < 2 and i not in self.clicked:
            self.buttons[i].config(text=str(self.cards[i]))
            self.clicked.append(i)
            if len(self.clicked) == 2:
                self.root.after(500, self.check_match)

    def check_match(self):
        if self.cards[self.clicked[0]] == self.cards[self.clicked[1]]:
            self.matches += 1
            self.buttons[self.clicked[0]].config(state="disabled")
            self.buttons[self.clicked[1]].config(state="disabled")
        else:
            self.buttons[self.clicked[0]].config(text="")
            self.buttons[self.clicked[1]].config(text="")
        self.clicked = []
        if self.matches == 8:
            self.time_label.config(text="You won!")
            for button in self.buttons:
                button.config(state="disabled")

    def update_time(self):
        self.time_left -= 1
        self.time_label.config(text=f"Time left: {self.time_left}")
        if self.time_left > 0:
            self.root.after(1000, self.update_time)
        else:
            self.time_label.config(text="Time's up!")
            for button in self.buttons:
                button.config(state="disabled")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = MemoryPuzzleGame()
    game.run()