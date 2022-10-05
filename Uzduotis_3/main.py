# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).
from pprint import pprint

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

'''Nekeis žodyno, priimto kaip argumento, savo viduje.
Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).
'''


def get_dict_values(obj):
    for key, value in obj.items():
        print(value)


get_dict_values(audi)
