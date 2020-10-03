#检测单字符异或
#4.txt中的60个字符的字符串之一 已由单字符XOR加密。
#找到它。

import linecache
#字符频率表
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def get_score(String):
	score=0
	for char in String:
		char=char.lower()
		if char in CHARACTER_FREQ:
			score+=CHARACTER_FREQ[char]
	return score

contents=linecache.getlines('4.txt')

output0 = ''
score0 = 0

for string in contents:
    hex_string = bytes.fromhex(string[:-1])
    for i in range(256):
        y = [chr(i^sx) for sx in hex_string]
        z = "".join(y)
        score = get_score(z)
        if(score>score0):
            score0 = score
            output0 = z

print(output0)    