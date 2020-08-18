#genrates a user name from the users first and last name
first_name = input('first name: ')
last_name = input('last name: ')


def username_generator(first_name, last_name):
    username = ""
    while len(username) < 10:
        username += first_name[0]
        username += last_name[0:len(last_name)]
        if len(username) < 10:
            username += 'x'
    return username

print(username_generator(first_name, last_name))