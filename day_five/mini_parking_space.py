from parking_system_function import*
parking_slot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
	print(main_menu())
	menu_input = input("enter an input: ")
	match menu_input:
		case "1":
			name_input =input("WHAT IS YOUR NAME: ")
			key = check_for_slot(name_input,parking_slot)
			print(f" YOUR VEHICLE IS PARKED, HERE IS YOUR RETRIEVAL KEY ==> {key} <===  KEEP IT SAFE IF YOU'LL BE NEEDING YOUR CAR")

		case "2":
			name_input =input("what is your name:")
			key_input=input("enter your retrieval key:")
			print(retrieve_parked_car(key_input,name_input,parking_slot))

		case "3":
			print("""
WELCOME 
0 ==> EMPTY
1 ==> OCCUPIED 
			""")
			print(show_parking_lot(parking_slot))

		case "4":
			print("BYE, SEE YOU SOON")
			break

		case _:
			print("ENTER A VALID INPUT")
		
			
			
			
			
 