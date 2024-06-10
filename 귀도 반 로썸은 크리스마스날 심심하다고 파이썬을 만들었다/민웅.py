# 6568_귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다.
import sys
input = sys.stdin.readline

while True:
    base = []
    is_end = False
    for i in range(32):
        tmp = input().strip()
        base.append(tmp)
        if not tmp:
            is_end = True
            break
    if is_end:
        break
        
    adder = 0
    pc = 0

    while True:
        tmp = base[pc]
        o_type = tmp[:3]
        address = tmp[3:]

        # 5비트짜리
        pc = (pc + 1) % 32
        o_type = int(o_type, 2)
        # print(tmp, o_type, address)
        if o_type == 0:
            base[int(address, 2)] = bin(adder)[2:].zfill(8)
        elif o_type == 1:
            adder = base[int(address, 2)]
            adder = int(adder, 2)
        elif o_type == 2:
            if adder == 0:
                pc = int(address, 2)
        elif o_type == 3:
            continue
        elif o_type == 4:
            adder -= 1
        elif o_type == 5:
            adder += 1
        elif o_type == 6:
            pc = int(address, 2)
        else:
            break

        # 8비트짜리
        adder = adder % 256

    print(bin(adder)[2:].zfill(8))
