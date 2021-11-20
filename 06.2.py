import random
value1 = random.randint(0, 99)
value2 = random.randint(0, 99)
value3 = random.randint(0, 99)
value4 = random.randint(0, 99)
value5 = random.randint(0, 99)
value6 = random.randint(0, 99)
value7 = random.randint(0, 99)
value8 = random.randint(0, 99)
value9 = random.randint(0, 99)
value10 = random.randint(0, 99)
value11 = random.randint(0, 99)
value12 = random.randint(0, 99)
value13 = random.randint(0, 99)
value14 = random.randint(0, 99)
value15 = random.randint(0, 99)
value16 = random.randint(0, 99)
value17 = random.randint(0, 99)
value18 = random.randint(0, 99)
value19 = random.randint(0, 99)
value20 = random.randint(0, 99)

def First():
    print (f"{value1} + {value2}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value1 + value2:
        Answer = 1
    else:
        Answer = 0
    return Answer

def Second():
    print (f"{value3} + {value4}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value3 + value4:
        Answer = 1
    else:
        Answer = 0
    return Answer

def Third():
    print (f"{value5} + {value6}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value5 + value6:
        Answer = 1
    else:
        Answer = 0
    return Answer

def Fourth():
    print (f"{value7} + {value8}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value7 + value8:
        Answer = 1
    else:
        Answer = 0
    return Answer

def Fifth():
    print (f"{value9} + {value10}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value9 + value10:
        Answer = 1
    else:
        Answer = 0
    return Answer

def Sixth():
    print (f"{value11} + {value12}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value11 + value12:
        Answer = 1
    else:
        Answer = 0
    return Answer
    
def Seventh():
    print (f"{value13} + {value14}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value13 + value14:
        Answer = 1
    else:
        Answer = 0
    return Answer

def Eighth():
    print (f"{value15} + {value16}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value15 + value16:
        Answer = 1
    else:
        Answer = 0
    return Answer

def Ninth():
    print (f"{value17} + {value18}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value17 + value18:
        Answer = 1
    else:
        Answer = 0
    return Answer
    
def Tenth():
    print (f"{value19} + {value20}")
    Answer = int(input ('Enter your answer: '))
    if Answer == value19 + value20:
        Answer = 1
    else:
        Answer = 0
    return Answer

def Overall(One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten):
    Score = One + Two + Three + Four + Five + Six + Seven + Eight + Nine + Ten
    return Score

def Output(Score):
    print (f'Your score is {Score}/10')

One = First()
Two = Second()
Three = Third()
Four = Fourth()
Five = Fifth()
Six = Sixth()
Seven = Seventh()
Eight = Eighth()
Nine = Ninth()
Ten = Tenth()
Score = Overall(One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten)
Final = Output(Score)