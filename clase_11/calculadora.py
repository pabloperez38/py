import tkinter as tk
from tkinter import ttk
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")                                 
        
        # Variables
        self.current_number = tk.StringVar()
        self.current_number.set("0")
        self.stored_number = 0
        self.operation = ""
        self.new_number = True
        
        # Crear interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Display
        display_frame = tk.Frame(main_frame, bg="#34495e", relief=tk.RAISED, bd=3)
        display_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.display = tk.Label(
            display_frame,
            textvariable=self.current_number,
            font=("Arial", 24, "bold"),
            bg="#34495e",
            fg="white",
            anchor="e",
            padx=10,
            pady=10
        )
        self.display.pack(fill=tk.X)
        
        # Botones
        buttons_frame = tk.Frame(main_frame, bg="#2c3e50")
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurar grid
        for i in range(7):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Definir botones
        buttons = [
            ("C", 0, 0, "#e74c3c"), ("±", 0, 1, "#95a5a6"), ("%", 0, 2, "#95a5a6"), ("÷", 0, 3, "#f39c12"),
            ("7", 1, 0, "#34495e"), ("8", 1, 1, "#34495e"), ("9", 1, 2, "#34495e"), ("×", 1, 3, "#f39c12"),
            ("4", 2, 0, "#34495e"), ("5", 2, 1, "#34495e"), ("6", 2, 2, "#34495e"), ("-", 2, 3, "#f39c12"),
            ("1", 3, 0, "#34495e"), ("2", 3, 1, "#34495e"), ("3", 3, 2, "#34495e"), ("+", 3, 3, "#f39c12"),
            ("0", 4, 0, "#34495e", 2), (".", 4, 2, "#34495e"), ("=", 4, 3, "#f39c12"),
            ("√", 5, 0, "#9b59b6"), ("x²", 5, 1, "#9b59b6"), ("1/x", 5, 2, "#9b59b6"), ("⌫", 5, 3, "#e67e22"),
            ("sin", 6, 0, "#9b59b6"), ("cos", 6, 1, "#9b59b6"), ("tan", 6, 2, "#9b59b6"), ("log", 6, 3, "#9b59b6")
        ]
        
        # Crear botones
        for button_info in buttons:
            if len(button_info) == 5:  # Botón con colspan
                text, row, col, color, colspan = button_info
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 16, "bold"),
                    bg=color,
                    fg="white",
                    relief=tk.RAISED,
                    bd=3,
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
            else:
                text, row, col, color = button_info
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 16, "bold"),
                    bg=color,
                    fg="white",
                    relief=tk.RAISED,
                    bd=3,
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    
    def button_click(self, value):
        current = self.current_number.get()
        
        if value.isdigit() or value == ".":
            if self.new_number:
                self.current_number.set(value)
                self.new_number = False
            else:
                if value == "." and "." in current:
                    return
                self.current_number.set(current + value)
        
        elif value in ["+", "-", "×", "÷"]:
            if self.operation and not self.new_number:
                self.calculate()
            self.stored_number = float(current)
            self.operation = value
            self.new_number = True
        
        elif value == "=":
            if self.operation and not self.new_number:
                self.calculate()
                self.operation = ""
                self.new_number = True
        
        elif value == "C":
            self.clear()
        
        elif value == "±":
            if current != "0":
                if current.startswith("-"):
                    self.current_number.set(current[1:])
                else:
                    self.current_number.set("-" + current)
        
        elif value == "%":
            try:
                result = float(current) / 100
                self.current_number.set(str(result))
            except ValueError:
                self.current_number.set("Error")
        
        elif value == "⌫":
            if len(current) > 1:
                self.current_number.set(current[:-1])
            else:
                self.current_number.set("0")
        
        elif value == "√":
            try:
                result = math.sqrt(float(current))
                self.current_number.set(str(result))
            except ValueError:
                self.current_number.set("Error")
        
        elif value == "x²":
            try:
                result = float(current) ** 2
                self.current_number.set(str(result))
            except ValueError:
                self.current_number.set("Error")
        
        elif value == "1/x":
            try:
                result = 1 / float(current)
                self.current_number.set(str(result))
            except ValueError:
                self.current_number.set("Error")
        
        elif value == "sin":
            try:
                result = math.sin(math.radians(float(current)))
                self.current_number.set(str(result))
            except ValueError:
                self.current_number.set("Error")
        
        elif value == "cos":
            try:
                result = math.cos(math.radians(float(current)))
                self.current_number.set(str(result))
            except ValueError:
                self.current_number.set("Error")
        
        elif value == "tan":
            try:
                result = math.tan(math.radians(float(current)))
                self.current_number.set(str(result))
            except ValueError:
                self.current_number.set("Error")
        
        elif value == "log":
            try:
                result = math.log10(float(current))
                self.current_number.set(str(result))
            except ValueError:
                self.current_number.set("Error")
    
    def calculate(self):
        try:
            current = float(self.current_number.get())
            if self.operation == "+":
                result = self.stored_number + current
            elif self.operation == "-":
                result = self.stored_number - current
            elif self.operation == "×":
                result = self.stored_number * current
            elif self.operation == "÷":
                if current == 0:
                    self.current_number.set("Error")
                    return
                result = self.stored_number / current
            
            # Formatear resultado
            if result.is_integer():
                self.current_number.set(str(int(result)))
            else:
                self.current_number.set(str(result))
        except ValueError:
            self.current_number.set("Error")
    
    def clear(self):
        self.current_number.set("0")
        self.stored_number = 0
        self.operation = ""
        self.new_number = True

def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()
