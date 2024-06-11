tuple1=input("Enter elements of tuple1: ").split()
tuple2=input("Enter elements of tuple2: ").split()

resTuple=tuple1+tuple2

search=int(input("Enter search element:"))
inde=resTuple.index(search)
countocc=resTuple.count(search)

print(resTuple)
print(inde)
print(countocc)
