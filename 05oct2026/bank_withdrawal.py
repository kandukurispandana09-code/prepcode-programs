balance = 10000
requested_amount = 5000

allowed = (requested_amount <= balance)and(requested_amount % 500 == 0)
print("transaction allowed:",allowed)