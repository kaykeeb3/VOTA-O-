from rich import print

# CONSTANTES
VOTOS_BOLSONARO = 0
VOTOS_LULA = 0

# Roda eternamente
while True
 # apresente os candidatos
   print('*'*10)
   print(f'[on blue]TOTAL BOLSONARO:[/]{VOTOS_BOLSONARO}{os.linesep}[on red]TOTAL_LULA:[/]{VOTOS_LULA}')
   print('*'*10)


 # permita votar
  try:
   voto =  int(input(f'Para quem gostaria de votar,?{os.linesep}1 - Bolsonaro{os.linesep}2 - Lula{os.linesep}seu voto'))
  if voto == 1
   VOTOS_BOLSONARO = += 1
  elif voto == 2:
   VOTOS_LULA += 1
  else:
    pass
  except:
    print('Digite 1 ou 2')
    os.system('cls')
   




