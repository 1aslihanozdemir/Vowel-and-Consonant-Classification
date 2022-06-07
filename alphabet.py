###########
import string


Alphabet = "aeiouAEIOUbcdfghjklmnprstvyzqxBCDFGHJKLMNPRSTVYZXQ"
vowels ="aeiouAEIOU"


vowels_list=[]
consonant_list=[]



for i in Alphabet:
    if i in vowels:
        vowels_list.append(i)
    else:
        consonant_list.append(i)

    
print("vovels: ",vowels_list)
print("consonants: ",consonant_list)
