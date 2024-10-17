def fibonacci(n):
    if n < 0:
        return "Não existe Fibonacci para números negativos."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(input("Digite um número para calcular a sequência de Fibonacci: "))

resultado = fibonacci(numero)
print(f"O número na posição {numero} da sequência de Fibonacci é: {resultado}")