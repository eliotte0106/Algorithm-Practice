'''
Find the minimun length of results for repeating alphabets.
ex)ababcdcdababcdcd : 2ababcdcd, output should be 9.
This problem is from Kakao coding test 2020.
'''



def solution(s):   
    answer = len(s)
    #compress range from 1 measurement(step)
    for step in range(1,len(s)//2+1):
        compressed = ""
        prev = s[0:step] # starting from front to step
        count = 1
        #incrementing step and compare with previous one
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                count += 1
                #if there is other string so cannot be compressed
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        #process for the remaining string
        compressed  += str(count) + prev if count >= 2 else prev
        #miminum result
        answer = min(answer,len(compressed))
    return answer

print(solution("ababcdcdababcdcd"))
 
    


 