import tkinter as tk
#button click handler
def press(v):
    entry.insert(tk.END,v)
''' called when a number of operator button is clicked inserted the pressed values at the end '''

#clear function
def clear():
    entry.delete(0, tk.END)
''' It clears the calculator screen'''

#Calculation function
def calc():
    try:
        result = eval(entry.get())
        ''' entry.get() retives the expression (eg. 5+3) eval() evaluates the string as python '''
        entry.delete(0, tk.END)
        '''clears old expression'''
        entry.insert(0, result)
        '''Display the result of expression'''
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Get Lost")
    

#Main window creation
root = tk.Tk()
root.title("calcyy") 
root.configure(bg="#1e1e1e")
''' sets the bg colour (dark theme)'''
root.resizable(False, False)
    
#Entry widgets (Display screen)
entry = tk.Entry(
        root,
        font=("TImes new Roman", 20),
        bg="#2d2d2d",
        bd=0,
        justify="right"
    )

entry.grid(row=0,column=0, columnspan=4, padx=12, pady=12, ipady=10)
'''Place entry at top 
columnspan=4 makes it strech across 4 columns'''

#Button Labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

#Dynamic button creation
r=1
c=0
''' rows and column srating points'''

for b in buttons: #iterates through each button label
    cmd = calc if b == "="else lambda x=b: press(x)
    '''if button is "=", cal calc() 
    otherwise call press() with button value 
    lambda x=b prevents late binding issue'''

    tk.Button(
        root,
        text=b,
        command=cmd, #thees threelines creates button widgets
        font=("calibri",14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/" else "#3a3a3a",
        #operator buttons are orange, number buttons are gray
        fg="white",
        bd=0,                                                             
    ).grid(row=r, column=c, padx=6, pady=6)  

    c+=1
    #after 4 coloums, move to next row
    if c==4:
        r+=1
        c=0
    #moves to next row after 4 buttons 
    
#clear button
tk.Button(
    root,
    text="c",
    command=clear,
    font=("Calibri",14),
    bg="#f3bf3b",
    fg="white",
    bd=0,
    width=22,
    height=2
).grid(row=r, column=c, columnspan=4, pady=8)
''' clear the calculator spans across all coloumns '''    

#event loop
root.mainloop()
'''keeps the window running'''