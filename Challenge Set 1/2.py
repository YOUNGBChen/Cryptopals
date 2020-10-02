#编写一个函数，该函数接受两个等长缓冲区，并产生它们的XOR组合。
#如果您的函数可以正常工作，则在输入该字符串时：
#1c0111001f010100061a024b53535009181c
#...在进行十六进制解码后，以及针对以下内容进行XOR时：
#686974207468652062756c6c277320657965
#...应产生：
#746865206b696420646f6e277420706c6179

string1 = '1c0111001f010100061a024b53535009181c'
string1 = bytes.fromhex(string1)

string2 = '686974207468652062756c6c277320657965'
string2 = bytes.fromhex(string2)

result = ''


for x,y in zip(string1,string2):
    result = result + (chr(x^y))

result = result.encode()
output = bytes.hex(result)

print(result)
print(output)