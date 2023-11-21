fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname) # phải cd đến thư mục chứa file

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # idiom: retrieve/creat/update counter
        di[w] = di.get(w,0) + 1
        # print(di[w], '\n')
print(di)
max = -1
for k,v in di.items():
    print(k,v)
    if v > max:
        max = v
        the_word = k
print('Done', the_word, max)
