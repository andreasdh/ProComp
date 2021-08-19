p = float(input("How many in the population has gene variant a?: "))
q = float(input("How many in the population has gene variant A?: "))
if p + q == 1:
    AA = p**2  # Compute this first
    Aa = 2*p*q # Compute this second
    aa = q**2  # Compute this third
    print("1. Individuals with genotype AA:",AA)
    print("2. Individuals with genotype Aa:",Aa)
    print("3. Individuals with genotype aa:",aa)
else:
    print("Error: The sum of p and q is not equal to 1!")