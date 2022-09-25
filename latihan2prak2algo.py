import math

t1 = float(input(" masukkan lattitude daerah pertama = "))
g1 = float(input(" masukkan longitude daerah pertama = "))

t2 = float(input(" masukkan lattitude daerah kedua = "))
g2 = float(input(" masukkan longitude daerah kedua = "))

dlat = t2 - t1
dlon = g2 - g1

a = math.sin(math.radians(dlat/2)) ** 2 + math.cos(math.radians(t1))
math.cos(math.radians(t2)) * math.sin(math.radians(dlon/2)) ** 2

# Versi Arc sinus
c = 2 * math.asin(math.sqrt(a))

# Versi Arc tangen 2
r = 6371.01

print("jarak antara dua titik adalah" , c*r , "kilometer")
