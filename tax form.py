taxRate = 0.20
standardDeduction = 10000.0
dependentDeduction = 3000.0

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

taxableIncome = grossIncome - standardDeduction - (dependentDeduction * numDependents)
incomeTax = taxableIncome * taxRate

print("The income tax is " + str(incomeTax))