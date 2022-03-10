#nikitha prabhu

import math #for factorial function

x = int(input('Pick a number. This function will tel you if your number is even.: '))
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(is_even(x))

x = float(input('Pick a number. This function will tell you if your number is an integer.: '))
def is_int(x):
    if x % 1 == 0:
        return True
    else:
        return False
print(is_int(x))

x = int(input("Choose a number. This function will return the sum of your number's digits"))
def digit_sum(x):
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum
print(digit_sum(x))
    
x = int(input('What number would you like the factorial of? '))
def factorial(x):
    factorialx = int(math.factorial(x))
    return factorialx
print(factorial(x))     
    
x = int(input('Input a number. This function will tell you if it is prime.'))
def is_prime(x):
    for n in range(2, x-1):
        if x % n == 0: 
            return True
        else:
            return False
print(is_prime(x))

x = input('What string would you like the reverse of?')
def reverse(x):
    final = ""
    for i in x:
        final = i + final
        return final
print(reverse(x))
        
    
string = input('What word do you want without vowels? ')
def anti_vowel(string):
    vowels=["a","A","e","E","i","I","o","O","u","U"]
    text_input= ""
    for x in string:
        if x not in vowels: 
            text_input = text_input + x
    return text_input

print(anti_vowel(string))

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10} #dictionary for scrabble score

word = input('What word would you like the scrabble score of?')

def scrabble_score(word):
  sumScore = 0
  for c in word:
    for item in score:
      if c.lower() == item:
        sumScore += score[item]
        print(str(item) + ":" + (str(score[item])))
  return sumScore      
print(scrabble_score(word))  
    
def censor(text, word):
    text = text.split()
    for i in range(0, len(text)):
        if text(i) == word:
            text(i) = "*"*len(text(i))
        return " ".join(text)
print(censor("this", "this"))


def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total = total + 1
    return total
print(count(3, 2, 1, 1), 1)

def purify(numbers):
    flist = []
    for i in numbers:
        if i % 2 == 0: #checking if it is an odd number
            flist.append(i)
    return flist
print(purify[1, 2, 3])

def product(x):
    total = 1 #not zero because it would be zero when multiplied
    for i in x:
        total = total * 1
    return total
print(product[4, 5, 5])

def remove_duplicates(x):
    alist = []
    for i in x:
        if i not in alist: #so there won't be duplicates
            alist.append(i)
    return alist
print(remove_duplicates(1,1,2,2))

def median(list):
        list.sort()
        if len(list) % 2 == 0:
            return(list[int(len(list)/2)] + list[int(len(list)/2 - 1)]) / 2
        else:
            return (list[int(len(list)/2)]) + list[int(len(list)/2 - 1)]
