sentence=input("Enter a sentence: ")
sen =sentence.upper()
count=0
for i in range(len(sentence)):
    if sentence[i]==" ":
        count+=1
print(sen,",",count)