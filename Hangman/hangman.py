import random
from words import words
from time import sleep

word=random.choice(words)

def wait():
	for i in range(5):
		print('.',end=' ')
		sleep(.5)
	print()

print('I have guessed a ',len(word),'letters word')

wait()

right=['_']*len(word)
wrong=[]
used_letters=[]

def update():
	for i in right:
		print(i,end=' ')
	print()

update()



while True:	
	print("==========================")
	life=6
	guess=input('Guess the character:')
	print('let me check')
	wait()
	if guess in word:
		index=0
		for i in word:
			if i==guess:
				right[index]=guess
			index+=1
		update()
		if '_' not in right:
			print('You win')
			break
		if guess not in used_letters:
			used_letters.append(guess)
		else:
			print('You already used that')
	else:
		if guess not in wrong:
			wrong.append(guess)
		else:
			print('You already guess that')
		print('wrong')

		if len(wrong)>life:
			print('You lose')
			print("I choosed: ",word)
			break

	