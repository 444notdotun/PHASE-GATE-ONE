from quiz_function import *

while True:
	print(main_menu())
	menu_input = input("ENTER INPUT: ")
	match menu_input:
		case "1":
			count = 0
			counter = 1
			while counter <= 4:
				question = questioner()
				print(f" QUESTION ==> {question}")
				question_index(question)
				print(answer(question))
				option = input("ANSWER==>: ").lower()
				print(validation(option,question,count))
				if validation(option,question,count)=="CORRECT!":
					answers.pop(question_index(question))
					questions.remove(question)
					
					count+=1
				if counter>=4:
					print(f"GAME OVER!, YOU SCORE {get_counter(count)} PLAYED {counter}")
				counter+=1
				if counter==8:
					break
		case "2":
			print("THANKS FOR PLAYING!")
			break
		case _:
			print("ENTER A VALID INPUT")