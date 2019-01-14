#1.Feladat:
forras = open("szavazatok.txt")
sorok = forras.readlines()
#\n karakter eltűntetése
for x in range(0,len(sorok)):
   sorok[x] = sorok[x][:-1]

#2.Feladat:
print("2.Feladat:\nA helyhatósági választáson {0} képviselőjelölt indult.".format(len(sorok)))

#3.Feladat:
sorok2=[]

for x in range(0,len(sorok)):
   sorok2.append(sorok[x].split(" "))
   
for x in range(0,len(sorok2)):
   sorok2[x] = sorok2[x][1:4]

vnev=input("\n3.Feladat:\nVezetéknév: ")
knev=input("Keresztnév: ")
seged=0 #segéd a for ciklusban.

for x in range(0,len(sorok2)):
   seged+=1
   if vnev == sorok2[x][1] and knev == sorok2[x][2]:
      print(vnev,knev,"{0} szavazatot kapott.".format(sorok2[x][0]))
      break
   elif seged==len(sorok2):
      print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
      
#4.Feladat:
szavazok=0

for x in range(0,len(sorok2)):
   szavazok += int(sorok2[x][0])

szazalek=format(szavazok/12345*100, '.2f') #format-al 2tizedes jegyre kerekítem, round(,2) nem volt jó valamiért
print("\n4.Feladat:\n A választáson {0} állampolgár, a jogosultak {1}%-a vett részt.".format(szavazok,szazalek))

#5.Feladat:
sorok3=[]

for x in range(0,len(sorok)):
   sorok3.append(sorok[x].split(" "))

ZEP,GYEP,HEP,TISZ,FUGG=0,0,0,0,0

for x in range(0,len(sorok3)):
   if sorok3[x][4] == "ZEP":
      ZEP += int(sorok3[x][1])
   
   elif sorok3[x][4] == "GYEP":
      GYEP += int(sorok3[x][1])
   
   elif sorok3[x][4] == "HEP":
      HEP += int(sorok3[x][1])
   
   elif sorok3[x][4] == "TISZ":
      TISZ += int(sorok3[x][1])
   
   elif sorok3[x][4] == "-":
      FUGG += int(sorok3[x][1])

ZEPP = format(ZEP/szavazok*100, '.2f')
GYEPP = format(GYEP/szavazok*100, '.2f')
HEPP = format(HEP/szavazok*100, '.2f')
TISZ = format(TISZ/szavazok*100, '.2f')
FUGG = format(FUGG/szavazok*100, '.2f')

print("\n5.Feladat:\n  ZEP: {0}%\n GYEP: {1}%\n  HEP: {2}%\n TISZ: {3}%\n FUGG: {4}%".format(ZEPP,GYEPP,HEPP,TISZ,FUGG))

#6.Feladat:
szavazatok=[]
for x in range(0,len(sorok3)):
   szavazatok.append(int(sorok3[x][1]))
print("\n6.Feladat:")
for x in range(0,len(sorok3)):
   if int(sorok3[x][1]) == max(szavazatok):
      if sorok3[x][4] != "-":
         print(sorok3[x][2],sorok3[x][3],sorok3[x][4])
      else:
         print(sorok3[x][2],sorok3[x][3],"független")
#7.Feladat:
ki = open("kepviselok.txt","w")
ki.write("FOLYTASD INNEN sasha cuki")
ki.close() 
