import cs50

text = cs50.get_string("TEXT: ")
# print(text)
count = 0
word = 1
letter = 0
sentence = 0
# test='' # a=97 z=122 A=65 Z=90

for i in range(len(text)):
    # count +=1
    ############WORD COUNT##############
    if text[i] == ' ':
        word += 1
        # print(count)

# print(ord(test))
    #############LETTER COUNT###########
    if ord(text[i]) in range(97, 123):
        # print("small")
        letter += 1
    elif ord(text[i]) in range(65, 91):
        # print("cap")
        letter += 1

    ##########SENTENCE COUNT############
    elif text[i] == '?' or text[i] == '!' or text[i] == '.':
        # print("sentence")
        sentence += 1
# print(f"letter:{letter}|| word:{word}|| sentence:{sentence}")
    ##########AVERAGE CALCULATION###############
    
    
def avg_cal(letter, word, sentence):
    avgW = 0
    avgS = 0
    index = 0

    avgW = letter/word * 100
    avgS = sentence/word * 100

    index = round(0.0588 * avgW - 0.296 * avgS - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


    # print(avgW)
    # print(avgS)
    # print(index)
avg_cal(letter, word, sentence)