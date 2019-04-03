def hangman(word):
    d = {}
    word2 = word
    complexity = 10
    word = list(word)
    for index,ch in enumerate(word):
        if ch in d.keys():
            d[ch].append(index)
        else:
            d[ch] = [index]
        word[index] = '_'
    while bool(d):
        if complexity == 0:
            print("You lose")
            return
        print(str(word))
        print("Pick a letter:")
        ch = input('-->')
        if ch in d.keys():
            for index in d[ch]:
                word[index] = ch
            del d[ch]
        else:
            print("Incorrect")
        complexity -= 1
    print(word2)
    return

