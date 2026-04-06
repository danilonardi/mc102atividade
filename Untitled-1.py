print("-------Calculadora------- ")
print("Operação disponivel: + , - , * , ** , /")

a = float(input("Digite um numero:"))
Operacao = input("Digite a operacão:")
b = float(input("Digite outro numero:"))


match Operacao:
      case "+":
         print(f" o valor é {a + b:.2f}")

      case "*":
         print(f"o valor é {a * b: .2f}")
     
      case "**":
         print(f"o valor é {a ** b: .2f}")
    
      case "-":
         print (f"o valor é {a - b:.2f}")
    
      case "/":
         print (f"o valor é {a / b: .2f}")
        
      case _ :
         print("Invalido, digite uma operacao")


       