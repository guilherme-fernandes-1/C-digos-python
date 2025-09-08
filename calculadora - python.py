def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Usamos try-except para lidar com a divisão por zero
    try:
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida.")
        return a / b
    except ValueError as e:
        return str(e) # Retorna a mensagem de erro como string

def calculadora_avancada():
    while True:
        print("\n--- Calculadora ---")
        print("Operações: +, -, *, /, **")
        print("Digite 'sair' para encerrar.")

        # Recebe a operação do usuário
        operacao = input("Digite a operação (+, -, *, /, **): ")

        if operacao.lower() == 'sair':
            print("Encerrando a calculadora.")
            break

        # Bloco try-except para lidar com entradas inválidas
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
            continue # Pula para o próximo ciclo do loop

        # Lógica para realizar a operação
        if operacao == '+':
            resultado = somar(num1, num2)
        elif operacao == '-':
            resultado = subtrair(num1, num2)
        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        elif operacao == '/':
            resultado = dividir(num1, num2)
        elif operacao == '**':
            resultado = num1 ** num2 # Exponenciação
        else:
            print("Operação inválida.")
            continue
        
        print("Resultado:", resultado)

calculadora_avancada()