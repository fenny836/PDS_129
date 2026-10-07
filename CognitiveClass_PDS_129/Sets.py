set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}

album_list = ["Michael Jackson", "Thriller", "Thriller", 1982]
album_set = set(album_list)

A = {"Thriller", "Back in Black", "AC/DC"}

A.add("NSYNC")
A.remove("NSYNC")

"AC/DC" in A
"who" in A

album_set1 = {"AC/DC", "Back in Black", "Thriller"}
album_set2 = {"AC/DC", "Back in Black", "The Dark side of the Moon"}

album_set3 = album_set1 & album_set2

album_set1.union(album_set2)

album_set3.issubset(album_set1)
