in2 = [[0.5, 6], [0.5, 7], [0.5, 4], [0.5, 9], [0.5, 9]]
out = []
for j in range(2):
    min = in2[0][1]
    min2 = in2[0]
    for i in range(len(in2)):
        if(in2[i][1] < min):
            min = in2[i][1]
            min2 = in2[i]
    print(min2)
    in2.remove(min2)
    out.append(min2)
    print(in2)
print(out)