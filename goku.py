"CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AFK": "fuera del teclado",
            "BOOMER":"Muy viejo y no quiere entender a lo jovenes",
            "BASADO": "tiene a su disposicion toda la verdad",
            "CREEPY": "Tenebroso o de miedo",
            "GG":" buena partida",
            "NT":"Buen intento",
            "EZ":"Facil"
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AFK": "fuera del teclado",
            "BOOMER":"Muy viejo y no quiere entender a lo jovenes",
            "BASADO": "tiene a su disposicion toda la verdad",
            "CREEPY": "Tenebroso o de miedo",
            "GG":" buena partida",
            "NT":"Buen intento",
            "EZ":"Facil"
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(f"La palabra {word} significa:  {meme_dict[word]}")
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("no se encontro el significado de: ", word, " intentalo nuevamente")
