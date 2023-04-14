#Verifica se um número pertence à sequência de fibonacci

numero = int(input("Insira o número da sequencia de fibonacci que deseja verificar:"))
fibonacci_buffer = [0,1]
fibonacci_number = 0
verificador = False


while(fibonacci_number <= numero):
    
    if(fibonacci_number == numero):
        verificador = True
        print("O número pertence a sequência de Fibonacci")
        exit()


    fibonacci_number = fibonacci_buffer[0] + fibonacci_buffer[1]
    fibonacci_buffer[0] = fibonacci_buffer[1]
    fibonacci_buffer[1] = fibonacci_number
    
    

print("O número não pertence a sequência de Fibonacci")