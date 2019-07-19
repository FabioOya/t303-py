def lista_de_compras(**kwargs):
    fruta = kwargs.get ('fruta')
    if fruta is not None:
        print(f'Na lista e compras há uma fruta {fruta}')

lista_de_compras (fruta='banana', massas='nhoque', verdura='alface')
lista_de_compras (bebida='guaraná',sorvete ='flocos')