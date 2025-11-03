def longest(sen):
    longest = sen[0]
    for i in range(len(sen)):
        if len(sen[i]) > len(longest):
            longest = sen[i]
    print(longest)
    sen.remove(longest)
    print(sen)
            

sentence = (input("sentence: ").split(" "))
longest(sentence)