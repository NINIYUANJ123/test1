a = input("请输入一个四位的整数:")
b = []
for i in range(len(a)):
    b.append((int(a[i]) + 5) % 10)
b[1 - 1], b[4 - 1] = b[4 - 1], b[1 - 1]
b[2 - 1], b[3 - 1] = b[3 - 1], b[2 - 1]
print("转换后的四位数%d\n" % (b[0] * 1000 + b[1] * 100 + b[2] * 10 + b[3]))
