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


def dif(p, n, i, mo):
    d = p / n + (i / 12 * 100) + (p - (p * (mo - 1) / n))
    print(f"Month {mo}: payment is {round(d)}")


def periods(lp, mp):
    i = round(lp / 12 / 100)
    n = math.ceil(math.log((mp / (mp - i * lp)), (1 + i)))
    return n


def annuity(lp, per, li):
    i = li / 12 / 100
    a = math.ceil(lp * (i * ((1 + i) ** per)) / (((1 + i) ** per) - 1))
    print(f"Your annuity payment = {a}!")


def prin(per, li, pay):
    i = li / 12 / 100
    p = pay / (i * math.pow((1 + i), per) / ((1 + i) ** per - 1))
    return p

if args.principal != "none" and args.periods != "none" and args.interest != "none" and args.type == "diff" and args.payment == None:
    month = 1
    while month != args.periods + 1:
        dif(args.principal, args.periods, args.interest, month)
        month += 1
elif args.principal != "none" and args.periods != "none" and args.interest != "none" and args.type == "annuity" and args.payment == None:
    annuity(args.principal, args.periods, args.interest)

#periods(args.principal, args.payment)
#annuity(args.principal, args.periods, args.interest)
#prin(args.periods, args.interest, args.payment)
print(args)

if args.type != "diff" and args.type != "annuity":
    print("Incorect parameters")
else:
    print("OK")
