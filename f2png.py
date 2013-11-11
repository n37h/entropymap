import sys
import os.path
import png

# ToDo: 
#   add usage instrucktions
#   add argsparser
#   add options for blocking based mapping

def stoInt(b):
	h = b.encode("hex")
	if h=='':
		h="0"
	r = int(h,16)
	return r

def colorizeByte(myByte) :
	r=0
	g=0
	b=0
	# if control character, r=0 for ascii/ext ascii
	if myByte < 32:
		r=8*myByte

	# if extended ascii char , else  = 0
	if myByte > 127:
		b= ( myByte + 255) / 2

	# b ~0 for control chars, >0 for ascii / ext ascii
	g = myByte

	return [r,g,b] 




f = open (sys.argv[1] , 'r+')

s = f.read()

l = len(s)

print l

# linewidth

w = int(sys.argv[2])

# seekpoint

s = int(sys.argv[3])

# the bitmap
p =  []

# row index, top down
rowidx = 0 

# pixelcounter, max 128 per line ( 0 - 127)
pixidx = 0

f.seek(s)

# number of pixes written
n = 0
while l > 0: 
	row = []	

	pixidx = 0

	while pixidx < w:
		b = f.read(1)
		cb = colorizeByte(stoInt(b))
		row.append( cb[0] )
		row.append( cb[1] )
		row.append( cb[2] )
		pixidx+=1
		n+=1
		l-=1
	
	p.append(row)

print len(p)

print p[0][0]

png.from_array(p, 'RGB').save(os.path.basename(sys.argv[1]) + '.png')

f.close()
