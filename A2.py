import random
import sys
import time
def ketik(s):
    for c in s + '\n':

	sys.stdout. write(c)
	sys.stdout. flush()

	time.sleep (random.random() * 0.5)

ketik('apakah ini sudah benar \nkalo salah bagaimana? \nokelah itu aza ya')
