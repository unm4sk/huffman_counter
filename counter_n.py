from collections import Counter
cnt = 0
c = Counter()
for letter in list(input().lower()):
    c[letter]+=1
    cnt+=1
for key,value in c.most_common():
    print(key, value, round((value/cnt),2))
print(f"Всего букв: {cnt}")   
