while True :
    massage = input()
    # 프로그램 종료
    if massage == "." :
        break
    bracket = []
    result = True
  
    for i in massage :
        # "(" 일때,
        if i == "(" :
            bracket.append("(")
        # "[" 일때,
        elif i == "[" :
            bracket.append("[")
        # ")" 일때,
        elif i == ")" :
            if not bracket or bracket[-1] == "[" :
                result = False
                break
            elif bracket[-1] == "(":  bracket.pop()
        # "]" 일때,
        elif i == "]" :
            if not bracket or bracket[-1] == "(" :
                result = False
                break
            elif bracket[-1] == "[" : bracket.pop()

    if result == True and not bracket :
        print("yes")
    else : 
        print("no")