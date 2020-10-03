#实现重复键异或
#这是英语的重要著作的开头节：
#Burning 'em, if you ain't quick and nimble
#I go crazy when I hear a cymbal
#使用重复密钥XOR在密钥“ ICE”下对其进行加密。
#在重复密钥XOR中，您将按顺序应用密钥的每个字节。明文的第一个字节将与I，下一个C，下一个E，然后又是第4个字节进行XOR运算，依此类推。
#它应该显示为：
#0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
#a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
def xor_repeat(string,key):
    key_len = len(key)
    result=''
    for index,ch in enumerate(string):
        n = index % key_len
        b = chr(ord(key[n]) ^ ord(ch))
        result = result + b
    return result

def main():
    string1 = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    key = 'ICE'
    output = xor_repeat(string1,key).encode()
    output = bytes.hex(output)
    print(output)

if __name__ == '__main__':
	main()