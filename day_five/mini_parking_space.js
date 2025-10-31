parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
function check_for_slot(name,parking_slot){
	let expected = 0
	for(let position = 0; position < parking_slot.length;position++){
		console.log(parking_slot[position])	
		if (parking_slot[position] == 0){
			parking_slot[position] = name
			return parking_slot.indexOf(name)
			
		}
		
	}
	return "There is no available parking slot"
	
}

function retrieve_parked_car(input,name,parking_slot){
	let expected =0	
	for(let count = 0; count < parking_slot.length;count++){
		if (parking_slot[count] == name){
			let expected = parking_slot.indexOf(name)
			break
		}
		else{	
			return "ENTER A VALID NAME"
		}
	}
			
	if (input ==  expected){
		return "THANK YOU AND HOPE TO SEE YOU SOON"
	}
	else{
	return "ENTER A VALID KEY"
		}
}

function show_parking_lot(parking_slot){
	for(let count = 0; count < parking_slot.length;count++){
		if( parking_slot[count] != 0){
			parking_slot[count] = 1
		}
	return parking_slot
}
}function main_menu(){
	let menu=`
================================
NOTDOTUN'S AUTOMATED PARKING LOT
================================
WHAT DO YOU WANT TO DO?
1-> PARK VEHICLE
2-> RETRIEVE PARKED VEHICLE
3-> SHOW PARKING LOT
4-> EXIT
================================
	`
	return menu

}



let prompt = require('prompt-sync')();



while (true){
	console.log(main_menu())
	menu_input = prompt("enter an input: ")
	switch(menu_input){
		case "1":
			let name_input =prompt("WHAT IS YOUR NAME:")
			let key = check_for_slot(name_input,parking_slot)
			console.info(" YOUR VEHICLE IS PARKED, HERE IS YOUR RETRIEVAL KEY ==> ", key ," <===  KEEP IT SAFE IF YOU'LL BE NEEDING YOUR CAR")
			break

		case "2":
			let name_input2 =prompt("what is your name:")
			let key_input =prompt("enter your retrieval key:")
			console.log(retrieve_parked_car(key_input,name_input2,parking_slot))
			break
		case "3":
			console.info(`
WELCOME 
0 ==> EMPTY
1 ==> OCCUPIED 
			`)
			console.log(show_parking_lot(parking_slot))
			break
		case "4":
			
			console.log("BYE, SEE YOU SOON")
			process.exit()
			break

		default:
			console.log("ENTER A VALID INPUT")
			process.exit
			break
		}
}