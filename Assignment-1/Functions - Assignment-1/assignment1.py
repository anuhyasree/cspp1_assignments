"""Functions | Assignment-1 - Paying Debt off in a Year"""
# Write a program to calculate the credit card balance after one year
#if a person only pays the minimum monthly payment required by the
# credit card company each month.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and remaining balance.
#At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print
# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135
# So your program only prints out one thing:
#the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0
# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month =
#(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
def paying_debtoffinayear(balance, annual_interest_rate, montly_interest_rate):
    """def for credit card balance"""
    i = 1
    while i <= 12:
        montly_interest_rate = annual_interest_rate / 12.0
        mini_monthly_payment = montly_interest_rate * balance
        montly_bal = balance - mini_monthly_payment
        updated_bal = montly_bal + (montly_interest_rate * montly_bal)
        balance = updated_bal
        i += 1
        updated_balance_each_month1 = round(updated_bal, 2)
    return updated_balance_each_month1
def main():
    """def"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
   print("Remaining balance :",str(paying_debtoffinayear(data[0], data[1], data[2])))
if __name__ == "__main__":
    main()
