import re, random
from time import sleep
print("Prime Calculator 1.0 © GlydeR")
sleep(1.5)

# Cycle that allows to loop the program and to exit it if exit_value equals False
while True:
	print("\nSelect preferable working mode:\n1. Get a range of numbers\n2. Say whether the number is prime")
	print("\nTo close script type 'exit'")
	while True:
		mode = input(">")
		if mode == "":
			continue
		if mode == "1":
			print("Note: Start and end values themselves also will be included in the range.")
			print("To go back to mode selection menu type 'back'. To exit type 'exit'.\nYou can type theese commands in any prompt in this mode.")
			while True:
				prompting = True
				while prompting:
					print("\nSet the start of range")
					start_range = input(">")
					if start_range.isdigit():
						start_range = int(start_range)
						prompting = False
					elif start_range == "back": break
					elif start_range == "exit": exit()
					else:
						print("Not an integer")
				if start_range == "back": break

				prompting = True
				while prompting:
					print("Set the end of range")
					end_range = input(">")
					if end_range.isdigit():
						end_range = int(end_range) + 1
						prompting = False
					elif end_range == "back": break
					elif end_range == "exit": exit()
					else:
						print("Not an integer")
				if end_range == "back": break

				if start_range > end_range:
					print("Sorry, I'm not so flexible and cannot compute backwards.\nPlease, set range values corresponding to shown prompt.")
					continue
				elif start_range == end_range - 1:
					print("If you need to know if certain number is prime use mode 2")
					continue
				else:
					for n in range(start_range, end_range):
						is_prime = not re.match(r'^.?$|^(..+?)\1+$', '1' * n)
						if is_prime == True:
							if n == "":
								print(None)
							else:
								print(n)
			if start_range == "back" or end_range == "back": break
		elif mode == "2":
			print("\nType your number")
			while True:
				n = input(">")
				if n == "back": break
				elif n == "exit": exit()
				elif n != "":
					n = int(n)
					regex_value = not re.match(r'^.?$|^(..+?)\1+$', '1' * n)	
					if regex_value == True:
						print("Prime")
					else:
						print("Composite")
			if n == "back": break
		elif mode == "exit":
			exit()
		if mode == "spam":
			print("You shouldn't have done that lol")
			sleep(3)
			word_list = ["SPAM", "BOOGIE", "CHEESE", "CAKEISALIE", "NULL"]
			spam_word = random.choice(word_list)
			choice = random.randint(0, 1)
			if choice == 0:
				while True:
					print(spam_word, end=" ")
			if choice == 1:
				while True:
					rand = " " * random.randint(1, 100)
					print(spam_word, end=rand)
		else:
			print("Incorrect value")