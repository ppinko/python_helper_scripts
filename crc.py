from crccheck.crc import CrcBase

arr = [ 7, 88, 205, 21 ]

class Crc4(CrcBase):
    _names = ('CRC-4')
    _width = 4
    _poly = 0x9
    _initvalue = 0x000000
    _reflect_input = True
    _reflect_output = True
    _xor_output = 0x000000
    _check_result = 0x2
    _residue = 0x000000

crc4 = Crc4()
crc4.selftest() # test for default array b'123456789'
crc4.selftest(arr, 0xd)

class Crc8(CrcBase):
    _names = ('CRC-8')
    _width = 8
    _poly = 0x7
    _initvalue = 0x000000
    _reflect_input = False
    _reflect_output = False
    _xor_output = 0x000000
    _check_result = 0xf4
    _residue = 0x000000

crc8 = Crc8()
crc8.selftest() # test for default array b'123456789'
crc8.selftest(arr, 0x78)

class Crc16(CrcBase):
    _names = ('CRC-16')
    _width = 16
    _poly = 0x1021
    _initvalue = 0x000000
    _reflect_input = False
    _reflect_output = False
    _xor_output = 0x000000
    _check_result = 0x31c3
    _residue = 0x000000

crc16 = Crc16()
crc16.selftest() # test for default array b'123456789'
crc16.selftest(arr, 0x84de)

class Crc32(CrcBase):
    _names = ('CRC-32')
    _width = 32
    _poly = 0x04C11DB7
    _initvalue = 0xFFFFFFFF
    _reflect_input = False
    _reflect_output = False
    _xor_output = 0xFFFFFFFF
    _check_result = 0xfc891918
    _residue = 0x000000

crc32 = Crc32()
crc32.selftest() # test for default array b'123456789'
crc32.selftest(arr, 0xc476f68f)

class Crc24(CrcBase):
    _names = ('CRC-24')
    _width = 24
    _poly = 0x864CFB
    _initvalue = 0x000000
    _reflect_input = False
    _reflect_output = False
    _xor_output = 0x000000
    _check_result = 0xcde703
    _residue = 0x000000

crc24 = Crc24()
crc24.selftest() # test for default array b'123456789'
crc24.selftest(arr, 0x724ec)
