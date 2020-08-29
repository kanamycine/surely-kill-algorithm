tc = int(input())
for t in range(1,tc+1):
    input_num = list(input().split())
    input_list = list(input().split())
    
    zro = []
    one = []
    two = []
    thr = []
    for_ = []
    fiv = []
    six = []
    svn = []
    egt = []
    nin = []

    while(len(input_list) != 0):
        p = ''
        p = input_list.pop()
        if p == 'ZRO':
          zro.append(p)
        elif p == 'ONE':
            one.append(p)
        elif p == 'TWO':
            two.append(p)
        elif p == 'THR':
            thr.append(p)
        elif p == 'FOR':
            for_.append(p)
        elif p == 'FIV':
            fiv.append(p)
        elif p == 'SIX':
            six.append(p)
        elif p == 'SVN':
            svn.append(p)
        elif p == 'EGT':
            egt.append(p)
        elif p == 'NIN':
            nin.append(p)
    result_list = []
    for j in range(len(zro)):
        result_list.append('ZRO')
    for j in range(len(one)):
        result_list.append('ONE')
    for j in range(len(two)):
        result_list.append('TWO')
    for j in range(len(thr)):
        result_list.append('THR')
    for j in range(len(for_)):
        result_list.append('FOR')
    for j in range(len(fiv)):
        result_list.append('FIV')
    for j in range(len(six)):
        result_list.append('SIX')
    for j in range(len(svn)):
        result_list.append('SVN')
    for j in range(len(egt)):
        result_list.append('EGT')
    for j in range(len(nin)):
        result_list.append('NIN')
    
    print('#{}'.format(t))
    for k in range(len(result_list)):
        print(result_list[k], end=' ')