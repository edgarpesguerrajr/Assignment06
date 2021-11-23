def FirstSecondThirdFourth():
    FirstNumber = float(input("ENTER YOUR FIRST NUMBER: "))
    SecondNumber = float(input("ENTER YOUR SECOND NUMBER: "))
    ThirdNumber = float(input("ENTER YOUR THIRD NUMBER: "))
    FourthNumber = float(input("ENTER YOUR FOURTH NUMBER: "))
    return FirstNumber, SecondNumber, ThirdNumber, FourthNumber

def UnoDosTresKwatro(First, Second, Third, Fourth):
    # 1234
    if First >= Second and First >= Third and First >= Fourth:
        if Second >= Third and Second >= Fourth:
            if Third >= Fourth:
              Min = First, Second, Third, Fourth

    # 1243
    if First >= Second and First >= Third and First >= Fourth:
        if Second >= Third and Second >= Fourth:
            if Fourth >= Third:
              Min = First, Second, Fourth, Third
    
    # 1324
    if First >= Second and First >= Third and First >= Fourth:
        if Third >= Second and Third >= Fourth:
            if Second >= Fourth:
              Min = First, Third, Second, Fourth

    # 1342
    if First >= Second and First >= Third and First >= Fourth:
        if Third >= Second and Third >= Fourth:
            if Fourth >= Second:
              Min = First, Third, Fourth, Second

    # 1423
    if First >= Second and First >= Third and First >= Fourth:
        if Fourth >= Third and Fourth >= Second:
            if Second >= Third:
              Min = First, Fourth, Second, Third

    # 1432
    if First >= Second and First >= Third and First >= Fourth:
        if Fourth >= Third and Fourth >= Second:
            if Third >= Second:
              Min = First, Fourth, Third, Second
   
    # 2134
    if Second >= First and Second >= Third and Second >= Fourth:
        if First >= Third and First >= Fourth:
            if Third >= Fourth:
                Min = Second, First, Third, Fourth
    
    # 2143
    if Second >= First and Second >= Third and Second >= Fourth:
        if First >= Third and First >= Fourth:
            if Fourth >= Third:
                Min = Second, First, Fourth, Third
    
    # 2314
    if Second >= First and Second >= Third and Second >= Fourth:
        if Third >= First and Third >= Fourth:
            if First >= Fourth:
                Min = Second, Third, First, Fourth
    
    # 2341
    if Second >= First and Second >= Third and Second >= Fourth:
        if Third >= First and Third >= Fourth:
            if Fourth >= First:
                Min = Second, Third, Fourth, First
    
    # 2413
    if Second >= First and Second >= Third and Second >= Fourth:
        if Fourth >= Third and Fourth >= First:
            if First >= Third:
                Min = Second, Fourth, First, Third
    
    # 2431
    if Second >= First and Second >= Third and Second >= Fourth:
        if Fourth >= Third and Fourth >= First:
            if Third >= First:
                Min = Second, Fourth, Third, First

    # 3124
    if Third >= First and Third >= Second and Third >= Fourth:
        if First >= Second and First >= Fourth:
            if Second >= Fourth:
                Min = Third, First, Second, Fourth
    
    # 3142
    if Third >= First and Third >= Second and Third >= Fourth:
        if First >= Second and First >= Fourth:
            if Fourth >= Second:
                Min = Third, First, Fourth, Second
    
    # 3214
    if Third >= First and Third >= Second and Third >= Fourth:
        if Second >= First and Second >= Fourth:
            if First >= Fourth:
                Min = Third, Second, First, Fourth
   
    # 3241
    if Third >= First and Third >= Second and Third >= Fourth:
        if Second >= First and Second >= Fourth:
            if Fourth >= First:
                Min = Third, Second, Fourth, First
    
    # 3412
    if Third >= First and Third >= Second and Third >= Fourth:
        if Fourth >= First and Fourth >= Second:
            if First >= Second:
                Min = Third, Fourth, First, Second
        
    # 3421
    if Third >= First and Third >= Second and Third >= Fourth:
        if Fourth >= First and Fourth >= Second:
            if Second >= First:
                Min = Third, Fourth, Second, First

    # 4123
    if Fourth >= First and Fourth >= Second and Fourth >= Third:
        if First >= Second and First >= Third:
            if Second >= Third:
                Min = Fourth, First, Second, Third

    # 4132
    if Fourth >= First and Fourth >= Second and Fourth >= Third:
        if First >= Second and First >= Third:
            if Third >= Second:
                Min = Fourth, First, Third, Second
    # 4213
    if Fourth >= First and Fourth >= Second and Fourth >= Third:
        if Second >= First and Second >= Third:
            if First >= Third:
                Min = Fourth, Second, First, Third

    # 4231
    if Fourth >= First and Fourth >= Second and Fourth >= Third:
        if Second >= First and Second >= Third:
            if Third >= First:
                Min = Fourth, Second, Third, First

    # 4312
    if Fourth >= First and Fourth >= Second and Fourth >= Third:
        if Third >= First and Third >= Second:
            if First >= Second:
                Min = Fourth, Third, First, Second

    # 4321
    if Fourth >= First and Fourth >= Second and Fourth >= Third:
        if Third >= First and Third >= Second:
            if Second >= First:
                Min = Fourth, Third, Second, First
    
    return Min

First, Second, Third, Fourth = FirstSecondThirdFourth()
Min = UnoDosTresKwatro(First, Second, Third, Fourth)
print (f'The sequence is {Min}.')