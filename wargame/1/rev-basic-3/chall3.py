data = bytes.fromhex("49 60 67 74 63 67 42 66 80 78 69 69 7B 99 6D 88 68 94 9F 8D 4D A5 9D 45 00 00 00 00 00 00 00 00")
data = data[:24]

result = []

for i in range(len(data)):
    # i ^ a1[i] + 2 * i = data[i]
    tmp = data[i] - 2 * i
    tmp = tmp % 256

    # i ^ a1[i] = tmp
    a1_i = tmp ^ i

    result.append(a1_i)

result = bytes(result)

print(result)