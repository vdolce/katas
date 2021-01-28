# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
	arr = text.split()
	return' '.join(list(map(lambda w: w[1:] + w[0] + 'ay' if w.isalpha() else w, arr)))

print(pig_it('Pig latin is cool u'))
print(pig_it('Hello world !'))
