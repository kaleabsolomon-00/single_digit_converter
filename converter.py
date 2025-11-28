
Num=int(input("Enter a number: "))
while Num>9:
    Um=0
    str_num=str(Num)
    for digit in str_num:
        Um+=int(digit)
    Num=Um
print("Single digit:", Um, "revised is ", Um)
print(f" the revised amount is {Num}")
