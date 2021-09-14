import random

com = []
com = random.sample(range(1, 10), 3)
print(com)

t_cnt = 0
s_cnt = 0
b_cnt = 0

while(s_cnt < 3):
    
    s_cnt = 0
    b_cnt =0
    
    num = list(map(int,input('숫자 3개를 입력하세요(띄어쓰기로 구분) : ').split()))

    for i in range(0, 3):
        for j in range(0, 3):
            if (com[i] == num[j] and i==j):
                s_cnt +=1
            elif (com[i] == num[j] and i!=j):
                b_cnt +=1
    if(s_cnt == 0 and b_cnt == 0):
        print('OUT')
    else:
        print(f'{s_cnt}S, {b_cnt}B')
    t_cnt += 1 

print(f'입력횟수 : {t_cnt}')
