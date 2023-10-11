def find(l):
    outer=[[]]
    for i in l:
        n = len(outer)
        for j in range(n):
            internal = outer[j].copy()
            internal.append(i)
            outer.append(internal)
    # for i in outer:
    #     for j in range(len(i)):
    #         if l[j]!=i[j]:
    #             outer.remove(i)
    #             break
    return outer
l = [1,2,3,4]
print(find(l))