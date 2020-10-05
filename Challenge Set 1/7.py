#ECB模式下的AES
#7.txt中的Base64编码内容 已通过AES-128在ECB模式下在密钥下进行了加密
#"YELLOW SUBMARINE".
#（区分大小写，不带引号；正好16个字符；我喜欢“ YELLOW SUBMARINE”，因为正好16个字节长，现在也可以这样做）。
#解密。毕竟，您知道钥匙。
#最简单的方法：使用OpenSSL :: Cipher并将其提供给AES-128-ECB作为密码。