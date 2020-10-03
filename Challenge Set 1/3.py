#十六进制编码的字符串：
#1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
#...已针对单个字符进行XOR。找到密钥，解密消息。
#您可以手动执行此操作。但是请不要：编写代码为您完成此任务。
#怎么样？设计一些“计分”英文明文的方法。字符频率是一个很好的指标。评估每个输出并选择得分最高的输出。


#字符频率表
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def get_score(string):
	score=0
	for char in string:
		char=char.lower()
		if char in CHARACTER_FREQ:
			score+=CHARACTER_FREQ[char]
	return score

string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
output0 = ''
score0 = 0
x = bytes.fromhex(string)
for i in range(256):
    y = [chr(i^sx) for sx in x]
    z = "".join(y)
    score = get_score(z)
    if(score>score0):
        score0 = score
        output0 = z

print(output0)    


