

# [S/W 문제해결 기본] 2일차 - Sum D3



다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV2XTaX6DVkBBASl)


**[제약 사항]**

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

**[입력]**

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

**[출력]**

\#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.



**max, min, sum 쓰지 말기**



```python
for _ in range(10):
    test_case_num = int(input())
    inputlist = [list(map(int, input().split())) for _ in range(100)]

    Hrz_sum_list = []
    vtc_sum_list = []
    sumtmp = 0
    max_list = []
    # 가로행 합 
    for i in range(100):
        for j in range(100):
            sumtmp += inputlist[i][j]
        Hrz_sum_list.append(sumtmp)
        sumtmp = 0 

    max_list.append(max(Hrz_sum_list))

    # 세로행 합
    for i in range(100):
        for j in range(100):
            sumtmp += inputlist[j][i]
        vtc_sum_list.append(sumtmp)
        sumtmp = 0 

    max_list.append(max(vtc_sum_list))


# 대각선 합
    

    for i in range(100):
        sumtmp += inputlist[i][i]
    max_list.append(sumtmp)
    sumtmp = 0

    for i in range(100):
        sumtmp += inputlist[i][99-i]
    max_list.append(sumtmp)
    sumtmp = 0

    result = max(max_list)


    print(f'#{test_case_num} {result}')
```



