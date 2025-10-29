import random
questions=["what is my name?", "who is your java sensei?","whats the building you are in called?","what is the name of the guy from chad"]

answers=["adedotun , miss ope , nisi" , "benny,miss ope ,beny,lagos,SK","ebuka,lagos,sabo,semi-colon-village","SK,class daddy,nissi,beny"]

validate_answer = {"what is my name?":"adedotun","who is your java sensei?": "miss ope" , "whats the building you are in called?":"village", "what is the name of the guy from chad":"beny"}

count = 0

def questioner():
	return random.choice(questions)

def question_index(num):
	return questions.index(num)

def answer(num):
	return (answers[question_index(num)])

def validation(input,question,count):
	print(question)
	if input == validate_answer[question]:
		count+=1
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
	

	