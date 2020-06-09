import functools, itertools

# в массиве kl через 1 лежат координаты ловцов         т.е. x1 y1 x2 y2 x3 y3
# ob отвечает за кол-во ловцов + углы

# переменные

global n, xb, yb, s, kl, k, d, a, ob, r, f, xs, ys, fail
kl = []
e = ob = yv = xv = i = 0
a = []  # в массиве a через 1 лежат координаты возможных ходов     т.е. x1 y1 x2 y2 x3 y3


# функции

def analiz(x, y, ob):
    srzn = kol = d = 0
    for i in range(k):
        if k == 0:
            return 0
            break
        if (kl[d]==x) and (kl[d+1]==y):
            return 0
            break
        kol += abs(int(x) - int(kl[d])) + abs(int(y) - int(kl[d + 1]))
        #print(kol, end=' ', sep=' ')
        d += 2
    #print()
    kol += abs(int(x) - n) * 2 + abs(int(x) - 1) * 2 + abs(int(y) - 1) * 2 + abs(int(y) - n) * 2
    srzn = kol / ob
    return srzn


def pri():
    d = 0
    a = []
    for i in range(1, n + 1):
        if xb > n or yb > n:
            print('wrong input')
            break
        for j in range(1, n + 1):
            x = xb - j
            y = yb - i
            if (abs(x) + abs(y) <= s):
                a += str(j)
                a += str(i)
                #print(1, end=' ')
                d += 1
            #else:
                #print('-', end=' ')
        #print()

    a.append(int(1))
    a.append(int(1))

    a.append(int(1))
    a.append(int(n))

    a.append(int(n))
    a.append(int(1))

    a.append(int(n))
    a.append(int(n))

    return d, a

def prit():
    d = 0
    a = []
    for i in range(1, n + 1):
        if xb > n or yb > n:
            #print('wrong input')
            break
        for j in range(1, n + 1):
            x = xb - j
            y = yb - i
            if (abs(x) + abs(y) <= s):
                a += str(j)
                a += str(i)
                #print(1, end=' ')
                d += 1
            #else:
                #print('-', end=' ')
        #print()

    return d, a



# все остальное
fail = open('.txt','r')
r = fail.readline()



#r=int(input('Введите R: '))# за кого играем
if r==1:

    f = fail.readline()
    #f= int(input('Введите F: '))  # тип поля
    #n = int(input('Введите N: '))  # размеры поля
    #k = int(input('Введите K: '))  # кол-во ловцов
    #s = int(input('Введите S: '))  # кол-во шагов
    #xb = int(input('Введите X беглеца: '))  # координата беглеца по оси x
    #yb = int(input('Введите Y беглеца: '))  # координата беглеца по оси y
    for i in range(k):
        kl.append(int(fail.readline()))
        kl.append(int(fail.readline()))
        # kl.append(int(input("Введите X ловца: ")))
        # kl.append(int(input("Введите Y ловца: ")))
    fail.close()

    if f==0:
        n = fail.readline()
        k = fail.readline()
        s = fail.readline()
        xb = fail.readline()
        yb = fail.readline()
        ob = k + 4
        d, a = pri()
        #print(d, a, sep='   ')
        max = -1
        for i in range(0, d * 2, 2):
            res = analiz(a[i], a[i + 1], ob)
            #print(a[i], a[i + 1], res, sep=' ')
            if (res > max):
                max = res
                xs = int(a[i]) - xb
                ys = int(a[i + 1]) - yb


        fail = open('.txt', 'w')
        fail.write(xs, ' ', ys)
        fail.close()

        #print(xs,' ',ys)

        d, a = pri()
    else:
        n = fail.readline()
        k = fail.readline()
        s = fail.readline()
        xb = fail.readline()
        yb = fail.readline()

        #f = int(input('Введите F: '))  # тип поля
        #n = int(input('Введите N: '))  # размеры поля
        #k = int(input('Введите K: '))  # кол-во ловцов
        #s = int(input('Введите S: '))  # кол-во шагов
        #xb = int(input('Введите X беглеца: '))  # координата беглеца по оси x
        #yb = int(input('Введите Y беглеца: '))  # координата беглеца по оси y
        for i in range(k):
            kl.append(int(fail.readline()))
            kl.append(int(fail.readline()))
            #kl.append(int(input("Введите X ловца: ")))
            #kl.append(int(input("Введите Y ловца: ")))
        fail.close()

        ob = k
        d, a = prit()
        #print(d, a, sep='   ')
        max = -1
        for i in range(0, d * 2, 2):
            res = analiz(a[i], a[i + 1], ob)
            #print(a[i], a[i + 1], res, sep=' ')
            if (res > max):
                max = res
                xs = int(a[i]) - xb
                ys = int(a[i + 1]) - yb

        fail = open('.txt', 'w')
        fail.write(xs, ' ', ys)
        fail.close()

        #print(xs,' ',ys)
        d, a = pri()
else:
    d=2
    for i in range(k):
        if kl[d]==1:
            if kl[d+1]==1:
                kl[d]+=1
                fail = open('.txt', 'w')
                fail.write('1 ', '0')
                fail.close()
                #print('1 ', '0')
            else:
                kl[d+1]-=1
                fail = open('.txt', 'w')
                fail.write('0 ', '-1')
                fail.close()
                #print('0 ', '-1')
        else:
            kl[d+1]-=1
            fail = open('.txt', 'w')
            fail.write('-1 ', '0')
            fail.close()
            #print('-1', '0')
        d+=2
        print()