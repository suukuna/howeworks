names = ['Кравчук Леонід', 'Кучма Леонід', 'Ющенко Віктор', 'Янукович Віктор', 'Порошенко Петро',
         'Зеленський Володимир']


def structured_ukr_presidents_names(names: list) -> str:
    yield from names


n = structured_ukr_presidents_names(names)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

