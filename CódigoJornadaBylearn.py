def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  return media

def verificar_aprovacao(media):
  if media >= 6:
    print('Aluno Aprovado :)')
  else:
    print('Aluno Reprovado :(')

jose = [1, 4, 6, 7]
media = calcular_media(jose)
verificar_aprovacao(media)        