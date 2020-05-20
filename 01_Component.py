# not blank function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in the string and if it's a number
            for letter in response:
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# main routine goes here

item_to_sell = not_blank("What are you planning to sell? ",
                         "Your response cannot have numbers or be blank",
                         "no")

print("You are selling {}".format(item_to_sell))


