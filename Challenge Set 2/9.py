#实施PKCS＃7填充
#分组密码将固定大小的明文块（通常为8或16个字节）转换为密文。但是，我们几乎永远都不想转换单个块。我们会加密大小不规则的邮件。
#解决不规则大小消息的一种方法是填充，创建纯文本，该纯文本是块大小的偶数倍。最流行的填充方案称为PKCS＃7。
#因此：通过将填充字节数附加到块的末尾，将任何块填充到特定的块长度。例如，
#"YELLOW SUBMARINE"
#...填充为20个字节将是：
#"YELLOW SUBMARINE\x04\x04\x04\x04"

def pkcs7_pad(message,block_size):
    if len(message) == block_size:
        return message
    ch = block_size - len(message) % block_size
    return message + bytes([ch] * ch)

def main():
    message = b'YELLOW SUBMARINE'
    b = pkcs7_pad(message,20)
    print(b)
    
if __name__ == "__main__":
    main()
    