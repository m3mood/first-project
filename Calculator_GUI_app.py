import re
import tkinter as tk


class CalculatorApp:
	def __init__(self, root: tk.Tk) -> None:
		self.root = root
		self.expression = tk.StringVar()

		root.title("Calculator")
		root.resizable(False, False)

		display = tk.Entry(
			root,
			textvariable=self.expression,
			justify="right",
			font=("Segoe UI", 24),
			state="readonly",
			readonlybackground="white",
			width=14,
		)
		display.grid(row=0, column=0, columnspan=4, padx=8, pady=8, ipady=8)

		buttons = [
			("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
			("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
			("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
			("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
		]

		for label, row, column in buttons:
			command = self.clear if label == "C" else self.calculate if label == "=" else lambda value=label: self.append(value)
			tk.Button(
				root,
				text=label,
				command=command,
				font=("Segoe UI", 16),
				width=4,
				height=2,
			).grid(row=row, column=column, padx=4, pady=4)

	def append(self, value: str) -> None:
		self.expression.set(self.expression.get() + value)

	def clear(self) -> None:
		self.expression.set("")

	def calculate(self) -> None:
		expression = self.expression.get().replace("×", "*").replace("÷", "/")
		if not expression or not re.fullmatch(r"[0-9+*/.() -]+", expression):
			self.expression.set("Error")
			return

		try:
			result = eval(expression, {"__builtins__": {}}, {})
		except (ArithmeticError, SyntaxError, TypeError, ValueError):
			self.expression.set("Error")
		else:
			self.expression.set(str(result))


if __name__ == "__main__":
	app_root = tk.Tk()
	CalculatorApp(app_root)
	app_root.mainloop()
