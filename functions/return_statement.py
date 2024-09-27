# Return Statement

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'Two'
    elif answerNumber == 3:
        return 'Three'
    elif answerNumber == 4:
        return 'Four'
    elif answerNumber == 5:
        return 'Five'
    elif answerNumber == 6:
        return 'Six'
    elif answerNumber == 7:
        return 'Seven'
    elif answerNumber == 8:
        return 'Eight'


r = random.randint(1, 8)
print(r)
fortune = getAnswer(r)
print(fortune)