def fatorial(n): #definição de uma função fatorial, recebendo o parâmetro 
    
    if n < 0:    
        return "Por favor, insira um número não negativo."
    
    elif n == 0 or n == 1:  
        return 1, "1! = 1"
    
    else:           
        resultado = 1
        #conta = [] 
        for i in range(n, 0, -1):
            resultado *= i
            #conta.append(str(i))  
        
        #expressao = "*".join(conta)    
        return resultado #, f"{n}! = {expressao} = {resultado}"  #retorna o resultado e expressão

try:
    numero = int(input("Digite um número para calcular o fatorial: "))
    resultado = fatorial(numero) #, expressao = fatorial(numero)

    #print(expressao)
    print(f"O fatorial de {numero} é {resultado}.")

except ValueError:
    print("Entrada inválida! Por favor, insira um número inteiro.")
