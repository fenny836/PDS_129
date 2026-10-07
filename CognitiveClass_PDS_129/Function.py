
def f1(input):
    """add 1 to input"""
    output = input + 1
    return output


def f2(input):
    """add 2 to input"""
    output = input + 2
    return output


album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]

L = len(album_ratings)
S = sum(album_ratings)
sorted_album_ratings = sorted(album_ratings)
album_ratings.sort()


def add1(a):
    b = a + 1
    return b


add1(5)
help(add1)


def mul(a, b):
    c = a * b
    return c


mul(2, 3)
mul(10, 3.14)


def MJ():
    print("Michael Jackson")


MJ()


def nowork():
    pass


print(nowork())


def printstuff(stuff):
    for i, s in enumerate(stuff):
        print("Album", i, "Rating is", s)


album_ratings = [10.0, 8.5, 9.5]
printstuff(album_ratings)


def ArtistNames(*names):
    for name in names:
        print(name)


ArtistNames("Michael Jackson", "AC/DC")


def AddDC(y):
    x = y + "DC"
    print(x)
    return x


x = "AC"
z = AddDC(x)


def Thriller():
    Date = 1982
    return Date


Thriller()


def ACDC(y):
    print(Ratings)
    return Ratings + y


Ratings = 9
Z = ACDC(1)
print(Ratings)


def PinkFloyd():
    global claimedSales
    claimedSales = 45_000_000
    return claimedSales


PinkFloyd()
print(claimedSales)

