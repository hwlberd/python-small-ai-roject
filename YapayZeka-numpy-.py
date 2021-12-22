def mainFunction():
    import numpy as np

    text_file = open("dosya.txt", "r")
    lines = text_file.read().split('\n')

    text_file.close()

    lines = np.loadtxt("dosya.txt", unpack=False)
    m1sat = int(lines[0])
    m1süt = int(lines[1])

    matris1 = [[0 for x in range(m1sat)] for y in range(m1süt)]

    x = 2;
    for i in range(m1sat):
        for j in range(m1süt):
            matris1[i][j] = lines[x]
            x = x + 1

    print("matris1")
    print("")
    print(matris1)
    print("")
    print("")

    m2sat = int(lines[x])
    m2süt = int(lines[x])

    x = x + 1

    matris2 = [[0 for x in range(m2sat)] for y in range(m2süt)]

    for i in range(m2sat):
        for j in range(m2süt):
            matris2[i][j] = lines[x]
            x = x + 1

    print("matris2")
    print("")
    print(matris2)
    print("")
    print("")
    sonucuHesapla(m1sat, m2sat, m1süt, m2süt, matris1, matris2)


def sonucuHesapla(m1sat, m2sat, m1süt, m2süt, matris1, matris2):
    satsay = m1sat - m2sat + 1
    sütsay = m1süt - m2süt + 1

    sonucmat = [[0 for x in range(satsay)] for y in range(sütsay)]

    x = 0
    y = 0
    for i in range(satsay):
        for j in range(sütsay):
            sonucmat[i][j] = matris1[i][j] * matris2[x][y] + matris1[i][j + 1] * matris2[x][y + 1] + matris1[i][j + 2] * \
                             matris2[x][y + 2] + matris1[i + 1][j] * matris2[x + 1][y] + matris1[i + 1][j + 1] * \
                             matris2[x + 1][y + 1] + matris1[i + 1][j + 2] * matris2[x + 1][y + 2] + matris1[i + 2][j] * \
                             matris2[x + 2][y] + matris1[i + 2][j + 1] * matris2[x + 2][y + 1] + matris1[i + 2][j + 2] * \
                             matris2[x + 2][y + 2]

        print("")
        print("Matris Son ")
        print(sonucmat)


mainFunction()
