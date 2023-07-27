import random
import sys

def generate_diceware_number() -> int:
	num = 0
	for i in range(1, 6):
		num *= 10
		num += random.randint(1, 6)

	return num

def get_word_from_wordlist(word_id: int) -> str:
	with open("eff_large_wordlist.txt", "r", newline='') as file:
		wordlist = file.readlines()

		for line in wordlist:
			id, word = line.split("\t")
			id = int(id)

			if word_id == id:
				return word.strip()


def main():
	if len(sys.argv) == 2 and sys.argv[1].isdigit():
		SIZE = int(sys.argv[1])
		password_generated = ""

		for _word in range(0, SIZE):
			word_id = generate_diceware_number()

			password_generated += get_word_from_wordlist(word_id) + " "

		print(password_generated)
	
	else:
		print("Please use: {} <size>".format(sys.argv[0]))

if __name__ == "__main__":
	main()
