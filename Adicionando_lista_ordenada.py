def adiciona_em_ordem(nome, distancia, lista):
    lista1 = [nome, distancia]
    lista_nova = []
    if lista == []:
            lista_nova.append(lista1)
    for paises_distancia in lista:
        if paises_distancia[1] < lista1[1]:
            lista_nova.append(paises_distancia)
        elif lista1[1] < paises_distancia[1] and lista1 not in lista_nova:
            lista_nova.append(lista1)
            lista_nova.append(paises_distancia)
        else:
            lista_nova.append(paises_distancia)

    if lista1 not in lista_nova:
            lista_nova.append(lista1)
    return lista_nova