import struct
from struct import pack

x = pack('>i4sh',7,b'jajo',8)
print(x)
t = struct.unpack('>i4sh',x)
print(t)