def solution(s0, s1, line, k):
    answer = []
    return answer


""" 문제 설명
'0'과 '1'로만 이루어진 세 개의 문자열 s0, s1, line이 있습니다. 이제부터 다음과 같은 과정을 문자열 line에 대한 문자열 변환으로 정의합니다.

line의 모든 '0'을 s0으로 치환하고, 모든 '1'을 s1으로 치환합니다.
예를 들어, line = "110", s0 = "1001", s1 = "010" 인 경우, line에 문자열 변환을 적용하면 "0100101001"이 됩니다. (line의 모든 '1'이 "010" 으로 바뀌고, 모든 '0'이 "1001"로 바뀌었습니다.)

3개의 문자열 s0, s1, line, 그리고 정수 k가 매개변수로 주어집니다. line에 문자열 변환을 k번 적용했을 때, 다음 두 가지 경우의 수를 구하여 배열에 담아 return 하도록 solution 함수를 완성해주세요. 단, 경우의 수가 너무 커질 수 있으므로, 경우의 수를 107 + 19 로 나눈 나머지를 return 해주세요.

임의의 두 인덱스를 뽑았을 때, 왼쪽 인덱스의 값은 0이고 오른쪽 인덱스의 값은 1인 경우의 수.
예를 들어, "10110" 에는 총 2개의 경우의 수가 있습니다. ((1, 2), (1, 3))
임의의 두 인덱스를 뽑았을 때, 왼쪽 인덱스의 값은 1이고 오른쪽 인덱스의 값은 0인 경우의 수.
예를 들어, "10110" 에는 총 4개의 경우의 수가 있습니다. ((0, 1), (0, 4), (2, 4), (3, 4))
다음은 위 예시를 돕기 위하여 인덱스별로 "10110"의 값을 나타낸 표입니다.

인덱스	0	1	2	3	4
값	1	0	1	1	0
제한 사항
s0, s1, line은 '0'과 '1'로만 이루어진 문자열입니다.
s0, s1, line의 길이는 1 이상 10만 이하입니다.
k는 1 이상 1015 이하의 자연수입니다.
입출력 예
s0	s1	line	k	result
"1001"	"001"	"1110"	1	[26,14]
"00"	"11"	"101"	3	[64,64]
"1"	"111"	"1010"	2	[0,0]
입출력 예 설명
입출력 예 #1
10011001001100110010011001100100100110011001001
line에 문자열 변환을 1번 적용하면 1110의 각 '0'이 "1001"로 바뀌고 '1'이 "001"로 바뀌어서 "0010010011001"이 됩니다. 다음은 "0010010011001"의 인덱스별 값을 나타낸 표입니다.
인덱스	0	1	2	3	4	5	6	7	8	9	10	11	12
값	0	0	1	0	0	1	0	0	1	1	0	0	1
왼쪽 인덱스의 값이 0이고 오른쪽 인덱스의 값이 1인 경우는 다음과 같이 26가지입니다.
(0, 2), (0, 5), (0, 8), (0, 9), (0, 12), (1, 2), (1, 5), (1, 8), (1, 9), (1, 12), (3, 5), (3, 8), (3, 9), (3, 12), (4, 5), (4, 8), (4, 9), (4, 12), (6, 8), (6, 9), (6, 12), (7, 8), (7, 9), (7, 12), (10, 12), (11, 12)
왼쪽 인덱스의 값이 1이고 오른쪽 인덱스의 값이 0인 경우는 다음과 같이 14가지입니다.
(2, 3), (2, 4), (2, 6), (2, 7), (2, 10), (2, 11), (5, 6), (5, 7), (5, 10), (5, 11), (8, 10), (8, 11), (9, 10), (9, 11)
입출력 예 #2

이 예시에서는 line에 문자열 변환을 3번 적용해야 합니다. line은 "101" ⇒ "110011" ⇒ "111100001111" ⇒ "111111110000000011111111" 이 됩니다.
두 경우 모두 다 64가지임을 알 수 있습니다.
입출력 예 #3

이 예시에서는 line에 문자열 변환을 2번 적용해야 합니다. line은 "1010" ⇒ "11111111" ⇒ "111111111111111111111111" 이 됩니다.
이 문자열에는 '0'이 없으므로, 두 경우 모두 경우의 수가 0입니다. """