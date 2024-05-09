wo = open("common.txt", "r")

wor = []
for word in wo:
    wor.append(wo.readline().strip('\n'))
words = []
for word in wor:
    if not len(word) <= 3:
        words.append(word)

alpha = "abcdefghijklmnopqrstuvwxyz"
alphabet = [letter for letter in alpha]

while True:
    inputs = input('Input middle letter:\n')
    if len(inputs) > 1:
        print('One letter.')
    else:
        temp = []
        for word in words:
            if inputs.lower() in word:
                temp.append(word)
        words = sorted(temp, key=len)[::-1]
        counter = 0
        while counter <= 5:
            input2 = input('Input the surrounding letters one by one.\n')
            alphabet.remove(input2.lower())
            counter += 1
        print(alphabet)
        for word in words:
            for letter_left in alphabet:
                if letter_left in word:
                    words.remove(word)
                    #print(word)
        print(words)
