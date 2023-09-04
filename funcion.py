numeros=[]

largo=int(input('Ingrese cantidad de numeros: '))
i=0
while i<largo:
	num=int(input('Ingrese un numero (cero o uno):'))
	if num==0 or num==1:
		numeros.append(num)
		i=i+1
	else:
		print('Los numeros deben ser ceros o unos')
print()
for i in range(len(numeros)):
	print(numeros[i],end='')

input()
