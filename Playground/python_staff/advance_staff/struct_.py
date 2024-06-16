import struct
from struct import pack

if __name__ == "__main__":
    x = pack(">i4sh", 7, b"jajo", 8)
    print(x)
    t = struct.unpack(">i4sh", x)
    print(t)
