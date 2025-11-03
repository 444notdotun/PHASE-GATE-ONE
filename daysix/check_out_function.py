def sub_total(amount,total_price):
	total_price += amount
	return total_price

def vat_price(total_price):
	vat_price = 0.075
	return vat_price*total_price
	
def total_amounts(vat_price,total_price):
	return  vat_price+total_price

def balance(total_amount,paid):
	return paid - total_amount

def transaction_status(balances):
	if balances < 0:
		return "payment unsuccessful!, come back when you are bouyant"
	return "payment successful, thank you for shopping"
