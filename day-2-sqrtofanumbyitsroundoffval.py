x = 36
sqrt = x
while sqrt*sqrt>x:
    sqrt=(sqrt+x//sqrt)// 2
print("square root of",x,"is",sqrt)