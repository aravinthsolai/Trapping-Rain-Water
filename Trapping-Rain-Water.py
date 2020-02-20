id = [1,0,2,1,0,1,3,2,1,2,1]
i=0
j=1
water_level=0
for x in id:
 i=i+1
 q=len(id)
 #print(i)
 #print(q)
 #print('first loop ' + str(x))
 t=[x]
 #print('initial array' + str(t))
 if i != q and i >= j:
  for y in id[i:q]:
   #print(id[i:])
   if x >= y:
    #print('child 1 loop ' + str(y))
    t.append(y)
    j=j+1
    #print('child 1 loop append' + str(t))
   if y >= x:
    #print('child 2 loop ' + str(y))
    t.append(y)
    j=j+1
    if len(t) < 3:
     t=[x]
     j=j-1
    break
 if len(t) < 3:
  t=[x]
 
 if len(t) >= 3:
  #print(t)
  while t[-1] <= t[-2] and len(t) > 2:
   #print(t)
   t.pop(-1)
  while t[0] > t[-1]:
   t.pop(0)
  t.pop(-1)
  k=t
  k.sort()
  
  for v in t:
   water_level=water_level+(k[-1]-v)
   
print(water_level)
  
  
