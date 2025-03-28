vogaisList = ['a','e','i','o','u','á','é','í','ó','ú','à','è','ì','ò','ù','â','ê','î','ô','û','ã','õ','ü']

print("Bem vindo/a/e ao analisador de textos")
texto = input("Digite seu texto: ").lower()
vogaisqt=0

#print(texto)

for letra in texto:
    if letra in vogaisList:
        vogaisqt += 1


print(f"Quantidade de vogais em seu texto: {vogaisqt}")