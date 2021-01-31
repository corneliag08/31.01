prenume=["Mihai","George","Ana","Dan","Ion","Geta","Vio"]
varsta=[14,23,15,14,12,41,39]
for i in range (0,len(prenume)):
    print (prenume[i], 'are', varsta[i],'ani')

prenume.append('Andreea')
prenume.append('Ioan')
varsta.append('34')
varsta.append('23')
print(prenume)
print(varsta)

del prenume[2:3]
print (prenume)
del varsta[2:3]
print(varsta)

print(prenume[0:3])
print(varsta[:3])

print(prenume[::-1])

print(prenume[2])
print(varsta[2])
print(prenume[4])
print(varsta[4])
print(prenume[0:6])
print(varsta[0:6])