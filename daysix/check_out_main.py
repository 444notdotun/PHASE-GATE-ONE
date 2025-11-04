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
		if product_price.isdigit():
			prices.append(product_price)
			product_price = float(product_price)
			
			total_amount = sub_total(product_price,total_amount)
			
			
			
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
while(True):
	payment = float(input("enter payment amount: "))
	grand_total = total_amounts(vat_price(total_amount),total_amount)
	balance_of = float(balance(grand_total,payment))

	if payment < 0 and payment < balance_of:
		print("payment can not be less than zero")
	elif payment > 0 and payment < balance_of:
		print("payment can not be less than balance")
	else:

		print(" ")
		

		print(payment_receipt())
		for count in range(len(product_list)):
			print(f" {product_list[count]} => {prices[count]}")

		print(f" Total paid: #{payment}")
		print(f" Grand Total: #{total_amounts(vat_price(total_amount),total_amount)}")
	
		

		print(f" Balance #{balance(grand_total,payment):.2f}")
		print(transaction_status(balance(grand_total,payment)))
		break



