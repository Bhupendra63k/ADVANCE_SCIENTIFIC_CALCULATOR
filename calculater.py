import tkinter as tk
from math import *

class FixedVerticalCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Fixed Vertical Calculator")
        master.configure(bg='white')
        master.resizable(False, False)  # Disable resizing
        
        # Display (fixed width)
        self.display = tk.Entry(master, font=('Arial', 28), width=10, 
                              borderwidth=2, relief='solid', bg='white', fg='black', 
                              justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=(10, 10), padx=10, sticky='ew')
        
        # Button layout (vertical)
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('(', ')', '⌫', 'C'),
            ('sin', 'cos', 'tan', '√'),
            ('log', 'ln', 'π', '^'),
            ('e', 'n!', ' ', ' ')
        ]
        
        # Button styling
        btn_font = ('Arial', 16)
        btn_width = 5
        btn_height = 2
        
        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                if text == ' ':
                    continue  # Skip empty buttons
                
                btn = tk.Button(
                    master, text=text, font=btn_font, width=btn_width, height=btn_height,
                    bg='#f8f9fa' if not text.isdigit() else 'white',
                    fg='black',
                    activebackground='#e9ecef',
                    borderwidth=1, relief='solid',
                    command=lambda t=text: self.button_click(t)
                )
                
                # Special buttons
                if text == '=':
                    btn.config(bg='#007bff', fg='white')
                elif text == 'C':
                    btn.config(bg='#ff6b6b', fg='white')
                elif text in ['+', '-', '*', '/', '^']:
                    btn.config(bg='#e9ecef')
                
                btn.grid(row=row_idx+1, column=col_idx, padx=2, pady=2, sticky='nsew')
    
    def button_click(self, char):
        current = self.display.get()
        
        if char == '=':
            try:
                expr = current.replace('π', 'pi').replace('e', 'exp(1)')
                expr = expr.replace('√', 'sqrt').replace('^', '**')
                expr = expr.replace('log', 'log10').replace('ln', 'log')
                result = eval(expr)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif char == 'C':
            self.display.delete(0, tk.END)
        elif char == '⌫':
            self.display.delete(len(current)-1, tk.END)
        elif char == 'n!':
            try:
                num = float(current)
                result = factorial(int(num))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, char)

# Create and run the calculator
root = tk.Tk()
root.geometry("300x600")  # Fixed size (width x height)
calc = FixedVerticalCalculator(root)
root.mainloop()