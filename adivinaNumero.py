import random

class JuegoAdivinanza:
    def __init__(self, minimo, maximo):
        self.numero_a_adivinar = random.randint(minimo, maximo)
        self.intentos = 0

    def adivinar(self, numero):
        self.intentos += 1

        if numero < self.numero_a_adivinar:
            return f"Demasiado bajo. Intento #{self.intentos}. Intenta de nuevo."
        elif numero > self.numero_a_adivinar:
            return f"Demasiado alto. Intento #{self.intentos}. Intenta de nuevo."
        else:
            return f"¡Correcto! Has adivinado el número en {self.intentos} intentos."

# Uso del juego
if __name__ == "__main__":
    print("Bienvenido al juego de adivinanza de números.")
    print("El número está entre 1 y 100.")

    while True:
        try:
            intento = int(input("Ingresa tu adivinanza: "))
            resultado = JuegoAdivinanza(1, 100).adivinar(intento)
            print(resultado)
            print("*" * 50)  # Línea de asteriscos para separar visualmente cada intento :D

            if resultado.startswith("¡Correcto!"):
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

