import tkinter as tk
from tkinter import filedialog as fd

def openFile(filePath : str, paper : tk.Text, file_path : list) -> None:
    try:
        file_path.append(filePath)
        if len(file_path) > 1:
            file_path.pop(0)
        with open(filePath, 'r') as file:
            fileContent = file.read()
        
        paragraphs=fileContent.split('\n')
        showText(paper, paragraphs)
        return fileContent

    except FileNotFoundError:
        return f"File '{filePath}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def getContent (content : list, paper: tk.Text, file_path : list) -> None:
    content.append(openFile(fd.askopenfilename(), paper, file_path))
    if len(content) > 1:
        content.pop(0)

def save_file(current_file_path : list, paper : tk.Text) -> None: 
    if len(current_file_path):
        content = paper.get("1.0", "end-1c").split("\n")
        with open(current_file_path[0], 'w') as file:
            for paragraph in content:
                file.write(paragraph)
                file.write('\n')
    else:
        save_file_as(current_file_path, paper)

def save_file_as(current_file_path : list, paper : tk.Text) -> None:
    file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if len(current_file_path): 
        current_file_path.append(file_path)
        current_file_path.pop(0)
    else:
        current_file_path.append(file_path)
    content = paper.get("1.0", "end-1c").split("\n")
    with open(file_path, 'w') as file:
        for paragraph in content:
            file.write(paragraph)
            file.write('\n')

def formatText(paper : tk.Text) -> list[str]:
    text = paper.get("1.0", "end-1c")
    paragraphs = text.split("\n")
    return paragraphs

def showText(paper : tk.Text, paragraphs : list) -> None:
    paper.delete("1.0", "end")
    for paragraph in paragraphs:
        paper.insert("end", paragraph)
        paper.insert("end", "\n")
    paper.delete("end")
    
def create_new_file(current_file_path : list, paper : tk.Text) -> None:    
    paper.delete("1.0", "end")
    save_file_as(current_file_path, paper) 

def selected_text(paper : tk.Text) -> str:
    return paper.tag_ranges(tk.SEL)

def make_text_bold(paper : tk.Text, fonts : list[tuple], indexFont : int, ids : list[int]):
    ids.append(ids[0] + 1)
    ids.pop(0)
    font = fonts[indexFont]
    input = font[2].split()
    id = ids[0]
    changed = False
    for word in input:
        if word == 'bold':
            bold = False
            changed = True
            input.remove(word)
    if not changed:
        bold = True

    output = " ".join(input)

    font = (font[0], font[1], output + " bold") if bold else (font[0], font[1], output)
    fonts[indexFont] = font

    if paper.tag_ranges(tk.SEL):
        paper.tag_add("bold" + str(id), paper.index(tk.SEL_FIRST), paper.index(tk.SEL_LAST))
        paper.tag_configure("bold" + str(id), font = font)

def make_text_italic(paper : tk.Text, fonts : list[tuple], indexFont : int, ids : list[int]):
    ids.append(ids[0] + 1)
    ids.pop(0)
    font = fonts[indexFont]
    input = font[2].split()
    id = ids[0]
    changed = False
    for word in input:
        if word == 'italic':
            italic = False
            changed = True
            input.remove(word)
    if not changed:
        italic = True

    output = " ".join(input)

    font = (font[0], font[1], output + " italic") if italic else (font[0], font[1], output)
    fonts[indexFont] = font

    if paper.tag_ranges(tk.SEL):
        paper.tag_add("italic" + str(id), paper.index(tk.SEL_FIRST), paper.index(tk.SEL_LAST))
        paper.tag_configure("italic" + str(id), font = font)

def make_text_underline(paper : tk.Text, fonts : list[tuple], indexFont : int, ids : list[int]):
    ids.append(ids[0] + 1)
    ids.pop(0)
    font = fonts[indexFont]
    input = font[2].split()
    id = ids[0]
    changed = False
    for word in input:
        if word == 'underline':
            underline = False
            changed = True
            input.remove(word)
    if not changed:
        underline = True

    output = " ".join(input)

    font = (font[0], font[1], output + " underline") if underline else (font[0], font[1], output)
    fonts[indexFont] = font

    if paper.tag_ranges(tk.SEL):
        paper.tag_add("underline" + str(id), paper.index(tk.SEL_FIRST), paper.index(tk.SEL_LAST))
        paper.tag_configure("underline" + str(id), font = font)