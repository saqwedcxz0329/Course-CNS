from base64 import b64encode
from base64 import b64decode

file = open('fake.crt', 'r')

cer = []
for line in file.readlines():
    cer.append(line)

print b64encode(''.join(cer))