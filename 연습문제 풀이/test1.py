def check(str):
    c = str[0]
    case = 0 # 0일 경우 D나 E, 1일 경우 F, 2일 경우 F또는 G 또는 D,E
    for i in range(1,len(str)+1):
        if case == 0:
            if c!= 'D' and c != 'E':
                return "NO"
            elif i!= len(str):
                c=str[i]
                case =1
            else:
                return "NO"
        elif case ==1:
            if c!='F':
                return "NO"
            elif i!= len(str):
                c=str[i]
                case =2
            else:
                return "NO"
        elif case ==2:
            if c== 'G' and i == len(str):
                return "Yes"
            elif (c== 'D' or c== 'E') and i != len(str):
                c=str[i]
                case = 1
            elif c=='F'and i != len(str):
                c=str[i]
                case =2
            else:
                return "NO"


def Slump(*strs):
    result = []
    for str in strs:
        result.append(check(str))
    return result

print(Slump("DFG","EFG","DFFFFFG","DFDFDFDFG","DFEFFFFFG"))
print(Slump("DFEFDG","EFAHG","DEFG","DFEFG","EFFFFDG"))

