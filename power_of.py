#!/usr/bin/env python3

print("Welcome. this program calcuates the value of x to the power of y")

def main():
    while True:
        try:
            base = int(input("Please input the value of the base: "))
            power = int(input("Please input the value of the exponent: "))
            if base < 0 or power < 0:
                print("Please input positive numbers only")
                continue
            break
        except:
            print("Invalid input, please input a number")
            continue

    #here we could have answer = base BUT it would throw wrong
    #results when power = 0
    #the solution is to initialize the answer variable with a value of 1
    # in the first iteration of the loop, answer var will be = to base
    answer = 1 
    i = 1

    while i <= power:
        answer = answer * base
        i += 1
    print("{} elevated to the power of {} is equals to {}".format(base,power,answer))

if __name__ == "__main__":
    main()
