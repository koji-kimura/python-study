# coding: UTF-8

s = "       test        "
s = s.strip()
print(s)

equ = "All animals are equal"
equ = equ.replace("a",'@')
print(equ)

basetxt = "Cat in the hat"

x1 = "Cat" in basetxt

x2 = "Bat" in basetxt

x3 = "Hat" in basetxt

print(x1)
print(x2)
print(x3)

fict = ["トルストイ","カミュ","オーウェル","ハクスリー","オースティン"]
fict_part = fict[0:3]
print(fict_part)