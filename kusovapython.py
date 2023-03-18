p = 0
q = 0
laters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЧШЩЬЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!, "
p_key = 0
priv_key = 0
close = True

while close:
    p, q = input("Введіть 2 прости числа в одному рядку через пробіл:\n> ").split(" ")
    p = int(p)
    q = int(q)
    n = p * q
    z = (p-1) * (q-1)

    for i in range(1, 10000):
        if 0 != z % i:
            p_key = round(i)
            break

    for j in range(0, 10000):
        d = 1 + (j * z)
        d2 = d / p_key
        if 0 == d % p_key:
            priv_key = round(d2)
            break

    close2 = True
    while close2:
        print("\n")
        print("p=",p)
        print("q=",q)
        print("модуль=",n)
        print("відкритий ключ=",p_key)
        print("особистий ключ=",priv_key)
        func = input("Виберіть функцію\n'e' = зашифрувати текст\n'd' = розшифрувати текст\n'ex' = для завешення програми\n> ")

        if func == "e":
            text = input("Введіть текст: ")
            encrypted = ""
            for k in text:
                m = 0
                for l in laters:
                    if k == l:
                        if m < 10:
                            m = m + 00
                        encrypted = encrypted + (str((m ** p_key) % n)) + " "
                        break
                    m += 1
            print("Зашифрований текст: ", encrypted)

        if func == "d":
            encrypted = input("Введіть зашифрований текст: ")
            text = ""
            for s in encrypted.split(" "):
                for k in laters:
                    m = 0
                    for l in laters:
                        if k == l:
                            if s == (str((m ** p_key) % n)):
                                text = text + l
                            break
                        m += 1
            print("Розшифрований текст:", text)

        if func == "ex":
            close = False
            close2 = False
