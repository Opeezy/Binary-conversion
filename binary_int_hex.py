from time import sleep

binary = input("Input binary string to be converted: ")
new_binary_string = ""
byte_count = 0
max_power = 0

#check if valid binary string
for bit in binary:
    if bit != "0" and bit != "1":
        binary = input("Your input is not a binary string. Try again... ")
    elif bit == "0" or bit == "1":
        new_binary_string += str(bit)
while len(new_binary_string)%4 != 0:
    new_binary_string = "0" + new_binary_string

#check for size of binary string
for i in range(0,len(new_binary_string),4):
    byte_count += 1

string_size = len(new_binary_string)
max_power = (string_size-1)
total_sum = 0

#convert binary to integer
for bit in new_binary_string:
    if bit == "1":
        total_sum = total_sum + (2**(max_power))
        max_power = max_power-1
    else:
        max_power = max_power-1

#convert new total_sum variable to hexadecimal
cant_divide = False
result = total_sum
remainder = 0
hex_string = ""

while result != 0:
    remainder = result%16
    result = result//16
    #remainder + hex_string
    if 0 <= remainder < 10:
        hex_string = str(remainder) + hex_string
    elif 10 <= remainder < 16:
        if remainder == 10:
            hex_string = "A" + hex_string
        elif remainder == 11:
            hex_string = "B" + hex_string
        elif remainder == 12:
            hex_string = "C" + hex_string
        elif remainder == 13:
            hex_string = "D" + hex_string
        elif remainder == 14:
            hex_string = "E" + hex_string
        elif remainder == 15:
            hex_string = "F" + hex_string
    else:
        print("Something went wrong... bye!")
        print(remainder)
        break

print("Initial binary value...")
sleep(.5)
print(new_binary_string + "\n")
sleep(.5)
print("Integer value...")
sleep(.5)
print(str(total_sum) + "\n")
sleep(.5)
print("Hexadeciaml value...")
sleep(.5)
print(hex_string)
