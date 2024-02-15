# 1. feladat

naplo = {}

with open("naplo.txt", mode="r", encoding="utf-8") as fajl:

    for line in fajl:           # reading the file line by line

        #print(line.strip())

        if line[0] == '#':          # to get the date

            datum_sor = line.strip().split()
            datum_kulcs = datum_sor[1] + ' ' + datum_sor[2]
            
            naplo[datum_kulcs] = []
            
        else:                       # to get the student data (line)

            bejegyzes_sor = line.strip().split()

            naplo[datum_kulcs].append([bejegyzes_sor[0] + ' ' + bejegyzes_sor[1], bejegyzes_sor[2]])

#print(naplo)


print("2. feladat")
szamlalo = 0

for a_datum_kulcsa in naplo:

    # print(a_datum_kulcsa)
    
    szamlalo += len(naplo[a_datum_kulcsa])  # counting the number of elements

print(f'A naplóban {szamlalo} bejegyzés van.')


print("3. feladat")
igazolt = 0
igazolatlan = 0

for a_datum_kulcsa in naplo:        # iterating through the keys (in a Dictionary)
    
    for bejegyzes in naplo[a_datum_kulcsa]:     # iterating through the values (Lists) of the keys

        igazolt += bejegyzes[1].count('X')          # counting the number 'X' characters

        igazolatlan += bejegyzes[1].count('I')

print(f'Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.')


# 4. feladat

def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok",
              "pentek", "szombat"]

    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]

    napsorszam = (napszam[honap-1] + nap ) % 7

    return napnev[napsorszam]


print("5. feladat")
honap_sorszama = int(input("A hónap sorszáma="))
nap_sorszama = int(input("A nap sorszáma="))

print(f'Azon a napon {hetnapja(honap_sorszama, nap_sorszama)} volt.')

# print(hetnapja(2, 3))


print("6. feladat")

nap_neve = input("A nap neve=")
ora_sorszama = int(input("Az óra sorszáma="))

hianyzasok_szama = 0

for a_datum_kulcsa in naplo:

    if hetnapja(int(a_datum_kulcsa[:2]), int(a_datum_kulcsa[3:])) == nap_neve:      # further behaviour examination required (!)

        for bejegyzes in naplo[a_datum_kulcsa]:     # iterating through the lines of the students when a date is found

            # if (bejegyzes[1][ora_sorszama - 1] == 'X') or (bejegyzes[1][ora_sorszama - 1] == 'I'):        # this is also working

                # hianyzasok_szama += 1

            if ('X' in bejegyzes[1][ora_sorszama - 1]) or ('I' in bejegyzes[1][ora_sorszama - 1]):

                hianyzasok_szama += 1

print(f'Ekkor összesen {hianyzasok_szama} óra hiányzás történt.')


print("7. feladat")

hianyzasok = {}

for a_datum_kulcsa in naplo:        # creating a new dictionary

    for bejegyzes in naplo[a_datum_kulcsa]:

        # print(bejegyzes)

        hianyzas_db = bejegyzes[1].count('X') + bejegyzes[1].count('I')     # counting the number of 'X' characters

        # print(hianyzas_db)
        
        if bejegyzes[0] in hianyzasok:              # if the current student is in the dictionary

            hianyzasok[bejegyzes[0]] += hianyzas_db     # add to the value
            
        else:                               # if the current student is NOT in the dictionary

            hianyzasok[bejegyzes[0]] = hianyzas_db      # set the value
            

max_hianyzas = 0

for diak in hianyzasok:             

    if hianyzasok[diak] > max_hianyzas:         # if the current is greater than the maximum

        max_hianyzas = hianyzasok[diak]             # set the new maximum


print('A legtöbbet hiányzó tanulók:', end=' ')

for diak in hianyzasok:

    if hianyzasok[diak] == max_hianyzas:

        print(diak, end=' ')