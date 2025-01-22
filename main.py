from utils import inicializar_juego

def jugar_ahorcado():
    
    palabra_adivinar = "python"
    vidas, palabra_oculta = inicializar_juego(palabra_adivinar)

    print("Palabra a adivinar:", " ".join(palabra_oculta))

    while vidas > 0:
        letra_usuario = input("Introduce una letra: ").lower()

        if letra_usuario in palabra_adivinar:
            print(f"¡Has acertado! La letra '{letra_usuario}' está en la palabra.")
            for index, letra in enumerate(palabra_adivinar):
                if letra == letra_usuario:
                    palabra_oculta[index] = letra_usuario
            print("Progreso:", " ".join(palabra_oculta))
        else:
            vidas -= 1
            print(f"Has fallado. La letra '{letra_usuario}' no está en la palabra.")
            print(f"Te quedan {vidas} vidas.")

        if "_" not in palabra_oculta:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_adivinar}")
            break

    if "_" in palabra_oculta:
        print(f"FIN DEL JUEGO. Has perdido. La palabra era: {palabra_adivinar}") 

if __name__ == "__main__":
    jugar_ahorcado()