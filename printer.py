wo = open("common.txt", "r")

wor = []
for word in wo:
    wor.append(wo.readline().strip('\n'))
words = []
for word in wor:
    if not len(word) <= 3:
        words.append(word)

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
        input2 = input('Input the surrounding letters separated by a space.\n')
        if not (',' in input2):
            temp2 = []
            gene = words
            for i in range(len(words)):
                for letter in input2.lower().replace(' ', ''):
                    gene[i].replace(letter, '')
                if gene[i] == '':
                    temp2.append(words[i])
            words = temp2
            print('Word list complete. Words:')
            print(words)
        else:
            print('No commas.')

