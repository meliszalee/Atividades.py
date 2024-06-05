def main():
    while True:
        # Exibe o menu de opções
        print("Escolha a operação matemática que deseja realizar:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        opcao = int(input("Digite o número da opção desejada: "))

        # Verifica se o usuário quer sair do programa
        if opcao == 5:
            print("Saindo do programa...")
            break

        # Solicita ao usuário os dois números para a operação
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        # Executa a operação escolhida e exibe o resultado
        if opcao == 1:
            resultado = numero1 + numero2
            print("Resultado da adição:", resultado)
        elif opcao == 2:
            resultado = numero1 - numero2
            print("Resultado da subtração:", resultado)
        elif opcao == 3:
            resultado = numero1 * numero2
            print("Resultado da multiplicação:", resultado)
        elif opcao == 4:
            if numero2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = numero1 / numero2
                print("Resultado da divisão:", resultado)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

            
            
