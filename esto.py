listaPecas = [] #lista é a melhor escolha pois não se sabe quantos
cadastros/registros terão
#--Início cadastrarPeca--
def cadastrarPeca(rp):#rp, ou registro de peça
printlistaPecas = ('Você selecionou a opção de cadastrar peça')
print('Código da Peça: {}'.format(rp))
nome = input('Por favor, entre com o NOME da peça: ')
fabricante = input('Por favor, entre com o FABRICANTE da peça: ')
valor = float(input('Por favor, entre com o VALOR(R$) da peça: '))
dicionarioPeca = {'--------------------\nCódigo': rp,
'Nome': nome,
'Fabricante': fabricante,
'Valor': valor}
listaPecas.append(dicionarioPeca.copy()) #Uma cópia do dicionário é
importante pra caso ele sofrer alguma alteração, não alterar dentro da
lista
#--Fim cadastrarPeca--
#--Início consultarPeca--
def consultarPeca():
while True:
try:
print('Você selecionou a opção de consultar peças')
opDesejada = int(input('Escolha a opção desejada:\n'
'1- Consultar todas a peças\n'
'2- Consultar peças por código\n'
'3- Consultar peças por fabricante\n'
'4- Retornar\n'
'>> '))
if opDesejada == 1:
for peca in listaPecas: #Esse "for" vai em cada ítem da
'listaPecas' para mostrar todas as informações, porém ele não consegue
acessar as keys e values
for key, value in peca.items():#Esse "for" serve para
acessar as keys e values
print('{}: {}'.format(key, value))
elif opDesejada == 2:
pecaCod = int(input('Digite o CÓDIGO da peça:'))
for peca in listaPecas:
if (peca['--------------------\nCódigo'] == pecaCod):
for key, value in peca.items():
print('{}: {}'.format(key, value))
elif opDesejada == 3:
pecaCod = input('Digite o FABRICANTE da peça: ')
for peca in listaPecas:
if (peca['Fabricante'] == pecaCod):
for key, value in peca.items():
print('{}: {}'.format(key, value))
elif opDesejada == 4:
return
except ValueError:
print('Valor inválido')
#--Fim consultarPeca--
#--Início removerPeca--
def removerPeca():
pecaCod = int(input('Digite o código da peça a ser removida: '))
for peca in listaPecas:
if (peca['--------------------\nCódigo'] == pecaCod):
listaPecas.remove(peca)
#--Fim removerPeca
#Programa Principal
nico4022326 = 'Nícolas Vinícius Lobo Morais'
print('Bem Vindo ao Controle de Estoque da Bicicletaria do
{}'.format(nico4022326))
registroPecas = 0
while True: #While foi utilizado pois não se sabe quantas vezes as opções
serão repetidas
try:#O try vai ser utilizado para evitar que algum parâmetro inválido
seja digitado
opcao = int(input('Escolha a opção desejada:\n'
'1- Cadastrar Peças\n'
'2- Consultar Peças\n'
'3- Remover Peças\n'
'4- Sair\n'
'>> '))
if opcao == 1:
registroPecas += 1 #Será o código da peça
cadastrarPeca(registroPecas)
elif opcao == 2:
consultarPeca()
elif opcao == 3:
removerPeca()
elif opcao == 4:
print('Programa encerrado...')
break
else: #Caso o usuário digite números que não existem no menu
print('Opção Inválida')
continue
except: #Caso o usuário digite um número decimal, ou uma letra. Isso
evita um ValueError
print('Valor inválido')
