# msgs to user
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

# valid operators
sum_char = "+"
sub_char = "-"
mul_char = "*"
div_char = "/"

# other variables
memory = float(0)


# functions
# is_one_digit - validate if v has only one digit or not
# check - prints a message according to the values checked
#  choose_msg - return the correct msg based on the index received


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def choose_msg(msg_ind):
    if msg_ind == 10:
        return msg_10
    if msg_ind == 11:
        return msg_11
    if msg_ind == 12:
        return msg_12


# First user input sequence - enter operation
while True:
    calc = input(msg_0 + "\n").split()
    try:
        if calc[0] == "M":
            x = memory
        else:
            x = float(calc[0])

        oper = calc[1]

        if calc[2] == "M":
            y = memory
        else:
            y = float(calc[2])

        result = float()

        if oper != sum_char and oper != sub_char and oper != mul_char and oper != div_char:
            print(msg_2)
            continue
        else:
            check(x, y, oper)

        if oper == sum_char:
            result = x + y
        elif oper == sub_char:
            result = x - y
        elif oper == mul_char:
            result = x * y
        elif oper == div_char:
            if y != 0:
                result = x / y
            else:
                print(msg_3)
                continue
        print(result)

        # Second user input sequence - store result
        while True:
            answer = input(msg_4 + "\n")
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10  # this is hardcoded because we only want msg index equal to 10 or higher
                    # Third user input sequence - embarrassment loop
                    while True:
                        answer = input(choose_msg(msg_index) + "\n")
                        if answer == "y":
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break  # End of third user input sequence
                        elif answer == "n":
                            break
                        continue
                else:
                    memory = result
                break  # End of second user input sequence
            elif answer == "n":
                break  # End of second user input sequence

        # Fourth user input sequence - continue calculations decision
        while True:
            answer = input(msg_5 + "\n")
            if answer == "y" or answer == "n":
                break  # End of fourth input sequence

        # We go back to the beginning of the first user input sequence
        if answer == "y":
            continue
        break  # End of first user input sequence
    except ValueError:
        print(msg_1)
