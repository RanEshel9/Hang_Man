#hangman
def is_valid_input(letter_guessed):
	"""
	checking if the letter is good or not
	:param letter_guessed: the guess of player
	:type letter_guessed: int/ string/ else
	:return: true or false
	"""
	if (letter_guessed.isalpha() and len(letter_guessed) == 1):
		return True
	elif ((len(letter_guessed) > 1) and (not letter_guessed.isalpha())):
		return False
	elif (not letter_guessed.isalpha()):
		return False
	elif (len(letter_guessed) > 1):
		return False
	
def check_valid_input(letter_guessed, old_letters_guessed):
	"""
	checking if the letter is in the list alredy
	:param letter_guessed: the guess of player
	:param old_letters_guessed: the list
	:type old_letters_guessed: list
	:type letter_guessed: int/ string/ else
	:return: true or false
	"""
	global old_letters_guessed_start
	if (letter_guessed.isalpha() and len(letter_guessed) == 1 and (old_letters_guessed.count(letter_guessed) == 0)):
		return True
	elif ((len(letter_guessed) > 1) and (not letter_guessed.isalpha())):
		return False
	elif (not letter_guessed.isalpha()):	
		return False
	elif (len(letter_guessed) > 1):
		return False
	elif (old_letters_guessed.count(letter_guessed) != 0 or old_letters_guessed.count(letter_guessed.upper) != 0):
		return False		

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""
	add to the list is that needed
	:param letter_guessed: the guess of player
	:param old_letters_guessed: the list
	:type old_letters_guessed: list
	:type letter_guessed: int/ string/ else
	:return: true or false
	"""
	global old_letters_guessed_start
	if (check_valid_input(letter_guessed, old_letters_guessed) == True):
		old_letters_guessed.append(letter_guessed)
		return True
	else:
		print ("\tX")
		old_letters_guessed.sort()
		#str1 = " -> ".join(map(str, old_letters_guessed))
		str1 = " -> ".join(old_letters_guessed)
		print ('\t' + 'this is the letters you already geusses:\t' + str1)
		print ("\tFalse")	
		return False	

def show_hidden_word(secret_word, old_letters_guessed):
	"""
	return new stirng with the the right chars and the 
	other is _
	:param secret_word: the word hes need to find
	:paran old_letters_guessed: the list of the chars 
	type secret_word: str
	type old_letters_guessed: list
	return: str	
	"""
	global old_letters_guessed_start
	str2 = ''
	for char in secret_word:
		if (char in old_letters_guessed):
			str2 = str2 + char + ' '
		else:
			str2 = str2 + '_ '
	return str2		

def check_win(secret_word, old_letters_guessed):
	"""
	check if the player is winning
	:paran secret_word: word
	:param old_letters_guessed: list
	:type secret_word: str
	:type old_letters_guessed: list
	:return: True OR False
	"""
	global old_letters_guessed_start
	for i in secret_word:
		if (i not in old_letters_guessed):
			return False
		else:
			continue
	return True

def print_hangman(num_of_tries):
	"""
	print the situasion of hangman
	:param num_of_tries: num of fail tries
	:type num_of_tries: int
	:return ascii art
	"""
	HANGMAN_PHOTOS = {"1": """x-------x""", "2": """x-------x\n|\n|\n|\n|\n|""", 
	"3": """x-------x\n|\t|\n|\t0\n|\n|\n|""", "4": """x-------x\n|\t|\n|\t0\n|\t|\n|\n|""",
	"5": """x-------x\n|\t|\n|\t0\n|      /|\ \n|\n|""", "6": """x-------x\n|\t|\n|\t0\n|      /|\ \n|      /\n|""",
	"7": """x-------x\n|\t|\n|\t0\n|      /|\ \n|      / \ \n|"""}
	
	if (num_of_tries == 1):
		print(HANGMAN_PHOTOS["1"])
	elif (num_of_tries == 2):
		print(HANGMAN_PHOTOS["2"])
	elif (num_of_tries == 3):
		print(HANGMAN_PHOTOS["3"])
	elif (num_of_tries == 4):
		print(HANGMAN_PHOTOS["4"])	
	elif (num_of_tries == 5):
		print (HANGMAN_PHOTOS["5"])
	elif (num_of_tries == 6):
		print(HANGMAN_PHOTOS["6"])
	elif (num_of_tries == 7):
		print(HANGMAN_PHOTOS["7"])	
	return None
	
def choose_word(file_path, index):
	"""
	return the secret word and the number of equal word in the file
	:param file_path: the file
	:param index: the index of secret word
	:type file_info: file
	type index: int
	:return: tuple
	"""
	file = open(file_path, "r")
	file_info = file.read()
	list_for_now = file_info.split()
	len_file = len(list_for_now)
	len_for_after = len_file #this is for the loop after
	old_words = []
	for word in list_for_now:
		if (list_for_now.count(word) > 1 and word not in old_words):
			number = list_for_now.count(word)
			len_file = len_file - number + 1
		old_words.append(word)
	if (index > len_for_after):
		while index > len_for_after:
			index = index - len_for_after
	index = index - 1
	word_back = list_for_now[index]
	new_tuple = (len_file, word_back)
	file.close()
	return word_back

def openning_game(hello):
	"""
	return the openning screen
	:param hello: random
	type hello: random
	return: str
	"""
	HANGMAN_ASCII_ART = ("""welcome to the game hangman\n
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")
	print (HANGMAN_ASCII_ART)
	
def main():	
	MAX_TRIES = 6
	num_of_tries = 1
	old_letters_guessed_start = []
	openning_game(True)
	#file_address = input("insert a file path that lead for file of random words:\t")	
	file_address = r"C:\\Users\\oesch\\OneDrive\\Desktop\\Software\\python program\\word.txt"#this is a stock of word
	index_secret_word = int(input("input a random number, it will represent the locaision of the secret word:\t\n"))
	print ("we are going to start, are you exiting? first this is your starting position:\n")
	print_hangman(num_of_tries)
	secret_word = choose_word(file_address, index_secret_word)
	print ('\n\tthe secret word is:\t' + show_hidden_word(secret_word, old_letters_guessed_start) + ' ')
	while num_of_tries <= MAX_TRIES:
		that_my_try = input("\n\twhich letter do you think is correct?\t")
		num_of_tries += 1
		if (check_win(secret_word, old_letters_guessed_start) == True):
			print ("\tWIN\n")
			break
		elif (that_my_try in old_letters_guessed_start):
			print ('\n\tX\n')
			num_of_tries -= 1
		elif (is_valid_input(that_my_try) == False):
			print ('\n\tX\n')
			num_of_tries -= 1
		elif (try_update_letter_guessed(that_my_try, old_letters_guessed_start) == True and that_my_try in secret_word):
			print ("\n\tnice! you right!\n\tthis is your posion now:")
			print ('\t' + show_hidden_word(secret_word, old_letters_guessed_start))
			if (check_win(secret_word, old_letters_guessed_start) == True):
				print ("\tWIN\n")
				break
		elif (try_update_letter_guessed(that_my_try, old_letters_guessed_start) == False):
			print ("\t):\n\n")
			print_hangman(num_of_tries)		
	if (check_win(secret_word, old_letters_guessed_start) == False):
		print ("LOSE")
		
if __name__ == "__main__":
	main()






