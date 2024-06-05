from random import choice

lista_palavras = ['python', 'desenvolvedor', 'software', 'programação']
palavra = choice(lista_palavras)

letras_usuario = []
chances = 5
ganhou = False

print('='*15, 'Jogo da Forca', '='*15, '\n')

while True:
    
    for letra in palavra:
        
        if letra.lower() in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
        
    print('')
    print(f'Você tem {chances} chances')
            
    tentativa = input('Escolha uma letra: ')
    letras_usuario.append(tentativa.lower())
    
    if tentativa.lower() not in palavra.lower():
        chances -= 1
        
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False
    
        
        
    if chances == 0 or ganhou:
        break


print('\n')

if ganhou:
    print(f'Parabéns, você ganhou! A palavra era {palavra}')
    
else:
    print(f'Você perdeu! A palavra era {palavra}')