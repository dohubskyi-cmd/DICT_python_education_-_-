import math
import argparse
import sys

def calculate_diff(p, n, interest):
    i = interest / (12 * 100)
    total_paid = 0
    for m in range(1, n + 1):
        dm = math.ceil((p / n) + i * (p - (p * (m - 1)) / n))
        total_paid += dm
        print(f"Month {m}: payment is {dm}")
    print(f"\nOverpayment = {total_paid - p}")

def calculate_annuity(args):
    i = args.interest / (12 * 100)
    
    if args.type == "annuity" and args.principal and args.periods and not args.payment:
        a = math.ceil(args.principal * (i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1))
        print(f"Your monthly payment = {a}!")
        print(f"Overpayment = {a * args.periods - args.principal}")
        
    elif args.type == "annuity" and args.principal and args.payment and not args.periods:
        n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        years, months = divmod(n, 12)
        
        res = "It will take "
        if years > 0:
            res += f"{years} year" + ("s" if years > 1 else "")
        if years > 0 and months > 0:
            res += " and "
        if months > 0:
            res += f"{months} month" + ("s" if months > 1 else "")
        
        print(f"{res} to repay this loan!")
        print(f"Overpayment = {args.payment * n - args.principal}")
        
    elif args.type == "annuity" and args.payment and args.periods and not args.principal:
        p = math.floor(args.payment / ((i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1)))
        print(f"Your loan principal = {p}!")
        print(f"Overpayment = {args.payment * args.periods - p}")

parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", choices=["annuity", "diff"], help='Type of payment: "annuity" or "diff"')
parser.add_argument("--payment", type=float, help="Monthly payment amount")
parser.add_argument("--principal", type=int, help="Loan principal amount")
parser.add_argument("--periods", type=int, help="Number of months to repay")
parser.add_argument("--interest", type=float, help="Annual interest rate (percentage)")

args = parser.parse_args()

params_list = [args.payment, args.principal, args.periods, args.interest]
count_provided = len([p for p in params_list if p is not None])
has_negative = any(p is not None and p < 0 for p in params_list)

is_error = False

if args.type not in ["annuity", "diff"]:
    is_error = True
elif args.type == "diff" and args.payment is not None:
    is_error = True
elif args.interest is None:
    is_error = True
elif count_provided < 3:
    is_error = True
elif has_negative:
    is_error = True

if is_error:
    print("Incorrect parameters")
else:
    if args.type == "diff":
        calculate_diff(args.principal, args.periods, args.interest)
    else:
        calculate_annuity(args)
