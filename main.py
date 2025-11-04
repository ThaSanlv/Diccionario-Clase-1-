meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": " ligera desaprobación",
            "CREEPY":"aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "ÉL/ELLA JURA": "Piensa que tiene la razón",
            "OK MAÑANA 💜": "eso no va a pasar"

            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ").upper()

if word in meme_dict.keys():
    print(word,":",meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("Lo lamento, pero no encontramos ese termino")
    # ¿Qué hacer si no se encuentra la palabra?
