from check_out_function import *
from check_out_function2 import *
product_list = []
prices = []
total_amount = 0
while(True):
	product_name =input("enter product name: ")
	product_list.append(product_name)
	while(True):
		product_price = input("enter product price: ")
		if product_price.isdigit:
			prices.append(product_price)
			total_amount = sub_total(float(product_price),total_amount)
			
			break
		else:
			print("enter numbers")
		
	choice = input("continue or done(1/2)")
	match choice:
		case "1":
			...
				
		case "2":
			break
		case _:
			print ("enter a valid input")
print(" ")

print(invoice())
for count in range(len(product_list)):
	print(f" {product_list[count]} => {prices[count]}")
print(" ")

print(f" subtotal: #{total_amount}")
print(f" VAT(7.5%) : #{vat_price(total_amount)}")
print(f" Total Amount: #{total_amounts(vat_price(total_amount),total_amount)}")

payment = float(input("enter payment amount: "))

print(" ")

print(payment_receipt())
for count in range(len(product_list)):
	print(f" {product_list[count]} => {prices[count]}")

print(f" Total paid: #{payment}")
print(f" Grand Total: #{total_amounts(vat_price(total_amount),total_amount)}")
grand_total = total_amounts(vat_price(total_amount),total_amount)
balance_of = balance(grand_total,payment)
if balance_of < 0:
	print(transaction_status(balance(grand_total,payment)))
else:

	print(f" Balance #{balance(grand_total,payment):.2f}")
	print(transaction_status(balance(grand_total,payment)))



