def findAllUnrepeatedLetters( word ):
    unrepeatedChar = set()

    for letter in word:
        if letter in unrepeatedChar:
            unrepeatedChar.remove(letter)
        else:
            unrepeatedChar.add(letter)

    print "all unrepeated letters: "
    print unrepeatedChar
    print

def findFirstUnrepeatedLetters( word ):
    unrepeatedChar = []

    for letter in word:
        if letter in unrepeatedChar:
            unrepeatedChar.remove(letter)
        else:
            unrepeatedChar.append(letter)

    print "first unrepeated letters: "
    print unrepeatedChar[0]
    print



findAllUnrepeatedLetters("racecar")
findAllUnrepeatedLetters("elephant")

findFirstUnrepeatedLetters("racecar")
findFirstUnrepeatedLetters("elephant")