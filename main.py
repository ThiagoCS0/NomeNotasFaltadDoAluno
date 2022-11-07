nome = "Thiago"
nota1 = 8.5
nota2 = 6.5
faltas = 1

def Avaliacao():
  if(faltas<3 and ((nota1+nota2)/2)>7):
    Resultado("APROVADO!!")
  else:
    Resultado("REPROVADO!")

def Resultado(mensagem):
  print("O aluno "+nome+" foi "+mensagem)

Avaliacao()