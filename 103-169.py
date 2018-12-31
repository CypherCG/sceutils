from scetypes import *

ENC_KEY = binascii.a2b_hex('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
ENC_IV =  binascii.a2b_hex('AF5F2CB04AC1751ABF51CEF1C8096210') #set like this until real iv is found

SCE_KEYS = KeyStore()
SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SPKG, 
    0, 
    '2E6F4751D15B06C51F572A9306E52DD7007EA56A31D459EC6D3681AB08625501', 
    'B3D541A568751DF8F4833BAB4EFE0537', 
    0x00000000000, 
    0xFFFFFFFFFFF, 
    SelfType.NONE
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SRVK, 
    0, 
    '4648164DB9E67009456C7CA6F2378835FD678539B36B3DE6F1C604B7D4258141', 
    '6EC8AD67993DAE75675F0AFFDE5C41F3', 
    0x00000000000, 
    0xFFFFFFFFFFF,
    SelfType.NONE
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
    1, 
    '7A7FB1560DCD121CEA5E11B90124B13282752F2D5B95D75036AB3A29BB3BD2AB', 
    '6C71642A042A041F1EE3094070B009BE', 
    0x00000000000, 
    0xFFFFFFFFFFF,
    SelfType.BOOT
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
    1, 
    '9D4E4CE92EA1C4576EB9601EC43EC03AAE8EC324ECF6DE01E918E61D2223EE55', 
    'CFEA3CCBA454D3279AD7CB0510431434', 
    0x00000000000, 
    0xFFFFFFFFFFF,
    SelfType.SECURE
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
	1, 
	'B4AAF62D48FBD898C240308A9773AFE57B8A18D783F0B37932BB21B51386A9A0', 
    '8CD162C5C613376F3E4BEA0B8FD5A3D0', 
    0x00000000000, 
    0xFFFFFFFFFFF, 
    SelfType.KERNEL
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
    1, 
    '613AD6EAC63D4E14F51A8C6AF18C66621968323B6F205B5E515C16D77BB06671', 
    'ADBDAA5041B2094CF2B359301DE64171', 
    0x00000000000, 
    0xFFFFFFFFFFF, 
    SelfType.USER
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
    2, 
    '0F2041269B26D6B7EF143E35E83E914629A92F50F3A4CEE14CDFF63AEC641117', 
    '07EF64437F0CB6995E6D785E42796C83', 
    0x00000000000, 
    0xFFFFFFFFFFF, 
    SelfType.USER
)