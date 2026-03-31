
while True:
        n1 = float(input("Número: "))
        print("Selecione uma operação:")
        print("Soma: +")
        print("Subtração: -")
        print("Multiplicação: *")
        print("Divisão: /")
        try:
            funcao = input("Operação: ")
            if funcao not in ["+", "-", "*", "/"]:
                raise ValueError("Operação inválida")
        except ValueError:
            print("Selecione uma operação válida!")
            continue
        n2 = float(input("Número: "))
        if funcao == "/" and n2 == 0:
            print("ERROR 404")
        elif funcao == "/":
            resultado = n1 / n2
        elif funcao == "*":
            resultado = n1 * n2
        elif funcao == "+":
            resultado = n1 + n2
        elif funcao == "-":
            resultado = n1 - n2
        print("Esse é o resultado:", resultado)
        sair = input("Deseja continuar? (s/n): ")
        if sair.lower() == "n":
            break
