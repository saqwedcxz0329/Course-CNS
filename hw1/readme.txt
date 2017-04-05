Language: python2.7

4. Classical Cipher
	Execute: 
	python ./src/code4.py

	How to get the flag:
	In round2, it will print 25 possible sentences, find the most like an English sentence and enter it
	Example:
	Jqygxgt oqtg cfxcpegf vgejpkswgu uwej cu
	Ipxfwfs npsf bewbodfe ufdiojrvft tvdi bt
	However more advanced techniques such as
	Gnvdudq lnqd zcuzmbdc sdbgmhptdr rtbg zr
	Fmuctcp kmpc ybtylacb rcaflgoscq qsaf yq
	Eltbsbo jlob xasxkzba qbzekfnrbp prze xp
	Dksaran ikna wzrwjyaz paydjemqao oqyd wo
	Cjrzqzm hjmz vyqvixzy ozxcidlpzn npxc vn
	Biqypyl gily uxpuhwyx nywbhckoym mowb um
	Ahpxoxk fhkx twotgvxw mxvagbjnxl lnva tl
	Zgownwj egjw svnsfuwv lwuzfaimwk kmuz sk
	Yfnvmvi dfiv rumretvu kvtyezhlvj jlty rj
	Xemuluh cehu qtlqdsut jusxdygkui iksx qi
	Wdltktg bdgt pskpcrts itrwcxfjth hjrw ph
	Vcksjsf acfs orjobqsr hsqvbweisg giqv og
	Ubjrire zber nqinaprq grpuavdhrf fhpu nf
	Taiqhqd yadq mphmzoqp fqotzucgqe egot me
	Szhpgpc xzcp loglynpo epnsytbfpd dfns ld
	Rygofob wybo knfkxmon domrxsaeoc cemr kc
	Qxfnena vxan jmejwlnm cnlqwrzdnb bdlq jb
	Pwemdmz uwzm ildivkml bmkpvqycma ackp ia
	Ovdlcly tvyl hkchujlk aljoupxblz zbjo hz
	Nuckbkx suxk gjbgtikj zkintowaky yain gy
	Mtbjajw rtwj fiafshji yjhmsnvzjx xzhm fx
	Lsaiziv qsvi ehzergih xiglrmuyiw wygl ew

	Enter: However more advanced techniques such as
	
	In round4, it will print some numbers, find a list of numbers it will replay
	Example:
	9 13 4 6 2 6 2 2 13 14 17 6 11 2 9 13 4 6 2 6 2 2 13 14 17 6 11 2 9 13 4 6 2 6 2 2 13 14 17 6

	Enter: 9 13 4 6 2 6 2 2 13 14 17 6 11 2

	Finally, you can get the flag
	(Sometimes it will be blocked, please stop the program and try it again)

5. Google can beat this
	Execute:
	nc 140.112.31.109 10001
	python ./src/code5.py

	How to get the flag:
	Connecting to the server, and find out the rightmost 24 bits in sha1(x). Opening code5.py and modify the target's value to the rightmost 24 bits. Executing code5.py. If it find the collision, it will print M1 and M2. Enter M1 and M2, you can get the flag. If not found after two mintes, try it again, until it find the collision. It is a little bit of your luck.


	Example:
	nc 140.112.31.109 10001
	Give me the X such that sha1(X)=??????????????????????????????????af6d6b

	code5.py
	target = "af6d6b"

8. Man in the Middle
	Execute:
	python ./src/code8.py

	How to get the flag:
	Executing code8.py. After it find the password, it will print the flag.