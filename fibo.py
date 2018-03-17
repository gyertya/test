def print_out(i,fi,spaces_nr,spaces_fibo):
    formatting_nr = '%-'+str(spaces_nr+2)+'s'
    formatting_fibo = '%'+str(spaces_fibo)+'s'
    print(formatting_nr%(str(i+1)+". ")+formatting_fibo%fi[i])

    #old one
    #print(" "*(spaces_nr-len(str(i+1))),i+1,":"," "*(spaces_fibo-len(str(fi[i]))),fi[i])

import os
os.system('clear')

fibo = [0,1]

number_of_fibo = input("How many number(s) do you want to print out?")

print("Fibonacci sequance:")
for n in range(0,int(number_of_fibo)):
    if n > 1:
        fibo.append(fibo[n-1] + fibo[n-2])

for n in range (0,int(number_of_fibo)):
    print_out(n,fibo,len(number_of_fibo),len(str(fibo[int(number_of_fibo)-1])))
