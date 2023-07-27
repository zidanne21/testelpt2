def soma(valor,valor2):
    return valor + valor2

def subtrai(valor,valor2):
    return valor - valor2

def multiplica(valor,valor2):
    return valor*valor2

def divide(valor,valor2):
    if valor2==0:
        print("nao pode dividir")
    return valor/valor2 

def menu():
    print("1,soma")
    print("2,subtrai")
    print("3,multiplica")
    print("4,divide")
    print("5.sair")

valor = input("qual o valor")
valor2 = input("qual o valor")

while(True):
    menu()
    opcao=input("qual opcao voce quer")
    if opcao=='1':
        resultado = soma(valor,valor2)
        print (f"resultado da soma:{resultado}")
    elif opcao =='2':
        resultado = subtrai(valor,valor2)
        print (f"resultado da soma:{resultado}")
    elif opcao == '3':
        resultado = multiplica(valor,valor2)
        print (f"resultado da soma:{resultado}")
    elif opcao == '4':
        resultado = divide(valor,valor2)
        print (f"resultado da soma:{resultado}")
    elif opcao == '5':
        break