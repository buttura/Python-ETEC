print('\033[1;36m--=--=--=--=--=--=--=--=---=--=--=--=--\033[m')
print('')
print('\033[1;32mC O N V E R S Ã O  D E  U N I D A D E S\033[m')
print('')
print('\033[1;36m--=--=--=--=--=--=--=--=---=--=--=--=--\033[m')
print('')
print('\033[1;32m[ 1 ]\033[m KM \033[1;32m>\033[m M')
print('\033[1;32m[ 2 ]\033[m M  \033[1;32m>\033[m CM')
print('\033[1;32m[ 3 ]\033[m CM \033[1;32m>\033[m MM')
print('\033[1;32m[ 4 ]\033[m CM \033[1;32m>\033[m POL')
print('')
print('\033[1;36m--=--=--=--=--=--=--=--=---=--=--=--=--\033[m')
opcao = int(input('\033[1;32m>>\033[m Sua opção: '))
print('')
if opcao == 1:
    quilometros = int(input('Digite o valor em \033[1;36mQUILÔMETROS\033[m: '))
    print(f'A conversão de quilômetros (KM)')
    print('para metros (M) é \033[1;32m{quilometros * 1000}\033[m metros.')
elif opcao == 2:
    metros = int(input('Digite o valor em \033[1;36mMETROS\033[m: '))
    print(f'A conversão de metros (M) para centimetros (CM) é \033[1;32m{metros * 100}\033[m centimetros.')
elif opcao == 3:
    centimetros = int(input('Digite o valor em \033[1;36mCENTIMETROS\033[m: '))
    print(f'A conversão de centimetros (CM) para milimetros (MM) é \033[1;32m{centimetros * 10}\033[m milimetros.')
elif opcao == 4:
    centimetros = int(input('Digite o valor em \033[1;36mCENTIMETROS\033[m: '))
    print(f'A conversão de centimetros (CM) para polegadas (POL) é \033[1;32m{centimetros/2.54}\033[m polegadas.')
else:
    print('\033[1;31mOpção Inválida\033[m, tente novamente.')



