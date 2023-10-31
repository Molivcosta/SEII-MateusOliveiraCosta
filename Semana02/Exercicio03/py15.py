#15. The range() Function

numbers = range(5)  #Gera uma sequência de números de zero até o número que especificamos
print(numbers)

for number in numbers:
    print(number)

#Ou

print("\n")
for number in range(5):
    print(number)


numbers = range(5, 10)  #Gera uma sequência de números de acordo com o intervalo que especificamos
print("\n", numbers)

for number in numbers:
    print(number)

#Ou


print("\n")
for number in range(5, 10):
    print(number)

print("\n")

numbers = range(5, 10, 2)  #Gera uma sequência de números alternados de acordo com o intervalo que especificamos
print("\n", numbers)

for number in numbers:
    print(number)

#Ou

print("\n")
for number in range(5, 10, 2):
    print(number)


print("\n")