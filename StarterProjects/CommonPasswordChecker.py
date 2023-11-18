def check_password(password: str):
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
    # print(common_passwords)

    for i, common_password in enumerate(common_passwords, start=1):  # enumerate the common passwords and start at 1
        if password == common_password:
            print(f'{password}: Denied (#{i})')
            return
    print(f'{password}: (Unique)')


def main():
    while True:
        user_password: str = input('Enter a password (or type "exit" to quit): ')

        if user_password == 'exit':
            print('Quiting..')
            break

        if user_password.strip():  # checking if the entered password is not empty
            check_password(user_password)
            print("Try again")
        else:
            print('Password cannot be empty. Try again.')


if __name__ == '__main__':
    main()

# insert a check that prevents the user to enter nothing
