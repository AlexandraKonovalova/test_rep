a = []
n = 0
with open('text1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        words = line.split()
        a.append(len(words))
        if len(words) > 0:
            n += 1;
print("Average lenth is ", round(sum(a)/n, 1))
    
