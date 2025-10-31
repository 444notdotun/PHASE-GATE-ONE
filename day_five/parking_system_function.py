
def check_for_slot(name,parking_slot):
	for position in range(len(parking_slot)):
		
			
		if parking_slot[position] == 0:
			parking_slot[position] = name
			expected = parking_slot.index(name)
			break
		
		if parking_slot[position] != 0:
			expected= "There is no available parking slot"
	return expected

def retrieve_parked_car(input,name,parking_slot):
		
	for count in parking_slot:
		print(count)
		if count == name:
			
			expected = parking_slot.index(name)
			break
		else:	
			return "ENTER A VALID NAME"
	if input.isdigit():		
		if int(input) ==  expected:
			parking_slot[int(input)] = 0
			return "THANK YOU AND HOPE TO SEE YOU SOON"
		return "ENTER A VALID KEY"
	else:
		return "ENTER A VALID KEY"

def show_parking_lot(parking_slot):
	for count in range(len(parking_slot)):
		if parking_slot[count] != 0:
			parking_slot[count] = 1
	return parking_slot

def main_menu():
	menu="""
================================
NOTDOTUN'S AUTOMATED PARKING LOT
================================
WHAT DO YOU WANT TO DO?
1-> PARK VEHICLE
2-> RETRIEVE PARKED VEHICLE
3-> SHOW PARKING LOT
4-> EXIT
================================
	"""
	return menu

