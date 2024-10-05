from collections import Counter
def is_stable(num):
    count=Counter(str(num))
    values=list(count.values())
    return len(set(values))==1
def password(p):
    stable=[]
    unstable=[]
    for i in p:
        if is_stable(i):
            stable.append(i)
        else:
            unstable.append(i)
    return max(stable)-min(unstable)

inputs=[]
for i in range(1,6):
    inputs.append(int(input('enter input'+str(i)+':')))
print(password(inputs))
