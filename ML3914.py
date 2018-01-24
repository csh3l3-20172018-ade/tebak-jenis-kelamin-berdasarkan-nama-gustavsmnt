nama = raw_input("Masukkan Nama : ")
print(nama)
cewek = 0
cowok = 0
name=list(nama)

for x in name:
    if x=="a" or x=="i" or x=="u" or x=="e" or x=="t" or x=="l" :
        cewek = cewek + 1
    elif x=="b" or x=="d" or x=="o" :
        cowok = cowok + 1

if cowok > cewek :
    print("Cowok")
elif cewek > cowok :
    print("Cewek")

