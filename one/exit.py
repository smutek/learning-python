import sys

intruder = "Loki"
user = ""

while user != "Your name":
    print('Enter "your name"')
    user = input()
    if user == intruder:
        sys.exit('Intruder Alert')

print('Welcome ' + user + ', you are free to proceed.')
