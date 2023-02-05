import random

nome = ("Higor", "Adilson", "Hugo", "Felipe", "João", "Marcia", "Gustavo", "Eduardo", "Thais", "Gabriela", "Gabriel", "James")
sobrenome = ("Frasson", "Buttura", "Alba", "Zidoi", "Seresuela", "Corbe", "Oliveira", "Trefilio", "Akynatom", "Botelho", "Nardelli")
lista_nomes = list()
for i in range(len(nome)):
    for x in range(len(sobrenome)):
        lista_nomes.append(f"INSERT INTO nome VALUES ('{nome[i]} {sobrenome[x]}');")
random.shuffle(lista_nomes)
for k, v in enumerate(lista_nomes):
    print(v)
