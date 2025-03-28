vogaisList = ['a','e','i','o','u','á','é','í','ó','ú','à','è','ì','ò','ù','â','ê','î','ô','û','ã','õ','ü']

print("Bem vindo/a/e ao analisador de textos")
texto = input("Digite seu texto: ").lower()
vogaisqt=0
palavrasqt=0
palavraLonga=""

#print(texto)

for letra in texto:
    if letra in vogaisList:
        vogaisqt += 1


textoSeparado = texto.split()
palavrasqt= len(textoSeparado)

for palavraAtual in textoSeparado:
    if len(palavraAtual)>len(palavraLonga):
        palavraLonga=palavraAtual


print(f"\nQuantidade de VOGAIS em seu texto: {vogaisqt}\n"
      f"Quantidade de PALAVRAS em seu texto: {palavrasqt}\n"
      f"Palavra mais LONGA: {palavraLonga}")


input("\nPressione qualquer tecla para sair.")


