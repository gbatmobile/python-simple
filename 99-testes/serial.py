def genUnserial(key, begin=0):
    ecx = begin
    si = 0x0a
    si = si ^ 0x408a
    si = (si + 0x1e)                # em resumo si = 0x409e

    ecx = ((ecx - si) & 0xFFFF) + (ecx & 0xFFFF0000)

    print (f"antes ecx 1337 {ecx:08x}")

    ecx = ((ecx ^ 0x1337) + 0x50) ^ 0x02

    print (f"Ecx na saida do laco deve ser {ecx:08x}")

    while ecx != 0:
        cl  = (ecx & 0xFF) - 0x30               # add cl, 0x30
        ecx = ((ecx & 0xFFFFFF00) + cl) & 0xFFFFFFFF
        ecx = (ecx + 0x803) & 0xFFFFFFFF
        ecx = ecx ^ 0x2 ^ 0xc
        ecx = ((ecx >> 8) | (ecx << 24)) & 0xFFFFFFFF  # ror ecx, 8
        print (f"apos ultimo digito -> {ecx:08x}")
        car = ecx >> 24
        ecx = (ecx - car) & 0xFFFFFFFF
    return ecx

def genSerial(key):
    ecx = 0
    for c in key:
        ecx = ecx + ord(c)
        print (f"apos soma digito {ord(c):02x} -> {ecx:08x}")
        ecx = ((ecx << 8) + (ecx >> 24)) & 0xFFFFFFFF  # rol ecx, 8
        print (f"apos rol {ecx:08x}")
        ecx = ecx ^ 0xE   # 0xc ^ 0x2 (mantem o LSB inverte os tres seguintes)
        print (f"apos 0e {ecx:08x}")
        ecx = (ecx - 0x803) & 0xFFFFFFFF
        print (f"apos -803 {ecx:08x}")
        cl  = ((ecx & 0xFF) + 0x30) & 0xFF             # add cl, 0x30
        ecx = (ecx & 0xFFFFFF00) + cl
        print (f"apos +30 em cl {ecx:08x}")

    # Converter saida em 0xaca7, pois 0xaca7 leva para zero.

    ecx = ((ecx ^ 0x02) - 0x50) ^ 0x1337

    si = 0x0a
    si = si ^ 0x408a
    si = (si + 0x1e) & 0xFFFF   # em resumo si = 0x409e
    ecx = (ecx & 0xFFFF0000) + ((ecx + si) & 0xFFFF)
    return ecx

# while True:
#   key = input("Serial: ")
key = '111111'
#keycoded = genSerial(key)
#print (f"Serial {key} coded: {keycoded:08x}")
print ("****************")
print (f"Serial decodificado {genUnserial(key, 0x0)} ", )
