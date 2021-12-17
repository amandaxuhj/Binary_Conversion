def int_to_bin(number: int)-> str:
    binary_num =" "
    while number >0:
        if number%2 == 0:
            binary_num=binary_num+"0"
            number=number/2
        elif number%2 != 0:
            binary_num=binary_num+"1"
            number=(number-1)/2       
    reversed_binary=reversed(binary_num)
    corrected_binary=("".join((reversed_binary)))
    return corrected_binary

number=int(input("please enter an integer: "))

conversion_result = int_to_bin(number)
print(conversion_result)
