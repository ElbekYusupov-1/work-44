# =============================================
# Array46: Yig'indisi R ga eng yaqin 2 ta elementni topish
# =============================================
def array46():
    n = 6
    R = 10
    massiv = [1, 3, 5, 7, 9, 2]
    
    eng_kichik_farq = float('inf')
    birinchi = 0
    ikkinchi = 0
    
    for i in range(n):
        for j in range(i+1, n):
            yigindi = massiv[i] + massiv[j]
            farq = abs(yigindi - R)
            
            if farq < eng_kichik_farq:
                eng_kichik_farq = farq
                birinchi = massiv[i]
                ikkinchi = massiv[j]
    
    print(birinchi, ikkinchi)

# array46()


# =============================================
# Array47: Takrorlanmagan elementlarni chiqarish
# =============================================
def array47():
    massiv = [7, 4, 2, 3, 1, 4, 5, 2, 4, 7]
    ko_rilgan = set()
    natija = []
    
    for son in massiv:
        if son not in ko_rilgan:
            ko_rilgan.add(son)
            natija.append(son)
    
    print(*natija)   # Natija: 7 4 2 3 1 5

# array47()


# =============================================
# Array48: Eng ko'p takrorlangan elementning soni
# =============================================
def array48():
    massiv = [7, 4, 2, 3, 1, 4, 5, 2, 4, 7, 4]
    
    from collections import Counter
    hisob = Counter(massiv)
    eng_kop = max(hisob.values())
    
    print("Eng ko'p takrorlangan sonning soni:", eng_kop)

# array48()


# =============================================
# Array49: Massiv 1 dan n gacha bo'lgan sonlardan tuzilganmi?
# =============================================
def array49():
    n = 5
    massiv = [1, 3, 2, 5, 4]   # to'g'ri misol
    
    for i in range(n):
        if massiv[i] < 1 or massiv[i] > n:
            print(i+1)   # 1-based index (qayerda xato ekanligi)
            return
    
    print(0)   # Hammasi joyida

# array49()


# =============================================
# Array50: O'ng qo'shnisidan katta bo'lgan elementlar soni
# =============================================
def array50():
    massiv = [1, 3, 2, 5, 4, 7, 6]
    sanoq = 0
    
    for i in range(len(massiv)-1):
        if massiv[i] > massiv[i+1]:
            sanoq += 1
    
    print("O'ng qo'shnisidan katta bo'lganlar soni:", sanoq)

# array50()