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
    'DAE4B0F901E338DEFF3CCDBDEA1E2FDEA9926BB98CB182443CC0C0F7FAE428EE', 
    '18D925FA885C7E28A9CFF458C24D8BED', 
    0x00000000000, 
    0xFFFFFFFFFFF,
    SelfType.NONE
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
    1, 
    'B1B936B512F9A16E51B948622B26F15C53680C77AC332EC25846B839520393EC', 
    '90D527BAF7296B5B6A576CFA6B54D266', 
    0x00000000000, 
    0xFFFFFFFFFFF,
    SelfType.BOOT
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
    1, 
    'B1B6FEB39A8BD7A2AC584D435E150C624F560D3EFB03E745C575E0844569E2D0', 
    '89B4E6BAB03B03D49BF0FC927FEA8659', 
    0x00000000000, 
    0xFFFFFFFFFFF, 
    SelfType.SECURE
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
    1, 
    '849AF7E8DE5B9C28C38CA74963FCF155E0F200FB08185E46CDA87790AAA10D72', 
    '88710E219454A3CBF6D382D4BBD22BFC', 
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
    3, 
    '3AFADA34660C6515B539EBBBC79C9C0ADA4337C32652CA03C6DD21A1D612D8F4', 
    '7F98A137869B91B1EB9604F81FD74C50', 
    0x00000000000, 
    0xFFFFFFFFFFF, 
    SelfType.USER
)

SCE_KEYS.register(
    KeyType.METADATA,
    SceType.SELF, 
    4, 
    '8FF491B36713E8AA38DE30B303689657F07AE70A8A8B1D7867441C52DB39C806', 
    'D9CC7E26CE99053E48F9BEF1CB93C184', 
    0x00000000000, 
    0xFFFFFFFFFFF, 
    SelfType.USER
)