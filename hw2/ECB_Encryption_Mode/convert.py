from base64 import b64encode
from base64 import b64decode

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

# M1 = 'login=aaaaaaaaaaadminadminadmina&role=user&pwd=b'
# M1_token = '8n2PkdJBmr17jtQ32Irvvh9hnGDdugd2xO+7fjAR5pWC/pJ9qRrJpreAg/c2fEM4MC+buz+ArMs+2sLn29HY4g=='
# print b64decode(M1_token).encode('hex')

cipher = "f27d8f91d2419abd7b8ed437d88aefbe5ac49a12fdb7836d1b74b4f02bf66daf1313d6b21520ad765b54caa9f837ade31aff28f1838f67aa2941b08f833b9cfc302f9bbb3f80accb3edac2e7dbd1d8e2"
print b64encode(cipher.decode("hex"))
