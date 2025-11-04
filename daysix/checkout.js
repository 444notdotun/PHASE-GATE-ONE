function sub_total(amount,total_price){
	total_price += amount
	return total_price
}

function vat_price(total_price){
	vatprice = 0.075
	return vatprice*total_price
}
	
function total_amounts(vat_price,total_price){
	return  vat_price+total_price
}

function balance(total_amount,paid){
	return paid - total_amount
}

function transaction_status(balances){
	if (balances < 0){
		return "payment unsuccessful!, come back when you are bouyant"
	}
	return "payment successful, thank you for shopping"
}

function invoice(){
	invoice="===INVOICE====="
	return invoice
}


function payment_receipt(){
	pay = "====PAYMENT RECEIPT===="
	return pay
}



let prompt = require('prompt-sync')();

let product_list = []
let prices = []
let total_amount = 0
let counter = 1
while( counter != 0){
	let product_name =prompt("enter product name: ")
	product_list.push(product_name)
	let counting = 1
	while(counting !=0){
	let product_price = prompt("enter product price: ")
	if (product_price < 0){
		console.log("price can not be less than 0")
	}
	else{		
	prices.push(product_price)
	total_amount = sub_total(Number(product_price),Number(total_amount))
	counting = 0
	}
}
	let choice = Number(prompt("continue or done(1/2)"))
	switch (choice){
		case 1:
			console.log(" ")	
		case 2:
			counter = 0
			
		default:
			console.log ("enter a valid input")
}	
}
console.log(" ")

console.log(invoice())
for(let count=0; count < product_list.lenght; count++){
	console.info( product_list[count], " =>" ,prices[count])
}
console.log(" ")

console.info(" subtotal: #",total_amount)
console.info(" VAT(7.5%) : #",vat_price(total_amount))
console.info(" Total Amount: #",total_amounts(vat_price(total_amount),total_amount))
let count = 1
while(count !=0){

	let payment =prompt("enter payment amount: ")

	payment = Number(payment)
	grand_total = total_amounts(vat_price(total_amount),total_amount)
	balance_of = balance(grand_total,payment)
	if(payment <grand_total){
		console.log("payment is below your cost")
	}
	else if(payment < 0){
		console.log("payment is below your cost")
	}
	
	else{

	console.log(" ")

	console.log(payment_receipt())
	for(let count=0; count < product_list.lenght; count++){
		console.info( product_list[count], " =>" ,prices[count])
	}	

	console.info("Total paid: #",payment)
	console.info("Grand Total: #",total_amounts(vat_price(total_amount),total_amount))


	if (balance_of < 0){
	console.log(transaction_status(balance(grand_total,payment)))
	break
	}
	else{

	console.log(" Balance #",balance(grand_total,payment))
	console.log(transaction_status(balance(grand_total,payment)))
	break
	}
}
}
