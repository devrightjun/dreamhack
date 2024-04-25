def main():
    data = bytes.fromhex("24 27 13 C6 C6 13 16 E6 47 F5 26 96 47 F5 46 27 13 26 26 C6 56 F5 C3 C3 F5 E3 E3 00 00 00 00 00")
    result = []

    for i in range(28):
        tmp = (data[i] << 4) | (data[i] >> 4)
        tmp %= 256

        result.append(tmp)

    result = bytes(result)
    print(result)

if __name__ == "__main__":
    main()