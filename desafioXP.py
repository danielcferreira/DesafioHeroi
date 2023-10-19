heroi = [('jorge',900),
         ('Antonio fagunde',2000),
         ('Fabio jr',3000),
         ('Amaral',6500),
         ('Atila',8500),
         ('rosa',9000),
         ('Magali',8000),
         ('Maria Carem',18000)
         ]

for nome, xp in heroi:
    if xp < 1000:
        nivel = 'ferro'
        print('o heroi de nome {} esta no nivel {}'.format(nome,nivel))
    elif xp > 1000 and xp <= 2000:
        nivel = 'bronze'
        print('o heroi de nome {} esta no nivel {}'.format(nome,nivel))
    elif  xp > 2000 and xp <=5000:
        nivel = 'prata'
        print('o heroi de nome {} esta no nivel {}'.format(nome,nivel))
    elif  xp > 6000 and xp <=7000:
        nivel = 'ouro'
        print('o heroi de nome {} esta no nivel {}'.format(nome,nivel))
    elif  xp > 7000 and xp <=8000:
        nivel = 'Platina'
        print('o heroi de nome {} esta no nivel {}'.format(nome,nivel))
    elif  xp > 8000 and xp <=9000:
        nivel = 'Ascendente'
        print('o heroi de nome {} esta no nivel {}'.format(nome,nivel))
    elif  xp > 9000 and xp <=10000:
        nivel = 'Imortal'
        print('o heroi de nome {} esta no nivel {}'.format(nome,nivel))
    elif  xp > 10000:
        nivel = 'Radiante'
        print('o heroi de nome {} esta no nivel {}'.format(nome,nivel))