marka = input('Podaj swoja ulubiona marke samochodu ')
print()
marka_Niemiecka = [
                'Audi',
                'BMW Alpine',
                'BMW',
                'Maybach',
                'Mini',
                'Porsche',
                'Volkswagen',
                'Mercedes-Benz',
                'Opel',
]


marka_Wloska = [
                'Alfa Romeo',
                'Benelli',
                'Ferrari',
                'Fiat',
                'Lamborghini',
                'Lancia',
                'Piaggio',
                'Iveco',
                'Maserati',
                'Pagani'
                ]
marka_Brytyjska = [
                'Jaguar',
                'Aston Martin',
                'Lotus',
                'Triumpch',
                'TVR',
                'McLaren',
                'Austin-Healey',
                'Morgan'
]

marka_Japonska = [
                'Acura',
                'Infiniti',
                'Lexus',
                'Subaru',
                'Mitsubishi',
                'Suzuki'
]
marka_Poludniowokoreanska = [
                'Daewoo',
                'Galloper',
                'Hyundai',
                'Kia',
                ]

print()
if marka in marka_Niemiecka:
        print(' Ta marka jest Niemiecka ')
if marka in marka_Wloska:
        print(' Ta marka jest Wloska')
if marka in marka_Brytyjska:
        print('Ta marka jest Brytyjska')
if marka in marka_Japonska:
        print('Ta  marka jest Japonska')
if marka in marka_Poludniowokoreanska:
        print('ta marka jest Poludniowokoreanska')
else:
        print('Zle napisales\las nazwe marki')
print('Dziekuje!')
