tc = int(input())
for t in range(1, tc+1):
    input_1 = list(input())
    input_2 = list(input())
    cnt, overlap_cnt = 0, 0

    for i in input_1:
        for j in input_2:
            if i == j:
                overlap_cnt += 1
        if overlap_cnt > cnt:
            cnt = overlap_cnt
        overlap_cnt = 0
    print("#{} {}".format(t, cnt))