def fibonacci(n):
    if n < 0:
        return "Não existe Fibonacci para números negativos."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicita um número ao usuário
numero = int(input("Digite um número para calcular a sequência de Fibonacci: "))

# Calcula o valor de Fibonacci e exibe o resultado
resultado = fibonacci(numero)
print(f"O número na posição {numero} da sequência de Fibonacci é: {resultado}")
