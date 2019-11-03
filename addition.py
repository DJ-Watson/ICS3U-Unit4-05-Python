#!/usr/bin/env python3

# Created by DJ Watson
# Created on October
# this program makes the user adds 5 numbers of their choice together


def main():
    answer = 0

    # input
    ln = input("how many numbers do you want to add: ")
    print("")
    # process and output
    try:
        loop_c = int(ln)
        for loop_n in range(loop_c):
            numinput = input("enter positive number: ")
            try:
                intcheck = int(numinput)
                if intcheck < 0:
                    continue
                else:
                    answer += intcheck
            except ValueError:
                continue
        print("")
        print(answer)
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
