print("Hello Python 101")

L=["Michael Jackson",10.1,1982]

Ratings=(10,9,6,5,10,8,9,6,2)

album_list=["Michael Jackson","Thriller","Thriller",1982]
album_set=set(album_list)

{"key1":1,"key2":"2","key3":[3,3,3],"key4":(4,4,4),('key5'):5}

age=19

if (age>18):
    print("you can enter")
else:
    print("go see meat loaf")

if (age>18):
    print("you can enter")
elif(age==18):
    print("go see pink floyd")
else:
    print("go see meat loaf")

for i in range(0,5):
    print(i)

squares=["orange","orange","purple","blue"]

i=0
while (squares[i]=='orange'):
    print(squares[i])
    i=i+1

def fun(a):
  """add 1 to a"""
  b=a+1;
  print(a,"+1=",b)
  return b

fun(5)

class Circle:
    def __init__(self,radius,color):
        self.radius=radius
        self.color=color

RedCircle=Circle(10,"red")
