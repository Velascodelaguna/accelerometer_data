#def analyze():
path = "/Users/james/Dropbox/SFU Courses/CMPT 275/Accelerometer data0"
accel_Data = open(path)
#global x,y,z
x = []
y = []
z = []
for i in accel_Data:
	a,b,c,d = map(str, i.split('='))
	e,e1 = map(str, b.split(','))
	f,f1 = map(str, c.split(','))
	g,g1 = map(str, d.split('\n'))

	x.append(float(e))
	y.append(float(f))
	z.append(float(g))

x = "x ="+str(x) + "\n"
y = "y ="+str(y) + "\n"
z = "z ="+str(z) + "\n"

out_file = open("/Users/james/Dropbox/SFU Courses/CMPT 275/accelData", "w")
out_file.write(x)
out_file.write(y)
out_file.write(z)
accel_Data.close()
out_file.close()