#def analyze():
path = "/Users/james/Dropbox/SFU Courses/CMPT 275/AccelerometerReadings"
accel_Data = open(path)
#global x,y,z
x = []
y = []
z = []
for line in accel_Data:
	if(line.find('X') != -1):
		a,b,c,d = line.split('=')
		e,e1 =  b.split(',')
		f,f1 =  c.split(',')
		g,g1 =  d.split('\n')

		x.append(float(e))
		y.append(float(f))
		z.append(float(g))

x = "x ="+ str(x) + ";\n"
y = "y ="+ str(y) + ";\n"
z = "z ="+ str(z) + ";\n"

count_file = open("/Users/james/Dropbox/SFU Courses/CMPT 275/count", "w")
count = str(int(count_file.read()) + 1)
count_file.write(count)

out_file = open("/Users/james/Dropbox/SFU Courses/CMPT 275/accelData" + count, "w")

out_file.write(x)
out_file.write(y)
out_file.write(z)

accel_Data.close()
out_file.close()
count_file.close()