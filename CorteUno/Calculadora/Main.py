from Operaciones import cálculos

class Calculadora:
    def __init__(self):
        self.operaciones = cálculos()

    def ejecutar(self):
        print("Bienvenido a la calculadora")
        while True:
            print("\nOpciones:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
                       
            opcion = input("Elige una opción (1-5): ")

            if opcion == '5':
                print("Saliendo de la calculadora.")
                break
            
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor, ingresa números válidos.")
                continue

            if opcion == '1':
                print(f"Resultado: {self.operaciones.sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {self.operaciones.restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {self.operaciones.multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {self.operaciones.dividir(num1, num2)}")
            else:
                print("Opción no válida. Por favor, elige de nuevo.")

if __name__ == "__main__":
    Main = Calculadora()
    Main.ejecutar()
