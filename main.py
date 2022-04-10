#loan_principal = 'Loan principal: 1000'
#final_output = 'The loan has been repaid!'
#first_month = 'Month 1: repaid 250'
#second_month = 'Month 2: repaid 250'
#third_month = 'Month 3: repaid 500'
#print(loan_principal)
#print(first_month)
#print(second_month)
#print(third_month)
#print(final_output)
import math

print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
calculate = input()
if calculate == "a":
    loan_principal = int(input("Enter the loan principal:"))
    numbers_months = int(input("Enter the number of periods:"))
    loan_interest = float(input("Enter the loan interest:"))
    i = loan_interest / 12 / 100
    a = math.ceil(loan_principal * (i * ((1 + i) ** numbers_months)) / (((1 + i) ** numbers_months) - 1))
    print(f"Your monthly payment = {a}!")
if calculate == "n":
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    i = loan_interest / 12 / 100
    n = math.ceil(math.log((monthly_payment / (monthly_payment - i * loan_principal)), (1 + i)))
    year_qlt = n // 12
    month_qlt = n % 12
    if year_qlt < 1:
        if month_qlt <= 1:
            print(f"It will take {month_qlt} month to repay this loan!")
        else:
            print(f"It will take {month_qlt} months to repay this loan!")
    elif year_qlt >= 1:
        if month_qlt == 0:
            print(f"It will take {year_qlt} years to repay this loan!")
        elif month_qlt == 1:
            print(f"It will take {year_qlt} years and 1 month month to repay this loan!")
        elif month_qlt > 1:
            print(f"It will take {year_qlt} years and {month_qlt} months to repay this loan!")

elif calculate == "p":
    print("Enter the annuity payment:")
    a = float(input())
    print("Enter the number of periods:")
    numbers_months = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    i = loan_interest / 12 / 100
    p = a / ((i * math.pow((1 + i), numbers_months) / ((1 + i) ** numbers_months - 1)))
    print(p)

