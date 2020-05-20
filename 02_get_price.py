# not blank function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        try:
            response = int(input(question))
            has_errors = ""

            if num_ok != "yes":
                # look at each character in the string and if it's a number
                for letter in response:
                    if letter.isdigit():
                        has_errors = "yes"
                        break
        except ValueError:
            print("Please enter in a number.")
            continue

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# main routine goes here

item_to_sell = not_blank("How much is the item? ",
                         "Your response cannot have letters or be blank",
                         "yes")

print("The price of your item is: ${}".format(item_to_sell))


