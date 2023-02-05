print('\033[1;36m--=--=--=--=--=--=--=--=---=--=\033[m')
print('')
print('\033[1;32mC Á L C U L O   D E   I M C\033[m')
print('')
print('\033[1;36m--=--=--=--=--=--=--=--=---=--=\033[m')
peso = float(input('\033[1;32m>>\033[m PESO: '))
altura = float(input('\033[1;32m>>\033[m ALTURA: [M] '))
imc = peso/altura**2
print('')
print('-------------------------------------------------')
print('        IMC         |        CLASSIFICAÇÃO')
print('-------------------------------------------------')
print(' \033[1;31mABAIXO DE 18,5\033[m     |      Abaixo do Peso')
print('\033[1;32mENTRE 18,6 E 24,9\033[m   |   Peso Ideal (Parabéns)')
print('\033[1;36mENTRE 25,0 E 29,9\033[m   |  Levemente acima do peso')
print('\033[1;33mENTRE 30,0 E 34,9\033[m   |     Obesidade grau I')
print('\033[1;95mENTRE 35,0 E 39,9\033[m   | Obesidade grau II (severa)')
print('   \033[1;31mACIMA DE 40\033[m      |  Obesidade III (mórbida)')
print('-------------------------------------------------')
print(f'O seu IMC é: \033[1;32m{imc:.2f}\033[m',end='\n')
if imc < 18.5:
    print('Você está \033[1;31mABAIXO DO PESO\033[m.')
elif imc >= 18.5 and imc < 25:
    print('\033[1;32mParabéns!\033[m Você está no \033[1;32mPESO IDEAL\033[m.')
elif imc >= 25 and imc < 30:
    print('Você está \033[1;36mLEVEMENTE ACIMA DO PESO\033[m.')
elif imc >= 30 and imc < 35:
    print('Você está na \033[1;33mOBESIDADE GRAU I\033[m.')
elif imc >= 35 and imc < 40:
    print('Você está na \033[1;95mOBESIDADE GRAU II (severa)\033[m.')
elif imc >= 40:
    print('Você está na \033[1;31mOBESIDADE GRAU III (mórbida)\003[m.')

