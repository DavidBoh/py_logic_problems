#!/usr/bin/env python3

def main():
    while True:
        try:
            n = int(input('Please input the value in Fharenheit: '))
            break
        except:
            print('Invalid input, please input a number')
            continue

    counting = n - 32
    counting = ((counting*5)/9)
    print("The value in celcius is {}".format(counting))

if __name__ == '__main__':
    main()
