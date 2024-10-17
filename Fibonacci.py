def fibonacci(n, soma=None, conta=None):
    if soma is None:
        soma = {}
    if conta is None:
        conta = []  

    if n < 0:
        return "Não existe Fibonacci para números negativos."
    elif n in soma: 
        return soma[n], conta
    elif n == 0:
        conta.append("F(0) = 0")
        soma[0] = 0
        return 0, conta
    elif n == 1:
        conta.append("F(1) = 1")
        soma[1] = 1
        return 1, conta
    else:
        
        fibonacci1, conta = fibonacci(n - 1, soma, conta)
        fibonacci2, conta = fibonacci(n - 2, soma, conta)
        resultado = fibonacci1 + fibonacci2
        soma[n] = resultado  
        conta.append(f"F({n}) = F({n-1}) + F({n-2}) = {fibonacci1} + {fibonacci2} = {resultado}")
        return resultado, conta

try:
    numero = int(input("Digite um número para calcular a sequência de Fibonacci: "))

    resultado, conta = fibonacci(numero)
    print(f"O número na posição {numero} da sequência de Fibonacci é: {resultado}.")
    print("Cálculo detalhado:")
    for calculo in conta:
        print(calculo)

except ValueError:
    print("Entrada inválida! Por favor, insira um número inteiro.")
