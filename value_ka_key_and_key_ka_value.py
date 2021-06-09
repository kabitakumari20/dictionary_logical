# a={1:"kabita",2:"manvi",3:"mahi",4:"durga"}
# c=[]
# d=[]
# for key in a:
#     c.append(key)
#     d.append(a[key])
#     di={d[key]:c[key] for key in range(len(c))}
# print(di)




a={1:"kabita",2:"manvi",3:"mahi",4:"durga"}
c=[]
d=[]
for key in a:
    c.append(key)
    d.append(a[key])
    dic={}
    i=0
    while i<len(d):
        dic[d[i]]=c[i]
        i=i+1
print(dic)
