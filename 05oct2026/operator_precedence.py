food_price = 300
quantity = 2
delivery_charge = 50
discount_percent = 10

final_bill = (food_price * quantity)-(1 - discount_percent/ 100)+ delivery_charge
print("final bill",final_bill)