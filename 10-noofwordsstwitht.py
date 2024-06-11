sen=list(input("Enter a sentence: ").split())
count=0
for word in sen:
    if word.startswith("T") or word.startswith("t"):
        count+=1
print("Number of words starts with T is ",count)