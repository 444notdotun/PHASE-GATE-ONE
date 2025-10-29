from quiz_function import *
while True:
	print(main_menu())
	menu_input = input("ENTER INPUT: ")
	match menu_input:
		case "1":
			question = questioner()
			print(f" QUESTION ==> {question}")
			question_index(question)
			print(answer(question))
			answer = input("ANSWER==>: ")
			print(validation(answer,question,count))
			
		case "2":
			break
			
			
		case _:
			print("ENTER A VALID INPUT")