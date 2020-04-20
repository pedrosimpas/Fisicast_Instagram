#########################################
###### Criado por Pedro Pasquini   ######
######      Data 20/04/2020        ######
#########################################


## funcao para calcula JOTO ##
def calcula_JOTO(palavra, dica):


	return_JOTO = 0
	if len(palavra) == len(dica):
		for letra1 in palavra:
			for letra2 in dica:
				if letra1 == letra2:
					return_JOTO = return_JOTO +1


	return return_JOTO
		


## Letras do alfabeto
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z']


## Lista com as dicas, sintaxe: [[palavra, ndica]]

## essas foram algumas dicas da matemaniaca no twitter.
lista_dicas = [['foda',2], ['ruim',2],['meta',3],['urso',1]]

### Verifica se uma palavra de 4 letras segue todas as dicas em lista_dicas corretamente e printa a palavra

Nletras = len(alfabeto)

i1 = 0

for i1 in range(Nletras):
	for i2 in range(Nletras):
		for i3 in range(Nletras):
			for i4 in range(Nletras):
				# checa só palavras com letras diferentes
				if i2 != i1 and i2 != i3 and i2 != i4 and i1 != i3 and i1 != i4 and i4 != i3:
					palavra_teste = alfabeto[i1] + alfabeto[i2] + alfabeto[i3] + alfabeto[i4]

					teste = True
					idicas = 0
					while idicas < len(lista_dicas) and teste:
						teste_JOTO = calcula_JOTO(palavra_teste,lista_dicas[idicas][0])
						if not (teste_JOTO == lista_dicas[idicas][1]):
							teste = False
						idicas = idicas + 1
					if teste:
						print(palavra_teste)
				
				
