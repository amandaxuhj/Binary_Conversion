def bin_to_int(binary: str)->int:
    power=0
    ans=0
    for i in range(len(binary)-1,-1,-1):
        power=power+1
        ans=ans+int(binary[i])*(2**(power-1))
    print (ans)

binary = str(input("please enter an integer in binary: "))
bin_to_int(binary)

