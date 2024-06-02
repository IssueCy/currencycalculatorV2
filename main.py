import tkinter as tk

class CalcGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x400")
        self.window.title("Currency Calculator")
        self.window.iconbitmap("gruenerkreis.ico")

        # Header
        self.header = tk.Label(self.window, text="Currency Calculator", font=('Arial', 16, 'bold'))
        self.header.pack(pady=20)

        # Entry - Amount
        self.amount_frame = tk.Frame(self.window)
        self.amount_frame.pack(pady=10)

        self.amount_info = tk.Label(self.amount_frame, text="Enter the amount you want to exchange:", font=('Arial', 10))
        self.amount_info.pack(side=tk.LEFT)

        self.amount = tk.Entry(self.amount_frame)
        self.amount.pack(side=tk.LEFT)

        
        self.currency_frame = tk.Frame(self.window)
        self.currency_frame.pack(pady=10)

        self.currency_info = tk.Label(self.currency_frame, text="Enter the currency you want to exchange from:", font=('Arial', 10))
        self.currency_info.pack(side=tk.LEFT)

        self.currency = tk.Entry(self.currency_frame)
        self.currency.pack(side=tk.LEFT)

        
        self.target_currency_frame = tk.Frame(self.window)
        self.target_currency_frame.pack(pady=10)

        self.target_currency_info = tk.Label(self.target_currency_frame, text="Enter the currency you want to exchange to:", font=('Arial', 10))
        self.target_currency_info.pack(side=tk.LEFT)

        self.target_currency = tk.Entry(self.target_currency_frame)
        self.target_currency.pack(side=tk.LEFT)


        self.calc_btn = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calc_btn.pack(pady=20)

        self.result_label = tk.Label(self.window, text="", font=('Arial', 12))
        self.result_label.pack()

        self.window.mainloop()

    def calculate(self):
        amount = float(self.amount.get())
        currency = self.currency.get().upper()
        target_currency = self.target_currency.get().upper()

        conversion_rates = {
            ("EURO", "DOLLAR"): 1.08,
            ("DOLLAR", "EURO"): 0.92,
            ("EURO", "PFUND"): 0.86,
            ("PFUND", "EURO"): 1.17,
            ("DOLLAR", "PFUND"): 0.79,
            ("PFUND", "DOLLAR"): 1.26
        }

        if (currency, target_currency) in conversion_rates:
            rate = conversion_rates[(currency, target_currency)]
            result = amount * rate
            self.result_label.config(text=f"{amount} {currency} sind {result:.2f} {target_currency}")
        else:
            self.result_label.config(text="Invalid currency conversion")

CalcGUI()
