#9.	If Statements

temperature = 25

if temperature > 30:
    print("\nIt's a hot day")
    print("Drink plenty od water")
elif temperature > 20:  #(20, 30]   Condição verdadeira se temperature for maior que 20 e menor igual a 30
    print("\nIt's a nice day")
elif temperature > 10:  #(10, 20]   Condição verdadeira se temperature for maior que 10 e menor igual a 20
    print("\nIt's a bit cold")
else:                   #Executa o bloco caso nenhuma condição seja verdadeira
    print("\nIt's cold")
print("Done")