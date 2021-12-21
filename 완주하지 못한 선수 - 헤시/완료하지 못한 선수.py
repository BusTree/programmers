def solution(participant, completion):
    from collections import Counter
    answer = Counter(participant) - Counter(completion)
    answer = answer.most_common(1)[0][0]
    print('answer', answer)
    # 참여자, 완료자
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
result = solution(participant, completion)
print('result', result)

# 모범답안

# import collections
# def solution(participant, completion):
#   answer = collections.Counter(participant) - collections.Counter(completion)
#   return list(answer.keys())[0]

# 베운점 - 컬렉션 카운터를 응용해서 객체간에 연산이 가능하다.