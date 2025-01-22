def jugar_ahorcado(vidas, palabra_adivinar, palabra_oculta):

    vidas = 1
    palabra_adivinar = "python"
    palabra_oculta = list("_"*len(palabra_adivinar))
    print(palabra_oculta)

    while vidas > 0:
        letra_usuario = input("Introduce una letra:")     # Introduccion de letra por parte del usuario.
    
        if letra_usuario in palabra_adivinar:             # Comprobacion de la letra introducida con las letras de la palabra a adivinar.
            print(f"Has acertado. La letra '{letra_usuario}' está en la palabra.")
        
           
        else:
            print(f"Has fallado. La letra '{letra_usuario}' no esta en la palabra")
            print("Te quedan:", vidas - 1)
            print(palabra_oculta)
        break
        
    if palabra_adivinar == palabra_oculta:                # Desarrollo del fin de juego
        print(f" FIN DEL JUEGO. YOU WIINN!!! La palabra era '{palabra_adivinar}'")

    else:
        print(f"FIN DEL JUEGO. YOU LOSEEE... La palabra era '{palabra_adivinar}'") 