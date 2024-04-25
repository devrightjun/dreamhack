# def main():
#     byte_140003000 = bytes.fromhex("AC F3 0C 25 A3 10 B7 25 16 C6 B7 BC 07 25 02 D5 C6 11 07 C5 00 00 00 00 00 00 00 00 00 00 00 00")
#     result = []
    
#     for i in range(21):
#         tmp = (byte_140003000[i])
#         tmp %= 256
#         result.append(tmp)

#     result = bytes(result)
#     print(result)

# if __name__ == "__main__":
#     main()



def main():
    byte_140003000 = bytes.fromhex(
        "AC F3 0C 25 A3 10 B7 25 16 C6 B7 BC 07 25 02 D5 C6 11 07 C5 00 00 00 00 00 00 00 00 00 00 00 00"
    )
    result = []

    for i in byte_140003000[:21]:  # 반복 범위는 21 바이트로 제한
        for candidate in range(256):  # 가능한 모든 바이트 값에 대하여
            if ((-5 * candidate) & 0xFF) == i:  # -5를 곱한 뒤, 256으로 모듈러 연산을 적용
                result.append(candidate)  # 조건을 만족하는 바이트를 결과에 추가
                break

    result = bytes(result)
    print(result)

if __name__ == "__main__":
    main()
