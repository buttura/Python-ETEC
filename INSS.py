print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
print('')
print('\033[1;32mS A L Á R I O  L Í Q U I D O\033[m')
print('')
print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
salario = float(input('\033[1;32m>>\033[m SALÁRIO BRUTO: \033[1;32mR$\033[m'))
dependente = int(input('\033[1;32m>>\033[m DEPENDENTES: '))

faixa1 = 1100 * 0.075
faixa2 = (2203.48 - 1100.01) * 0.09
faixa3 = (3305.22 - 2203.49) * 0.12
faixa4 = (6433.57 - 3305.23) * 0.14

faixa1irrf = 0
faixa2irrf = (2826.65 - 1903.99) * 0.075
faixa3irrf = (3751.05 - 2826.66) * 0.15
faixa4irrf = (4664.68 - 3751.06) * 0.225
faixa5irrf = 4664.68 * 0.275
print('')
if salario <= 1100:
    print(f'\033[1;32m1º\033[m faixa do INSS: \033[1;32mR${1100 * 0.075}\033[m')
    print('')
    print(f'Total INSS: \033[1;32mR${faixa1:.2f}\033[m ')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - faixa1
elif salario <= 2203.48:
    print(f'\033[1;32m1º\033[m faixa do INSS: \033[1;32mR${faixa1:.2f}\033[m')
    print(f'\033[1;36m2º\033[m faixa do INSS: \033[1;32mR${faixa2:.2f}\033[m')
    print('')
    print(f'Total INSS: {faixa1 + faixa2:.2f} ')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - (faixa1 + faixa2)
elif salario <= 3305.22:
    print(f'\033[1;32m1º\033[m faixa do INSS: \033[1;32mR${faixa1:.2f}\033[m')
    print(f'\033[1;36m2º\033[m faixa do INSS: \033[1;32mR${faixa2:.2f}\033[m')
    print(f'\033[1;35m3º\033[m faixa do INSS: \033[1;32mR${faixa3:.2f}\033[m')
    print('')
    print(f'Total INSS: {faixa1 + faixa2 + faixa3:.2f} ')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - (faixa1 + faixa2 + faixa3)
elif salario <= 6433.57 or salario > 6433.57 :
    print(f'\033[1;32m1º\033[m faixa do INSS: \033[1;32mR${faixa1:.2f}\033[m')
    print(f'\033[1;36m2º\033[m faixa do INSS: \033[1;32mR${faixa2:.2f}\033[m')
    print(f'\033[1;35m3º\033[m faixa do INSS: \033[1;32mR${faixa3:.2f}\033[m')
    print(f'\033[1;31m4º\033[m faixa do INSS: \033[1;32mR${faixa4:.2f}\033[m')
    print('')
    print(f'Total INSS: \033[1;32mR${faixa1 + faixa2 + faixa3 + faixa4:.2f}\033[m ')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - (faixa1 + faixa2 + faixa3 + faixa4)
    print('')
print(f'SALÁRIO TOTAL: \033[1;32mR${salario - dependente * 189.59:.2f}\033[m')
print('')
print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')

if salario <= 1903.98:
    print('')
    print(f'\033[1;32m1º\033[m faixa do IRRF: \033[1;32mR${faixa1irrf:.2f}\033[m')
    print('')
    print(f'Total IRRF: \033[1;32mR${faixa1irrf:.2f}\033[m')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - (faixa1irrf)
elif salario <= 2825.65:
    print('')
    print(f'\033[1;32m1º\033[m faixa do IRRF: \033[1;32mR${faixa1irrf:.2f}\033[m')
    print(f'\033[1;36m2º\033[m faixa do IRRF: \033[1;32mR${faixa2irrf:.2f}\033[m')
    print('')
    print(f'Total IRRF: R$ {faixa1irrf + faixa2irrf:.2f} ')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - (faixa1irrf + faixa2irrf)
elif salario <= 3751.05:
    print('')
    print(f'\033[1;32m1º\033[m faixa do IRRF: \033[1;32mR${faixa1irrf:.2f}\033[m')
    print(f'\033[1;36m2º\033[m faixa do IRRF: \033[1;32mR${faixa2irrf:.2f}\033[m')
    print(f'\033[1;35m3º\033[m faixa do IRRF: \033[1;32mR${faixa3irrf:.2f}\033[m')
    print('')
    print(f'Total IRRF: \033[1;32mR$ {faixa1irrf + faixa2irrf + faixa3irrf:.2f}\033[m ')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - (faixa1irrf + faixa2irrf + faixa3irrf)
elif salario <= 4664.68:
    print('')
    print(f'\033[1;32m1º\033[m faixa do IRRF: \033[1;32mR${faixa1irrf:.2f}\033[m')
    print(f'\033[1;36m2º\033[m faixa do IRRF: \033[1;32mR${faixa2irrf:.2f}\033[m')
    print(f'\033[1;35m3º\033[m faixa do IRRF: \033[1;32mR${faixa3irrf:.2f}\033[m')
    print(f'\033[1;31m4º\033[m faixa do IRRF: \033[1;32mR${faixa4irrf:.2f}\033[m')
    print('')
    print(f'Total IRRF: \033[1;32mR${faixa1irrf + faixa2irrf + faixa3irrf + faixa4irrf:.2f}\033[m ')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - (faixa1irrf + faixa2irrf + faixa3irrf + faixa4irrf)
elif salario > 4664.68:
    print('')
    print(f'\033[1;32m1º\033 faixa do IRRF: \033[1;32mR${faixa1irrf:.2f}\033[m')
    print(f'\033[1;36m2º\033 faixa do IRRF: \033[1;32mR${faixa2irrf:.2f}\033[m')
    print(f'\033[1;35m3º\033 faixa do IRRF: \033[1;32mR${faixa3irrf:.2f}\033[m')
    print(f'\033[1;31m4º\033 faixa do IRRF: \033[1;32mR${faixa4irrf:.2f}\033[m')
    print(f'\033[1;30m5º\033 faixa do IRRF: \033[1;32mR${faixa5irrf:.2f}\033[m')
    print('')
    print(f'Total IRRF: \033[1;32mR${faixa1irrf + faixa2irrf + faixa3irrf + faixa4irrf + faixa5irrf:.2f}\033[m ')
    print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
    salario = salario - (faixa1irrf + faixa2irrf + faixa3irrf + faixa4irrf + faixa5irrf)
print('')
print(f'SALÁRIO TOTAL: \033[1;32mR${salario:.2f}\033[m')
print('')
print('\033[1;36m--=--=--=--=--=--=--=--=--=-\033[m')
