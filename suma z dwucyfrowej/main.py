# sumowanie podajen dwócyfrowej liczby
two_digit_number = input("Type a two digit number: ")

#two_digit = str(two_digit_number) - nie ma potrzeby zamieniać na str, bo "input" daje str.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
suma = first_digit + second_digit
print(str(first_digit) + " + " + str(second_digit) + " = " + str(suma))