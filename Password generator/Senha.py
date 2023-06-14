import random
#Project: Password Generator v1.0
#Author: Frogg
#Version: 1.0


#Strings alphabet, Numbers and Symbols
alphabet = 'abcdefghijklmopqrstuvwxyz'
numbers = '1234567890'
symbols = '!@#$%¨&*()=/|\?'


#Welcome message to the user
print('*****************************************************')
print('**********Welcome to the Password Generator**********')
print('*****************************************************')

#Lenght of the password
print ('\nQual a quantidade de caracteres?')
lenght = int(input().upper().strip())

#Letters
print('\nDeseja Incluir letras maiúsculas? [Sim] [Não]')
letter = input().upper().strip()

#Numbers
print('\nDeseja incluir números? [Sim] [Não]')
number = input ().upper().strip()

#Symbols
print('\nDeseja inclir símbolos? [Sim] [Não]')
symbol = input().upper().strip()

#String of Output
password = ''

#String of random options
options = ''

#o usuario deseja ter letras Maiúsculas em sua senha
if letter == 'SIM': 
    options = options + alphabet.upper()
if letter == 'NÃO':
    options = options + alphabet

#o usuario deseja ter numero em sua senha
if number == 'SIM':
    options = options + numbers

#o usuario deseja ter simbolos em sua senha
if symbol == 'SIM':
    options = options + symbols

#Looping
while len(password) < lenght:
    password = password + random.choice(options)

print('Sua nova senha é:',password)

#finish program
input()