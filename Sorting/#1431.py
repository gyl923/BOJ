#1431 시리얼번호 
"""
문제
다솜이는 기타를 많이 가지고 있다. 그리고 각각의 기타는 모두 다른 시리얼 번호를 가지고 있다. 
다솜이는 기타를 빨리 찾아서 빨리 사람들에게 연주해주기 위해서 기타를 시리얼 번호 순서대로 정렬하고자 한다.

모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.

시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.

A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
시리얼이 주어졌을 때, 정렬해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 기타의 개수 N이 주어진다. N은 50보다 작거나 같다. 
둘째 줄부터 N개의 줄에 시리얼 번호가 하나씩 주어진다. 
시리얼 번호의 길이는 최대 50이고, 알파벳 대문자 또는 숫자로만 이루어져 있다. 시리얼 번호는 중복되지 않는다.

출력
첫째 줄부터 차례대로 N개의 줄에 한줄에 하나씩 시리얼 번호를 정렬한 결과를 출력한다.

예제 입력 1         예제 출력 1
5                   A
ABCD                ABCD
145C                Z321
A                   145C
A910                A910
Z321
 
예제 입력 2         예제 출력 2 
2                   Z20
Z19                 Z19
Z20

예제 입력 3         예제 출력 3 
4                   FIPJOTEA5
34H2BJS6N           PYF1J14TF
PIM12MD7RCOLWW09    34H2BJS6N
PYF1J14TF           PIM12MD7RCOLWW09
FIPJOTEA5

예제 입력 4         예제 출력 4 
5                   ABCDA
ABCDE               ABCDE
BCDEF               ACAAA
ABCDA               BAAAA
BAAAA               BCDEF
ACAAA
"""
'''
1.  A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
    만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 
    작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
2.  만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 
3.  숫자가 알파벳보다 사전순으로 작다.
'''
# 1 68ms
""" import sys
input = sys.stdin.readline

arr = []
num = [str(i) for i in range(10)]
n = int(input())
for i in range(n):
    cnt = 0
    line = input().rstrip()
    for j in line:
        if j in num:
            cnt += int(j)
    arr.append([line,cnt])       

arr.sort(key=lambda x:(len(x[0]),x[1],x[0]))
for i in arr:
    print(i[0])
 """
 # 2 filter() 사용
""" arr = sorted((input() for _ in range(int(input()))), key=lambda x:(len(x), sum(map(int,filter(lambda _: _ in '123456789',x))), x))
print('\n'.join(arr)) """

# 3 a.isnumeric() 사용 -> str형식안에 숫자인지 판별 // 숫자면 True 리턴
arr = sorted((input() for _ in range(int(input()))), key=lambda x:(len(x), sum([int(i) for i in x if i.isnumeric()]), x))
print('\n'.join(arr))