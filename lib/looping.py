#!/usr/bin/env python3

def happy_new_year():
    num = 11
    while num >= 1:
        num -= 1
        if num > 1:
            print(num)
        elif num == 1:
            print(num)
            print("Happy New Year!")


happy_new_year()

def square_integers(int_list):
    new_int_list = list()
    for i in int_list:
        new_int_list.append(i ** 2)
    return new_int_list




def fizzbuzz():
    fb_num = 0
    while fb_num < 100:
        fb_num += 1
        if not fb_num % 15:
            print("FizzBuzz")
        elif not fb_num % 5:
            print('Buzz')
        elif not fb_num % 3:
            print('Fizz')
        else :
            print(fb_num)