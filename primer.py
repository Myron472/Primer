import re, random, io
from time import sleep
try:
	import pyperclip
except ModuleNotFoundError:
	print("To run the program pyperclip module is needed. Install?")
	print("(y/yes - install module, n/no - exit program)")
	while True:
		choice = input(">")
		if choice == "y" or choice == "yes":
			print("Installing...")
			install("pyperclip")
			break
		elif choice == "n" or choice == "no":
			exit()
		else:
			print("Incorrect value")

ver = "v1.1"
help_text = "In development"
print("Primer", ver, "© GlydeR")
sleep(1.4)

# Looping program execution
while True:
	print("\nSelect preferable working mode:\n1. Tell if the number is prime\n2. Output prime numbers from a range\n\nTo see help type 'help'")

	# This loop is needed to not output upper text if user submitted empty value in the input field
	# No need for exit condition as exit() function is used
	while True:
		mode = input(">")

		if mode == "":
			continue

		if mode == "back" or mode == "mode":
			break

		# Tell if a number is prime
		elif mode == "1":
			print("\nType your number")
			while True:
				n = input(">")
				# Exiting loop
				if n == "help": print(help_text)
				elif n == "back": break
				elif n == "exit": exit()
				elif n != "":
					n = int(n)
					is_prime = not re.match(r'^.?$|^(..+?)\1+$', '1' * n)	
					if is_prime == True:
						print("Prime")
					else:
						print("Composite")
			# Exiting mode
			if n == "back": break

		# Output
		elif mode == "2":
			while True:
				print("Note: Start and end values themselves also will be included in the range.")
				print("To go back to mode selection menu type 'back' or 'mode'. To exit type 'exit'. To see help type 'help'.\nYou can type these commands in any prompt in this mode.\n")
				print("Set how you want to output result:\n1. Output on the screen\n2. Copy result to clipboard\n3. Write result to a file")
	
				prompting = True
				while prompting:
					output_option = input(">")
					if output_option == "1" or output_option == "2" or output_option == "3":
						print("Set number separator character. Press Enter to leave it's default value (EOL character).\nIf you want to set custom separator character type it into the prompt field.\n(You can set any value of any length).\nYou cannot do any commands while setting this option.")
						# Setting separator character
						sep = input(">")
						# If user submitted empty string (pressed Enter), set separator to eol character
						if sep == "":
							sep = "\n"
						sep_len = len(sep)
						break
					elif output_option == "help":
						print(help_text)
					elif output_option == "back" or output_option == "mode":
						prompting = False
					elif output_option == "exit":
						exit()
					else:
						print("Incorrect value")
				if output_option == "back" or output_option == "mode":
					break
	
				cycling = True
				while cycling:
					prompting = True
					while prompting:
						print("Set the start of range")
						start_range = input(">")
						if start_range.isdigit():
							start_range = int(start_range)
							prompting = False
						elif start_range == "help":
							print(help_text)
						elif start_range == "output" or start_range == "back" or start_range == "mode":
							prompting = False
						elif start_range == "exit":
							exit()
						else:
							print("Not an integer")
					if start_range == "back" or start_range == "output" or start_range == "mode":
						cycling = False
	
					prompting = True
					while prompting:
						print("Set the end of range")
						end_range = input(">")
						if end_range.isdigit():
							end_range = int(end_range)
							prompting = False
						elif end_range == "help":
							print(help_text)
						elif end_range == "output" or end_range == "back" or end_range == "mode":
							prompting = False
						elif end_range == "exit":
							exit()
						else:
							print("Not an integer")
					if end_range == "back" or end_range == "output" or end_range == "mode":
						cycling = False

					# Compute values only if start_range is less than end_range
					elif start_range > end_range:
						print("Sorry, I'm not so flexible and cannot compute backwards.\nPlease, set range values corresponding to shown prompt.")
						continue
					elif start_range == end_range:
						print("If you need to know if certain number is prime use mode 2")
						continue
					else:
						if output_option == "2" or output_option == "3":
							result = ""
						# Output first prime number without separator
						for n in range(start_range, end_range + 1):
							is_prime = not re.match(r'^.?$|^(..+?)\1+$', '1' * n)
							if is_prime == True:
								if output_option == "1":
									print(str(n), end="")
								elif output_option == "2" or output_option == "3":
									result += str(n)
								break
						# Output other prime numbers in range with separator before them
						for n in range(start_range + 1, end_range + 1):
							is_prime = not re.match(r'^.?$|^(..+?)\1+$', '1' * n)
							if is_prime == True:
								if output_option == "1":
									print(sep + str(n), end="")
								elif output_option == "2" or output_option == "3":
									result += sep + str(n)
						if output_option == "1":
							print()
						if output_option == "2":
							pyperclip.copy(result)
							print("Result was successfully copied to clipboard!")
						elif output_option == "3":
							with open("output.txt", "w") as file:
								file.write(result)
						print("")
				if output_option == "back" or output_option == "mode":
					break
				elif start_range == "back" or start_range == "mode":
					break
				try:
					if end_range == "back" or end_range == "mode":
						break
				except NameError:
					pass
			if output_option == "back" or output_option == "mode":
				break
			try:
				if start_range == "back" or start_range == "mode":
					break
			except NameError:
				pass
			try:
				if end_range == "back" or end_range == "mode":
					break
			except NameError:
				pass

		# Output help to screen
		elif mode == "help":
			print(help_text)

		# Exit program
		elif mode == "exit":
			exit()

		# Easter egg :)
		elif mode == "spam":
			print("You shouldn't have done that lol")
			sleep(3)
			word_list = ["SPAM", "BOOGIE", "CHEESE", "EGGS", "CAKEISALIE", "NULL"]
			spam_word = random.choice(word_list)
			choice = random.randint(0, 1)
			if choice == 0:
				while True:
					print(spam_word, end=" ")
			if choice == 1:
				while True:
					rand = " " * random.randint(1, 100)
					print(spam_word, end=rand)

		# Other values not stated in the program
		else:
			print("Incorrect value")