import random
list = []
for i in range(0,200):
    list.append((i,''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))))
for j,k in list:
    print(j,k)