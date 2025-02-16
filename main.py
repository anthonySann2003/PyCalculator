import tkinter as tk
from tkinter import ttk

def handleButtonClick(clickedButtonText):
    currentText = resultVar.get()
    
    if clickedButtonText == "=":
        try:
            #Replacing the symbols with operators to perform calculations
            expression = currentText.replace("÷", "/").replace("x", "*")
            result = eval(expression)

            if result.is_integer(): #Check if whole num
                result = int(result)

            resultVar.set(result)
        except Exception as e:
            resultVar.set("Error")
    elif clickedButtonText == "C":
            resultVar.set("")
    elif clickedButtonText == "%":
            #Convert to decimal
            try:
                currentNumber = float(currentText)
                resultVar.set(currentNumber / 100)
            except ValueError:
                resultVar.set("Error")
    elif clickedButtonText == "±":
        try:
            currentNumber = float(currentText)
            resultVar.set(-currentNumber)
        except ValueError:
            resultVar.set("Error")
    else:
        resultVar.set(currentText + clickedButtonText)


#Creating main window
root = tk.Tk()
root.title("Calculator")

resultVar = tk.StringVar()
resultEntry = ttk.Entry(root, textvariable=resultVar, font=("Helvetica", 24), justify="right")
resultEntry.grid(row=0,column=0,columnspan=4,sticky="nsew")

#Button Layout
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
    ]

#Configure style
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Helvetica", 16), width=10, height=4)


#Create buttons and add to grid
for buttonInfo in buttons:
    buttonText, row, col = buttonInfo[:3]
    colspan = buttonInfo[3] if len(buttonInfo) > 3 else 1
    button = ttk.Button(root, text=buttonText, command=lambda text=buttonText: handleButtonClick(text), style="TButton")
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5,pady=5)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

#Set window size
width = 500
height = 700
root.geometry(f"{width}x{height}")
root.resizable(False,False) #Make window not resizable

#Keyboard control
root.bind("<Return>", lambda event: handleButtonClick("="))
root.bind("<BackSpace>", lambda event: handleButtonClick("C"))

root.mainloop()