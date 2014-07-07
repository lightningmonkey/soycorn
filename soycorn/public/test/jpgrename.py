import os
import glob

for x in glob.glob('[0-9][0-9][0-9].jpg'):
	sep = x.split(".")
	os.rename(x, sep[0] + ".JPG")
