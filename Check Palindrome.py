#Check if Palindrome - Checks if the string entered by the user is a palindrome. 
#That is that it reads the same forwards as backwards like “racecar”

if __name__ == '__main__':
    input = input('Enter word you wish to check: ').lower()
    backward = input[::-1]
    if input == backward:
        print("Congradulations it is a palindrome")
    else: print('Not a palindrome')
