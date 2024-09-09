#!/usr/bin/python3

flag=""
def reverse(string):
	return string[::-1]

def slicing(string,chunk_size=8):
	chunks=[string[i:i+chunk_size] for i in range(0,len(string),chunk_size)]
	return chunks

input_str = input("Enter your String - ")
reverse_str = reverse(input_str)
sliced_str = slicing(reverse_str,8)
ordering_str = sliced_str[::-1]
for i in ordering_str:
	flag+=i

print(flag)