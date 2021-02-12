# Capital characters means important characters
# if capital is beside a 1, get out
 
 
 
x = int(input())
for i in range(x):
    chars = input()
    bina = input()
    dex = [x for x in range(len(chars)) if chars[x].isupper()]
    for x in dex:
        if x == 0:
            if bina[x + 1] == '1':
                print("not enough spaCe, please Bounce!")
                break
        elif x == 7:
            if bina[x - 1] == '1':
                print("not enough spaCe, please Bounce!")
                break
        elif bina[x - 1] == '1' or bina[x + 1] == '1':
            print("not enough spaCe, please Bounce!")
            break
    else:
        print("made some spaCe, welcome to the Bar!")