age = 19

if(age > 18):
    print("you can enter")
print("move on")


if(age > 18):
    print("you can enter")
else:
    print("go see meat loaf")
print("move on")


if(age > 18):
    print("you can enter")
elif(age == 18):
    print("go see pink floyd")
else:
    print("go see meat loaf")
print("move on")


album_year = 1985

if(album_year < 1980) or (album_year > 1989):
    print("the album was made in the 70's or 90's")
else:
    print("the album was made in the 1980's")


if(album_year > 1979) and (album_year < 1990):
    print("the album was made in the 80's")
