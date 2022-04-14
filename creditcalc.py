import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
commands = [args.type, args.payment, args.principal, args.periods, args.interest]
sum_payment = 0

def dif(p, n, i, mo):
    d = p / n + (i / 12 / 100) * (p - (p * (mo - 1) / n))
    print(f"Month {mo}: payment is {math.ceil(d)}")
    return math.ceil(d)


def periods(lp, mp, li):
    i = li / 12 / 100
    n = math.ceil(math.log((mp / (mp - i * lp)), (1 + i)))
    return n


def annuity(lp, per, li):
    i = li / 12 / 100
    a = math.ceil(lp * (i * ((1 + i) ** per)) / (((1 + i) ** per) - 1))
    print(f"Your annuity payment = {a}!")
    return a


def prin(per, li, pay):
    i = li / 12 / 100
    p = pay / (i * math.pow((1 + i), per) / ((1 + i) ** per - 1))
    print(f"Your loan principal = {math.floor(p)}!")
    return p

if args.principal != "none" and args.periods != "none" and args.interest != "none" and args.type == "diff" and args.payment == None:
    month = 1
    overpayment = 0
    while month != args.periods + 1:
        overpayment += dif(args.principal, args.periods, args.interest, month)
        if month == args.periods:
            print(f"Overpayment = {round(overpayment - args.principal)}")
        month += 1


elif args.principal != None and args.periods != None and args.interest != None and args.type == "annuity" and args.payment == None:
    a = annuity(args.principal, args.periods, args.interest)
    overpayment = args.periods * a - args.principal
    print(f"Overpayment = {round(overpayment)}")


elif args.payment != None and args.periods != None and args.interest != None and args.type == "annuity":
    p = prin(args.periods, args.interest, args.payment)
    overpayment = args.periods * args.payment - p
    print(f"Overpayment = {math.ceil(overpayment)}")


elif args.type == "annuity" and args.payment != None and args.interest != None and args.principal != None:
    n = periods(args.principal, args.payment, args.interest)
    overpayment = n * args.payment - args.principal
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
    print(f"Overpayment = {round(overpayment)}")


else:
    print("Incorrect parameters")


if args.type != "diff" and args.type != "annuity":
    print("Incorrect parameters")

