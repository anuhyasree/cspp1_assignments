"""Well then, how can we calculate a more accurate
fixed monthly payment than we did in Problem 2 without
running into the problem of slow code?
  What is a good upper bound? Imagine the
  instead of paying monthly, we paid off the
  entire balance at the end of the year. What we
 ultimately pay must be greater than what we
 would've paid in monthly installments, because
 the interest was compounded on the balance
 we didn't pay off each month. So a good upper
 bound for the monthly payment would be one-twelfth of the balance, after having its
 interest compounded monthly for an entire year."""
def payingdebt_offinayear(balance, annual_interestrate):
    """
    A function to calculate the lowest payment
    """
    def bal_d(balance, pay, annual_interestrate):
        """A function """
        balan_d = balance
        for _ in range(1, 13):
            unpaid_bal = balan_d - pay
            balan_d = unpaid_bal*(1 + (annual_interestrate/12.0))
        return balan_d
    payment_low = balance/12.0
    monthly_interestrate = annual_interestrate/12.0
    payment_high = (balance*((1 + monthly_interestrate)**12))/12.0
    payment = (payment_high + payment_low)/2.0
    epsilon = 0.05556

    while True:
        if  bal_d(balance, payment, annual_interestrate) > epsilon:
            payment_low = payment
        elif bal_d(balance, payment, annual_interestrate) < -epsilon:
            payment_high = payment
        else:
            return round(payment, 2)
        payment = (payment_high + payment_low)/2.0
def main():
    """An output"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(payingdebt_offinayear(data[0], data[1])))
if __name__ == "__main__":
    main()