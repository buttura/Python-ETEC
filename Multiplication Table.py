n = int(input('Digite um número: '))
q = int(input('Multiplicador: '))
for c in range(0, q+1):
    print(f'{n:2} x {c:2} = {n*c:2}')
