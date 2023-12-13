from cryptography.fernet import Fernet as fr

'''
def write_key():
    key = fr.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", 'rb')
    keys = file.read()
    file.close()
    return keys

master_psd = input("What is the master password? ")
key = load_key() + master_psd.encode()
fer = fr(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split('|')
            print("User: ", user + ",", " Password: ", fer.decrypt(pwd.encode()).decode())

def add():
    name = input("Account Name: ")
    psd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(psd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new passsword or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")
        continue

