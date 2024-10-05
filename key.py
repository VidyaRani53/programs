inputs=[int(i) for i in input().split()]
th,h,t,o=[],[],[],[]
for i in inputs:
    th.append(i//1000)
    h.append((i//100)%10)
    t.append((i//10)%10)
    o.append((i//1)%10)
key=int(f"{min(th)}{min(h)}{min(t)}{min(o)}")
print(key)



    
    
