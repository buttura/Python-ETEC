print('\033[1;36m--=--=--=--=--=--=--=--=---=--=\033[m')
print('')
print('\033[1;32mC Á L C U L O   D A   M É D I A\033[m')
print('')
print('\033[1;36m--=--=--=--=--=--=--=--=---=--=\033[m')
num = float(input('\033[1;32m>>\033[m PRIMEIRA PROVA: '))
num2 = float(input('\033[1;32m>>\033[m SEGUNDA PROVA: '))
media = (num + num2)/2
print('')
print(f'A sua média é: \033[1;32m{media:.1f}\033[m',end='\n')
if media >= 9:
    print('\033[1;32mParabéns!\033[m Você tirou \033[1;32mMB\033[1;32m.')
elif media >= 7 and media < 9:
    print('\033[1;32mParabéns!\033[m Você tirou \033[1;36mB\033[m.')
elif media >= 5 and media < 7:
    print('\033[1;32mParabéns!\033[m Você tirou \033[1;33mR\033[m.')
elif media >= 0 and media < 5:
    print('\033[1;31mReprovado!\033[m Você tirou \033[1;31mI\033[m.')

