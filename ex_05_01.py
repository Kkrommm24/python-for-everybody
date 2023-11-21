def Sum_day():
    sum = 0
    cnt = 0
    while True :
        sval = input("Enter a number: ")
        if sval == 'done': break
        try:
            fval = float(sval)
        except:
            print('Invalid. Try again')
            continue
        print(fval)
        sum += fval
        cnt += 1
    print(sum, cnt, sum/cnt)
Sum_day()
#???
