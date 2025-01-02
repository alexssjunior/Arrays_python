#A loja de cosméticos ficou muito feliz com seu trabalho
#  e chamaram você novamente! Dessa vez, eles precisam que você atualize o array de produtos.
#  Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções.
#  Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos.
#  Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.


lista_produtos = [
    'máscaras faciais', 'batons', 'esmaltes', 'perfumes', 
    'loções', 'xampus', 'sabonetes', 'delineadores'
]

# Atualizando os produtos
lista_produtos[1] = 'rímel'  # Substitui "batons" por "rímel"
lista_produtos[4] = 'cremes hidratantes'  # Substitui "loções" por "cremes hidratantes"
lista_produtos.remove('delineadores')  # Remove "delineadores"

# Adicionando novos produtos
lista_produtos.append('protetor solar')
lista_produtos.append('tônicos faciais')

# Imprimindo a nova lista
print("Lista de produtos atualizada:", lista_produtos)
