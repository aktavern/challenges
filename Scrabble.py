def scrabble():
    alphabet = {
        1:['A','E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
        2:['D','G'],
        3:['B','C','M','P'],
        4:['F','H','V','W','Y'],
        5:['K'],
        8:['J','X'],
        10:['Q','Z'],
        0: [" "],
        }
    
    import re
    word = str(input("Input a word: "))
    word = word.upper()
    matched = False

    with open("Collins Scrabble Words (2015).txt","r") as file:
        for line in file:
            if re.match(word,line):
                print (word + ' is acceptable!')
                matched = True
                break
            if line == ' ' and matched == False:
                print (word + ' is not acceptable!')
                break      
    file.close();
    if matched == True:
        total = []
        for i in word:
            for values,letters in alphabet.items():
                if i in letters:
                    total.append(values)
        print('Your word is worth ', sum(total), ' points in scrabble.')
    else:
        pass
