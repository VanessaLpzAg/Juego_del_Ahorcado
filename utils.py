
def inicializar_juego(palabra):
    """Inicializa los valores del juego."""
    vidas = 6
    palabra_oculta = list("_" * len(palabra))
    return vidas, palabra_oculta