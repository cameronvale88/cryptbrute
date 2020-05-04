#!/usr/bin/env python3

import pycipher
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# def vine():
#     url="https://guballa.de/vigenere-solver"
#     webbrowser.open(url)

# def vine(ciphertext):
#     for x in range(0, 3):
#         browser=webdriver.Chrome('/home/administrator/Public/python/python_samples/pentest/python_cipher/chromedriver')
#         browser.get('https://guballa.de/vigenere-solver')
#         browser.maximize_window()
#         browser.find_element_by_id("cipher").send_keys(ciphertext)
#         # browser.execute_script("window.open('');")
#         obj=Select(browser.find_element_by_name("variant"))
#         obj.select_by_index(x)
#         obj2=Select(browser.find_element_by_name("lang"))
#         obj2.select_by_index(1)
#         browser.find_element_by_name("key_len").clear()
#         browser.find_element_by_name("key_len").send_keys("3-40")
#         obj4=browser.find_element_by_name('break')
#         obj4.click()
#         # input("press enter to continue  ")

def vine(ciphertext):
    browser=webdriver.Chrome('PLACE THE ABSOLUTE PATH TO THE CHROMIUM DRIVER')
    browser.get('https://guballa.de/vigenere-solver')
    browser.maximize_window()
    browser.find_element_by_id("cipher").send_keys(ciphertext)
    obj=Select(browser.find_element_by_name("variant"))
    obj.select_by_index(0)
    obj2=Select(browser.find_element_by_name("lang"))
    obj2.select_by_index(1)
    browser.find_element_by_name("key_len").clear()
    browser.find_element_by_name("key_len").send_keys("3-40")
    obj4=browser.find_element_by_name('break')
    obj4.click()
    

    browser.execute_script("window.open('about:blank', 'tab2');")
    browser.switch_to.window("tab2")
    browser.get('https://guballa.de/vigenere-solver')
    browser.find_element_by_id("cipher").send_keys(ciphertext)
    obj=Select(browser.find_element_by_name("variant"))
    obj.select_by_index(1)
    obj2=Select(browser.find_element_by_name("lang"))
    obj2.select_by_index(1)
    browser.find_element_by_name("key_len").clear()
    browser.find_element_by_name("key_len").send_keys("3-40")
    obj4=browser.find_element_by_name('break')
    obj4.click()

    browser.execute_script("window.open('about:blank', 'tab3');")
    browser.switch_to.window("tab3")
    browser.get('https://guballa.de/vigenere-solver')
    browser.find_element_by_id("cipher").send_keys(ciphertext)
    obj=Select(browser.find_element_by_name("variant"))
    obj.select_by_index(2)
    obj2=Select(browser.find_element_by_name("lang"))
    obj2.select_by_index(1)
    browser.find_element_by_name("key_len").clear()
    browser.find_element_by_name("key_len").send_keys("3-40")
    obj4=browser.find_element_by_name('break')
    obj4.click()


def atbash(ciphertext):
    output=pycipher.Atbash().decipher(ciphertext, keep_punct=True)
    print("Atbash output: " + output )
    f=open('atbash.txt', 'w')
    f.write(output)
    f.close()

def caesar(ciphertext):
    print("CAESAR CIPHER OUTPUT: ")
    f=open('casear.txt', 'w' )
    for x in range(3,31):
        plaintext = pycipher.Caesar(x).decipher(ciphertext, keep_punct=True)
        f.write(plaintext +"\n")
        print(plaintext)
    f.close()

def rail(ciphertext):
    print("RAIL CIPHER OUTPUT: ")
    f=open("Rail.txt", 'w')
    for x in range(2,31):
        plaintext = pycipher.Railfence(x).decipher(ciphertext, keep_punct=True)
        f.write(plaintext + "\n")
        print(plaintext)
    f.close()

def rot13(ciphertext):
    plaintext = pycipher.Rot13().decipher(ciphertext, keep_punct=True)
    print("ROT13 OUTPUT: " + plaintext)
    f=open('ROT13.txt', 'w')
    f.write(plaintext)
    f.close()

def main():
    ciphertext=input("Please type cipher text: ")
    print("This program is designed for simple cipher that should decipher into something readable.")
    print("\n")
    print("If none of the output looks readable, then try another cipher and/or there may be an error.")
    print("The first cipher we will try is vigenere. We will go to the webpage: https://guballa.de/vigenere-solver")
    input("Please press enter to continue.")
    vine(ciphertext)
    print("\n")
    print('-----------------------------------------')
    atbash(ciphertext)
    print('-----------------------------------------')
    input("Press ENTER to continue.")
    print('-----------------------------------------')
    rot13(ciphertext)
    print('-----------------------------------------')
    input("Press ENTER to continue.")
    print('-----------------------------------------')
    caesar(ciphertext)
    print('-----------------------------------------')
    input("Press ENTER to continue")
    print('-----------------------------------------')
    rail(ciphertext)



if __name__ == '__main__': 
    main() 
