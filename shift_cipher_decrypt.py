#!/usr/bin/python

'''Read text from the file'''
def read_text_from_file(filename):
    f = open(filename,'r')
    text = f.readline()
    text = "".join(text)
    return text.strip()

'''Transform text into array'''
def text_to_list(text):
    l = list(text)
    return l

'''Print array into regular string'''
def print_list(l):
    print(''.join(l))

'''Get int value of a letter'''
def let_int(letter):
    return ord(letter)

'''''''''''''''''''''''''''''''''''''''''''''''''''
    Shift down a letter where z precede a
    a = 97, z = 122
    if shifted letter is more than 122 (z),
    new letter int = ((letter_int % 122) + 97) -1
'''''''''''''''''''''''''''''''''''''''''''''''''''
def shift_letter(letter, num_shift):
    letter_to_int = ord(letter)
    shifted_int = letter_to_int + num_shift
    if shifted_int > 122:
        shifted_int = shifted_int % 122
        shifted_int = shifted_int + 97 - 1
    s_letter = chr(shifted_int)
    return s_letter

'''Decrypt the message using a key'''
def shift_cipher_decryption(lst, num_shift):
    l = list()
    for let in lst:
        shifted_let = let
        if let.isalpha():
            shifted_let = shift_letter(let, num_shift)
        l.append(shifted_let)
    return l

'''Decrypt the message using all keys'''
def shift_cipher_decryption_all_keys(lst):
    for i in range(1,27):
        c_list = text_to_list(ciphertext.lower())       #transform the text to array/list
        l = shift_cipher_decryption(lst, i)
        print('Shift by ' + str(i) + ':\t' + ''.join(l))

ciphertext = read_text_from_file('cshift.txt')  #get text from file
print('Ciphertext:\t' + ciphertext +'\n')       #print ciphertext
c_list = text_to_list(ciphertext.lower())       #transform the text to array/list
shift_cipher_decryption_all_keys(c_list)        #decipher using all keys
