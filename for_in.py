#Uma nova loja de cosméticos abriu no seu bairro e pediram 
# para você elaborar um sistema que imprime na tela na frente
#  da loja os novos produtos que chegaram. O sistema da loja
#  já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.

lista_produtos = [
    'máscaras faciais', 'batons', 'esmaltes', 'perfumes', 
    'loções', 'xampus', 'sabonetes', 'delineadores'
]

for produto in lista_produtos:
    print(produto)

for produto in lista_produtos:
    print(f"Temos {produto} à venda!")