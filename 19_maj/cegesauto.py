# 1. feladat
# Open the file then store data

file = open('autok.txt', mode='r', encoding='utf-8')

lista = []
for line in file:

    #print(line)
    
    lista.append(line.strip('\n'))
    
#print(lista)


# To store a List in a List
new_list = []

for line in lista:
    
    sor = line.strip().split()

    new_list.append(sor)

    #print(line)

#print(new_list)


print('2. feladat')

rendszam = ""
nap = ""

for iterator in new_list:

    #print(iterator)
    if iterator[5] == "0":
        
        rendszam = iterator[2]
        nap = iterator[0]

print(f'{nap}. nap rendszám: {rendszam}')


print('\n3. feladat')

#bekert_nap = 4
bekert_nap = int(input('Nap: '))

print(f'Forgalom a(z) {bekert_nap}. napon:')

for sor in new_list:

    if int(sor[0]) == bekert_nap:   # if the day matches

        #print(sor)
        if sor[5] == "0":

            jelenlet = "ki"

        if sor[5] == "1":

            jelenlet = "be"

        print(sor[1], sor[2], sor[3], jelenlet)


print('\n4. feladat')

auto_kint = 0

for sor in new_list:

    if sor[5] == "0":       # the car is out

        auto_kint += 1

    if sor[5] == "1":       # the car is in

        auto_kint -= 1

print(f'A hónap végén {auto_kint} autót nem hoztak vissza.')


print('\n5. feladat')

for x in range(0, 10):      # to iterate through all the cars

    kezdo_km = 0
    veg_km = 0
    rendszam = "CEG30" + str(x)         # using the for loop for this value

    for line in new_list:       # iterate through the List every time

        if line[2] == rendszam:     # if the actual car is found

            if kezdo_km == 0:

                kezdo_km = int(line[4])

            veg_km = int(line[4])

    # print(kezdo_km)
    # print(veg_km)

    print(rendszam, veg_km - kezdo_km, "km")    # how many kilometres the actual car has travelled in this month


print('\n6. feladat')

legnagyobb_km = 0
max_sofor_id = 0

sor_szamlalo = 0            # to count the number of lines

for line in new_list:

    if line[5] == "1":      # if the car is brought back in

        for sor_vissza in range( (sor_szamlalo), 0, -1):   # further behaviour examination required (!)

            # print(sor_vissza)
            
            sorok = new_list[sor_vissza]    # (iterating through a list backwards)
            # print(sorok[5])

            if (str(sorok[5]) == "0") and (sorok[2] == line[2]):        # (if the car is out and the driver is the same)

                tavolsag_kiszamolt = int(line[4]) - int(sorok[4])
                #print(line[3], line[2], tavolsag_kiszamolt)

                if tavolsag_kiszamolt > legnagyobb_km:

                    legnagyobb_km = tavolsag_kiszamolt
                    max_sofor_id = line[3]
                
                break

    sor_szamlalo += 1

print(f'Leghosszabb út: {legnagyobb_km} km, személy: {max_sofor_id}')


print('\n7. feladat')

# bekert_rendszam = "CEG304"
bekert_rendszam = input('Rendszám: ')

file_export = open(f'{bekert_rendszam}_menetlevel.txt', mode='w', encoding='utf-8')     # to create a new file (with F-string)


for sor in new_list:

    if sor[2] == bekert_rendszam:

        if sor[5] == "0":           # the car is out
            
            print(sor[3]+ "\t" + sor[0] + ". " + sor[1]+ "\t" +sor[4] + " km", end="  ", file=file_export)

        if sor[5] == "1":           # the car is in

            print("\t" +sor[0] + ". " + sor[1]+ "\t" +sor[4] + " km", file=file_export)


file_export.close()

print('Menetlevél kész.')

file.close()