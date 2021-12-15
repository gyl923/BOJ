#11728 배열 합치기
"""
문제
정렬되어있는 두 배열 A와 B가 주어진다. 
두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 
배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

출력
첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.

예제 입력 1     예제 출력 1 
2 2             2 3 5 9
3 5
2 9

예제 입력 2     예제 출력 2 
2 1             1 4 7
4 7
1

예제 입력 3     예제 출력 3 
4 3             1 2 3 4 5 7 9
2 3 5 9
1 4 7
"""
# sol 1 / 1624ms
""" import sys
input = sys.stdin.readline

n,m = map(int, input().split())
print(*sorted(list(map(int, input().split()))+list(map(int, input().split())))) """

# sol 2 692ms

import sys
input()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))
# sys.stdin.readline == enter 기준 입력 받기?
# sys.stdin.read == enter 상관없이 ctrl z 전까지 모두 입력받기?