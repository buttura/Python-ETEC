print("\033[1;36m--=--=--=--=--=--=--=--=--=--=--=--=--=\033[m")
print('')
print("\033[1;32mC O M I S S Ã O   D O   V E N D E D O R \033[m")
print('')
print("\033[1;36m--=--=--=--=--=--=--=--=--=--=--=--=--=\033[m")
print("Digite a(s) quantidade(s) vendida(s)")
print('pelo vendedor:')
print('')
mussarela = float(input("\033[1;36m>>\033[m Mussarela: "))
mortadela = float(input("\033[1;36m>>\033[m Mortadela: "))
presunto = float(input("\033[1;36m>>\033[m Presunto: "))
peitodeperu = float(input("\033[1;36m>>\033[m Peito de Peru: "))

mussarela = 22.60 * mussarela
comissaomussarela = mussarela * 5 / 100
mortadela = 8.98 * mortadela
comissaomortadela = mortadela * 6.5 / 100
presunto = 31.03 * presunto
comissaopresunto = presunto * 4.5 / 100
peitodeperu = 58.90 * peitodeperu
comissaopeitodeperu = peitodeperu * 2.5 / 100

valtotalcomissao = comissaopeitodeperu + comissaopresunto + comissaomortadela + comissaomussarela
venda = peitodeperu + mortadela + mussarela + presunto

print('')
print("\033[1;36m--=--=--=--=--=--=--=--=--=--=--=--=--=\033[m")
print('')
print('O vendedor vendeu:')
print('')
print(f'\033[1;32mR${mussarela:.2f}\033[m de Mussarela por Kilo')
print(f'\033[1;32mR${mortadela:.2f}\033[m de Mortadela por Kilo')
print(f'\033[1;32mR${presunto:.2f}\033[m de Presunto por Kilo')
print(f'\033[1;32mR${peitodeperu:.2f}\033[m de Peito de Peru por Kilo')
print('')
print("\033[1;36m--=--=--=--=--=--=--=--=--=--=--=--=--=\033[m")
print('')
print('A comissão do vendedor de cada produto:')
print('')
print(f'\033[1;32mR${comissaomussarela:.2f}\033[m de Mussarela')
print(f'\033[1;32mR${comissaomortadela:.2f}\033[m de Mortadela')
print(f'\033[1;32mR${comissaopresunto:.2f}\033[m de Presunto')
print(f'\033[1;32mR${comissaopeitodeperu:.2f}\033[m de Peito de Peru')
print('')
print("\033[1;36m--=--=--=--=--=--=--=--=--=--=--=--=--=\033[m")
print('')
print(f'Venda(s): \033[1;32mR${venda:.2f}\033[m')
print(f'Comissão Total: \033[1;32mR${valtotalcomissao:.2f}\033[m')