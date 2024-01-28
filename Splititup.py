from collections import defaultdict
from heapq import heappush, heappop

def calculate_interest(principal, interest_rate, weeks):
    return principal * ((1 + interest_rate) ** weeks - 1)

def reconcile_expenses(expenses):
    balances = defaultdict(int)
    
    for expense in expenses:
        paid_by, amount, *participants = expense.split('/')
        amount = int(amount)
        share = amount / len(participants)
        
        for participant in participants:
            balances[participant] -= share
        
        balances[paid_by] += amount

    return balances

def reconcile_loans(loans):
    balances = defaultdict(int)
    loan_records = defaultdict(list)

    for loan in loans:
        lender, borrower, transaction_type, amount = loan.split('/')
        amount = int(amount)
        
        if transaction_type == 'L':
            loan_records[borrower].append((lender, amount))
            balances[lender] -= amount
            balances[borrower] += amount
        elif transaction_type == 'T':
            balances[lender] += amount
            balances[borrower] -= amount
            loan_records[borrower].sort()  # Sort by lender for lexicographical order
            for lender, loan_amount in loan_records[borrower]:
                if loan_amount <= amount:
                    balances[lender] += loan_amount
                    balances[borrower] -= loan_amount
                    amount -= loan_amount
                else:
                    balances[lender] += amount
                    balances[borrower] -= amount
                    break

    return balances

def reconcile_balances(balances):
    result = []

    for person, balance in sorted(balances.items()):
        if balance != 0:
            result.append((person, balance))

    return result

def group_expense_management(n, transactions):
    expenses = []
    loans = []
    
    for _ in range(n):
        transaction = transactions[_]
        if 'L' in transaction:
            loans.append(transaction)
        else:
            expenses.append(transaction)

    balances_expenses = reconcile_expenses(expenses)
    balances_loans = reconcile_loans(loans)

    # Combine the balances of expenses and loans
    for person, balance in balances_loans.items():
        balances_expenses[person] += balance

    result = reconcile_balances(balances_expenses)

    return result

# Input
n = int(input())
transactions = [input() for _ in range(n)]

# Output
result = group_expense_management(n, transactions)
if result:
    for payer, amount in result:
        print(f"{payer}/{'/'.join(sorted(result, key=lambda x: x[0]))}/{abs(amount)}")
else:
    print("NO DUES.")
