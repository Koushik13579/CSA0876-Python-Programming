A = int(input("Enter lower limit:"))
B = int(input("Enter upper limit:"))
print("Non primes in the given range are: ",end="")
for num in range(A, B+1):
 if num > 1:
     for i in range(2, num):
            if num % i == 0:
                print(num, end=", ")
                break