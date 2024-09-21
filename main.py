# Imprimir um cabeçalho
print ("# Torre de Hanói")

def mover (disco, origem, destino):
  print (f"Mover _disco {disco}_ da *torre {origem}* para a *torre {destino}*")

def torre_hanoi (n, torre_origem, torre_intermediaria, torre_destino):

  if n == 1:
    mover (1, torre_origem, torre_destino)
  else:
    # Resolver a torre de hanoi para (n-1) discos, tendo a torre de origem atual como origem, a torre do meio atual como destino, e a torre de destino atual como auxiliar
    torre_hanoi (n-1, torre_origem, torre_destino, torre_intermediaria)
  
    # Mover o disco n para a torre de destino
    mover (n, torre_origem, torre_destino)
    
    # Resolver a torre de hanói para (n-1) discos, tendo a torre do meio atual como origem, a torre de destino atual como destino, e a torre de origem atual como auxiliar
    torre_hanoi (n-1, torre_intermediaria, torre_origem, torre_destino)

torre_hanoi(5, "A", "B", "C")
  
