open_list = ["[","{","("]
close_list = ["]","}",")"]
showStr = lambda list : ''.join(map(str, list)) #ทำlist เป็น string

def check(expr):
    stackOpen = []
    stackClose = []
    for ori in expr:
        if ori in open_list:
            stackOpen.append(ori)
        if ori in close_list:
            stackClose.append(ori)
        else:
            pass
    stackClose.reverse()
    checkIndexO   = len(stackOpen)
    checkIndexC   = len(stackClose)
    if stackOpen == [] and stackClose != []:
        stackClose.reverse()
        print(f'{showStr(stackClose)} close paren excess')
        exit()
    if stackClose == [] and stackOpen != []:
        print(f'{showStr(stackOpen)} open paren excess   {len(stackOpen)} : {showStr(stackOpen)}')
        exit()
    while stackClose and stackOpen != []:
        for o in stackOpen:
            for c in stackClose:
                if o == "["  and c == "]" :
                    stackOpen.pop(o.index("["))
                    stackClose.pop(c.index("]"))
                elif o == "("  and c == ")" :
                    stackOpen.pop(o.index("("))
                    stackClose.pop(c.index(")"))
                elif o == "{"  and c == "}" :
                    stackOpen.pop(o.index("{"))
                    stackClose.pop(c.index("}"))
                elif (checkIndexC == (len(stackClose))) and (checkIndexO == (len(stackOpen)))  :
                    print
                    exit()(f'{expr} Unmatch open-close')
        if stackOpen == [] and stackClose != []:
           print(f'{expr} close paren excess')
           exit()
        if stackClose == [] and stackOpen != []:
           print(f'{expr} open paren excess   {len(stackOpen)} : {showStr(stackOpen)}')
           exit()
        else:
            print(f'{expr} MATCH')
            exit()
inPut = str(input("Enter expresion : "))
check(inPut)