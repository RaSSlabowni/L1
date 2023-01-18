def number_to_words(n):  # функция перевода числа в слова
    f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 0: ''}
    o = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто', 0: ''}
    s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    b = {100: 'сто', 200: 'Двести', 300: 'Триста', 400: 'Четыреста'
        , 500: 'Пятьсот', 600: 'Шестьсот', 700: 'Семьсот',
         800: 'Восемьсот', 900: 'Девятьсот', 0: ''}
    m = {1000: 'Тысяча', 2000: 'Две тысячи', 3000: 'Три тысячи',
         4000: 'Четыре тысячи', 5000: 'Пять тысяч' }
    n1 = n % 10
    n2 = n - n1
    n3 = n % 100
    n4 = n - n3
    n5 = n3 - n1
    n6 = n % 1000
    n7 = n - n6
    n8 = n4 - n7

    if n < 10:
        return f.get(n)
    elif 10 < n < 20:
        return s.get(n)
    elif 10 <= n <= 99 and n in o:
        return o.get(n)
    elif 100 <= n <= 999 and n in b:
        return b.get(n)
    elif 1000 <= n <= 9999 and n in m:
        return m.get(n)
    elif len(str(abs(n))) == 2:
        return o.get(n2) + ' ' + f.get(n1)
    elif n % 100 == (11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19) and len(str(abs(n))) == 3:
        return b.get(n4) + ' ' + s.get(n3)
    elif len(str(abs(n))) == 3 and n % 100 != (11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19):
        return b.get(n4) + ' ' + o.get(n5) + ' ' + f.get(n1)
    elif len(str(abs(n))) == 4 and n % 100 == (11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19):
        return m.get(n7) + ' ' + b.get(n8) + ' ' + s.get(n3)
    elif len(str(abs(n))) == 4:
        return m.get(n7) + ' ' + b.get(n8) + ' ' + o.get(n5) + ' ' + f.get(n1)




def deletecharacters(msg):
    msg1 = msg.replace('(', '')
    msg2 = msg1.replace(')', '')
    msg3 = msg2.replace(',', '')
    msg4 = msg3.replace("'", '')
    return msg4
