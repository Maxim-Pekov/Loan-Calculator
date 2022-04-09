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
loan_principal = int(input("Enter the loan principal:"))
print('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')
calculate = input()
if calculate == "m":
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    numbers_months = loan_principal / monthly_payment
    if numbers_months == 1:
        print("It will take,", round(numbers_months), "month to repay the loan")
    else:
        print("It will take,", round(numbers_months), "months to repay the loan")
elif calculate == "p":
    print("Enter the number of months:")
    numbers_months = int(input())
    payment = round(loan_principal / numbers_months)
    if loan_principal % numbers_months == 0:
        print("Your monthly payment =", round(payment))
    elif loan_principal % numbers_months != 0:
        lastpayment = loan_principal - (numbers_months - 1) * payment
        print("Your monthly payment =", round(payment + 1), "and the last payment =", round(lastpayment - numbers_months + 1), ".")


