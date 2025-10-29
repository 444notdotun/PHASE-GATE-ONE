import random
questions=["what is my name?", "who is your java sensei?","whats the building you are in called?","what is the name of the guy from chad","Which planet is known as the Red Planet?","Who painted the Mona Lisa?","Which element has the chemical symbol 'O'?","Which country invented paper?"]

answers=["adedotun","miss ope","village","beny","mars","Leonardo","Oxygen","China","lagos","ebuka","lagos","sabo","semi-colon","SK","class daddy","nissi","moses","ekuwe","nitrogen","earth","jupiter","femi","korean"]

validate_answer = {"what is my name?":"adedotun","who is your java sensei?": "miss ope" , "whats the building you are in called?":"village", "what is the name of the guy from chad":"beny","Which planet is known as the Red Planet?":"mars","Who painted the Mona Lisa?":"leonardo","Which element has the chemical symbol 'O'?":"oxygen","Which country invented paper?":"china"}

count = 0

def questioner():
	
	return random.choice(questions)
	

def question_index(num):
	return questions.index(num)

def answer(num):
	return ( random.choice(answers),random.choice(answers),random.choice(answers),
answers[question_index(num)])

def validation(input,question,count):
	
	if input == validate_answer[question]:
		
		return "CORRECT!"
	else:
		return "INCORRECT!"


def main_menu():
	menu="""
====================
	WELCOME!
====================
loading.............



=====================
ARE YOU READY!!!
====================
1-> YES
2-> NO
	"""
	return menu


def get_counter(count):
	return count
	

	