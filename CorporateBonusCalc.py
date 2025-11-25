# MonthlyBasePay = float(input("Enter the monthly base pay: "))
# EligibleEarnings = MonthlyBasePay*3
# TargetNonusPercentage = float(
#     input("Enter the target non-US percentage (as a decimal): "))
# BonusPayoutFactor = float(
#     input("Enter the bonus payout factor (as a decimal): "))
# FactoryPerformanceFactor = float(
#     input("Enter the factory performance factor (as a decimal): "))
# TotalBonusPayoutFactor = BonusPayoutFactor+FactoryPerformanceFactor

# CorporateBonus = EligibleEarnings*TargetNonusPercentage*TotalBonusPayoutFactor
# print(f"The corporate bonus is: P{CorporateBonus:,.2f}")


import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Corporate Bonus Calculator")
app.geometry("400x200")


def calculate_Bonus():
    try:
        MonthlyBasePay = float(monthly_base_pay_entry.get())
        TargetNonusPercentage = float(target_nonus_percentage_entry.get())
        BonusPayoutFactor = float(bonus_payout_factor_entry.get())
        FactoryPerformanceFactor = float(
            factory_performance_factor_entry.get())

        EligibleEarnings = MonthlyBasePay * 3
        TotalBonusPayoutFactor = BonusPayoutFactor + FactoryPerformanceFactor
        CorporateBonus = EligibleEarnings * TargetNonusPercentage * TotalBonusPayoutFactor
        output.config(
            text=f"Bonus: P{CorporateBonus:,.2f}")
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter valid numeric values.")


# GUI setup
# monthly_base_pay_label = tk.Label(
#     app, text="Monthly Base Pay\n (Check on Payslip)")
# monthly_base_pay_label.pack(pady=5)
# monthly_base_pay_entry = tk.Entry(app)
# monthly_base_pay_entry.pack(pady=5)
# target_nonus_percentage_label = tk.Label(
#     app, text="Target Non-US Percentage (as decimal)\n (Check on Workday)")
# target_nonus_percentage_label.pack(pady=5)
# target_nonus_percentage_entry = tk.Entry(app)
# target_nonus_percentage_entry.pack(pady=5)
# bonus_payout_factor_label = tk.Label(
#     app, text="Bonus Payout Factor (as decimal)\n (Check on Broadcast Email)")
# bonus_payout_factor_label.pack(pady=5)
# bonus_payout_factor_entry = tk.Entry(app)
# bonus_payout_factor_entry.pack(pady=5)
# factory_performance_factor_label = tk.Label(
#     app, text="Factory Performance Factor (as decimal)\n(Check on detailed Bonus announcement)")
# factory_performance_factor_label.pack(pady=5)
# factory_performance_factor_entry = tk.Entry(app)
# factory_performance_factor_entry.pack(pady=5)

# calculate_button = tk.Button(
#     app, text="Calculate Bonus", command=calculate_Bonus)
# calculate_button.pack(pady=20)

# output = tk.Label(app, text="", font=("Arial", 12))
# output.pack(pady=5)

# SidebySide Layout

frame = tk.Frame(app)
frame.pack(side=tk.TOP, padx=10, pady=10)

monthly_base_pay_label = tk.Label(
    frame, text="Monthly Base Pay: ")
monthly_base_pay_label.grid(row=0, column=0, sticky="w", pady=1)
monthly_base_pay_entry = tk.Entry(frame)
monthly_base_pay_entry.grid(row=0, column=1, pady=1)
target_nonus_percentage_label = tk.Label(
    frame, text="Target Non-US Percentage (as decimal):")
target_nonus_percentage_label.grid(row=1, column=0, sticky="w", pady=1)
target_nonus_percentage_entry = tk.Entry(frame)
target_nonus_percentage_entry.grid(row=1, column=1, pady=1)
bonus_payout_factor_label = tk.Label(
    frame, text="Bonus Payout Factor (as decimal): ")
bonus_payout_factor_label.grid(row=2, column=0, sticky="w", pady=1)
bonus_payout_factor_entry = tk.Entry(frame)
bonus_payout_factor_entry.grid(row=2, column=1, pady=1)
factory_performance_factor_label = tk.Label(
    frame, text="Factory Performance Factor (as decimal): ")
factory_performance_factor_label.grid(row=3, column=0, sticky="w", pady=1)
factory_performance_factor_entry = tk.Entry(frame)
factory_performance_factor_entry.grid(row=3, column=1, pady=1)

frame3 = tk.Frame(app, width=400, height=20)
frame3.pack(side=tk.TOP, padx=1, pady=1)
output = tk.Label(frame3, text="", font=("Arial", 12))
output.grid(row=1, columnspan=2, pady=5)

frame2 = tk.Frame(app)
frame2.pack(side=tk.TOP, padx=1, pady=1)
calculate_button = tk.Button(
    frame2, text="Calculate Bonus", command=calculate_Bonus)
calculate_button.grid(row=0, columnspan=2, pady=10)


app.mainloop()
