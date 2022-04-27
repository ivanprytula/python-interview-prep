entered_sequence = input("Enter  sequence: ")
reversed_copy = entered_sequence[::-1]
if entered_sequence == reversed_copy:
    print("Palindrome")
else:
    print("Not a palindrome")
