print('Juan Pablo Rojas Chinchilla')
print('201900289')
print('Laboratorio Lenguajes Formales y de Programacion')
print('')

expresion1 = '__servidor1'
expresion2 = '3servidor'


def automata (expresion):
    contador = 0
    print('-------------------------------------------------------------------------------------')
    print('su expresion es ' + expresion)
    if len(expresion) >= 3:
        for letra in expresion:
            if letra == '_' and letra == expresion[0]:
                pass
            elif letra.isalpha() and letra == expresion[0]:
                pass
            elif letra == '_' and letra == expresion[contador - 1]:
                pass
            elif letra.isalpha() and (expresion[contador - 1].isalpha() or contador == len(expresion) - 2):
                pass
            elif letra.isdigit() and letra == expresion[contador] and expresion[contador] == expresion[-1]:
                print('y su expresion pertenece al lenguaje')
                print('-------------------------------------------------------------------------------------')
                return
            else:
                break
            contador += 1
    print('y su expresion no pertenece al lenguaje')
    print('-------------------------------------------------------------------------------------')


decision = True
while decision:
    print('1. quiere ingresar sus propias palabras \n2. quiere utilizar __servidor1 y 3servidor')
    opcion = input('\npor favor seleccione un numero \n')

    if opcion == '2':
        automata('__servidor1')
        automata('3servidor')
    else:
        automata(input('ingrese su palabra \n'))
        automata(input('ingrese su palabra \n'))
    quiere = input('desea continuar? si/no \n')
    if quiere == 'no' or quiere == 'NO' or quiere == 'No':
        decision = False
