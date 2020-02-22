import math
import PESrank

rank = PESrank.main(username, password, path)

if rank < 0:
    print("strength>100 bits")
else:
    if math.log2(rank) <= 30:
        print("strength<30 bits")
    elif math.log2(rank) <= 50:
        print("30<strength<50 bits")
    else:
        print("strength>50 bits")
    print("your password is a variant of a leaked password")

print("strong >50 bits, medium 30-50 bits, weak <30 bits")
