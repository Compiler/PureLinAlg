from plotting import plot
from image import file2image

def Identity(S): return {z for z in S}
def Translate(x, y, S): return {(x + y*1j) + z for z in S}
def Scale(sz, S): return {z * sz for z in S}
def Rotate(d, S): return {-1j * z for z in S}
S = {2+2j, 3+2j, 1.75 + 1j, 2+1j, 2.25 + 1j, 2.5+1j, 2.75 + 1j, 3+1j, 3.25 + 1j}

#plot({((1+2j+z) * 0.5) * -1j for z in S}, 4)
#plot(Translate(1, 2, S), 4)
#plot(Rotate(1, S), 4)

S = file2image('img01.png')
print(S[0][0])
plot({ y * 1j + x for y in range(len(S)) for x in range(len(S[0])) if S[len(S) - y - 1][x][1] < 120}, len(S))
