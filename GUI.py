import tkinter as tk
from tkinter import filedialog as fd
import fcs

screen = tk.Tk()
screen.title(" Projekat Čizkejk ")
screen.geometry("1080x720")
screen.attributes('-fullscreen', 0)

content = []
file_path = []

paper = tk.Text(screen, height = 29, width = 65, font = ("", 15))
paper.focus_set()
paper.place(x = 220, y = 10)

openFileButton = tk.Button(screen, bd = 5, command = lambda: fcs.getContent(content, paper, file_path), text = "Open file", height = 2, width = 20)
openFileButton.place(x = 10, y = 10)

saveAsFileButton = tk.Button(screen, bd = 5, command = lambda: fcs.save_file_as(file_path, paper), text = "Save as file", height = 2, width = 20)
saveAsFileButton.place(x = 10, y = 70)

saveFileButton = tk.Button(screen, bd = 5, command = lambda: fcs.save_file(file_path, paper), text = "Save file", height = 2, width = 20)
saveFileButton.place(x = 10, y = 130)

newFileButton = tk.Button(screen, bd = 5, command = lambda: fcs.create_new_file(file_path, paper), text = "Create new file", height = 2, width = 20)
newFileButton.place(x = 10, y = 190)

screen.mainloop()