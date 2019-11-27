filename='guest.txt'

name=input('enter your name:')
with open(filename,'w') as file_object:
    file_object.write(name)

with open(filename,'r') as file_object:
    line=file_object.read()

print(f"the guest name is:{line}")
