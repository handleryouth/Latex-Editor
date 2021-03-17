import tkinter as tk
from pytexit import py2tex
from pylatexenc.latex2text import LatexNodes2Text
from pylatexenc.latexencode import unicode_to_latex

text_clue = "~ is unbreakable space, use it whenever you want to leave a space which " \
            "is unbreakable, and cannot expand or shrink, as e.q. in names: A.~U.~Thor.\n"\
            "$ (dollar sign) to start and finish math mode.\n_ (underscore) for subscripts in math mode.\n"\
            "^ (hat) for superscripts in math mode.\n"\
            "\ (backslash) starting commands, which extend until the first non-alphanumerical character.\n"\
            "{} (curly brackets) to group and separate commands from its surroundings. Must appear in pairs."\


def changing_toLatex():
    input = entering_input.get("1.0",'end-1c')
    try:
        output_text.configure(state="normal")
        output_text.delete("1.0", "end")
        result = py2tex(input)
        print(result)
        output_text.insert(tk.END, result)
        output_text.configure(state="disabled")

    except:
        output_text.configure(state="normal")
        output_text.delete("1.0", "end")
        result = unicode_to_latex(input)
        print(result)
        output_text.insert(tk.END, result)
        output_text.configure(state="disabled")

def changing_toSymbol():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    input = entering_input.get("1.0", 'end-1c')
    result = LatexNodes2Text().latex_to_text(input)
    print(result)
    output_text.insert(tk.END, result)
    output_text.configure(state="disabled")



#for the text version
root = tk.Tk()
root.title("Latex Translator and Generator")
root.resizable('false', 'false')

#font
helvetic = ("helvetica", 13, "bold")
timesNewRoman = ("Times New Roman", 12)


#container
label_input = tk.Frame(root)
label_input.grid(row = 0)

button_container = tk.Frame(root)
button_container.grid(row = 2)

clue_specialCharacter = tk.Frame(root)
clue_specialCharacter.grid(row = 3)


#input something
entering_text = tk.Label(label_input, text="Enter the Python Formula / Latex Code")
entering_text.grid(row = 0, column = 0)
entering_text.configure(font = timesNewRoman)

entering_input = tk.Text(label_input, width = 120, height = 15)
entering_input.grid(row = 0, column = 1, padx=20)

output_label = tk.Label(label_input, text="The result")
output_label.grid(row = 1, column=0, padx = 20, pady = 20)
output_label.configure(font = timesNewRoman)

output_text = tk.Text(label_input, width = 120, height = 15, cursor ="arrow", state = "disabled")
output_text.grid(row = 1, column = 1, padx = 20, pady = 20)

entering_input.configure(font = helvetic)
output_text.configure(font = helvetic)
#printing the text



#button
pythonic = tk.Button(button_container, text = "Translate Symbol to Latex", command=changing_toLatex, cursor = "hand2")
pythonic.pack(side="left", expand = "YES", padx = 5, pady = 20)
pythonic.configure(font = timesNewRoman)

Latex_translator = tk.Button(button_container, text = "Translate Latex to Symbol", command = changing_toSymbol,  cursor = "hand2")
Latex_translator.pack(side="right", expand = "YES", padx = 5, pady = 20)
Latex_translator.configure(font = timesNewRoman)

#clue
clue = tk.Label(clue_specialCharacter, text = text_clue)
clue.pack()
root.mainloop()