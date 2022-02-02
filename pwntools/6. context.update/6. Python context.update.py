from pwn import *

context.update(arch = 'arm', os = 'android', bits = 64, endian = 'little')

print(context.update)