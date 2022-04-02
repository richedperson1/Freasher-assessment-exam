# Frequency count of string 
"""
Input of string is to be lowercase letter only.


input 1  : babdc
output 1 : a1b1c1d1

input 2  :  cbd
output 2 : b1c1d1


TC = O(n)
SC = O(1)

"""
print("=-="*25)
string = "cbd"

counting_alph = [0]*26
for word in string:
    local = ord(word)- ord('a')
    counting_alph[local]+=1

form = ""
for idx, count in enumerate(counting_alph):
    if count:
        local = chr(idx+97)
        form+=(local+str(count))

print(form)
"""
author : rutvikjaiswal195@gmail.com
Date   : 2 April 2022

"""
