def conversionador(valor, esc):
    if esc == 1:
        x = valor * 0.39
        file = open('conversao.txt', 'w+')
        file.write(
            'o valor {} em centimetros equivale a {:.2f} em polegadas'.format(
                valor, x))
        file.seek(0.0)
        print(file.read())
        file.seek(0, 0)
        file.close()

    else:
        x = valor / 0.39
        file = open('conversao.txt', 'w+')
        file.write(
            'o valor {} em polegadas equivale a {:.2f} em centimetros'.format(
                valor, x))
        file.seek(0.0)
        print(file.read())
        file.seek(0, 0)
        file.close()
print('eu sou pobre')