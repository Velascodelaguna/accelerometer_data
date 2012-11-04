'''
Format accelerometer data so that it is easy to
input to MATLAB. Gather statistics such as mean values,
min, max, range, and vector sum.

By James Velasco and Brian Mo
Same Level Software
'''

import math

def get_time(time):
	last_colon = time.rfind(':')
	time_sec = time[last_colon + 1 :]
	return time_sec

def get_mean(num_list):
	return math.fsum(num_list)/len(num_list)

def get_vector_sum(x, y, z):
	return math.sqrt((x * x) + (y * y) + (z * z))

def std_dev(num_list, mean):
	total_val_minus_mean_squared = 0
	for num in num_list:
		total_val_minus_mean_squared = total_val_minus_mean_squared + math.pow(num - mean,2)
	return math.sqrt(total_val_minus_mean_squared / len(num_list))


print("Analyzing accelerometer data")
file_name = input('Enter file name: ')
path = "/Users/james/Dropbox/SFU Courses/CMPT 275/accelerometer data/" + file_name
accel_Data = open(path)
x_lst, y_lst, z_lst, vector_sum = [],[],[],[]
seconds, duration = [],[]
date = ''

for line in accel_Data:
	# A line will have an X if it is outputting accelerometer data
	if(line.find('X') != -1):
		line_list = line.split(' ')
		time_sec = float(get_time(line_list[1]))
		x_val = float(line_list[5].replace(',' , ''))
		y_val = float(line_list[8].replace(',', ''))
		z_val = float(line_list[11].replace('\n', ''))
		vec_val = get_vector_sum(x_val,y_val,z_val)
		date = line_list[0]
		duration.append(line_list[1])
		seconds.append(time_sec) 

		x_lst.append(x_val)
		y_lst.append(y_val)
		z_lst.append(z_val)
		vector_sum.append(vec_val)

# Gather mean values of x, y, z
mean_x = get_mean(x_lst)
mean_y = get_mean(y_lst)
mean_z = get_mean(z_lst)

# Gather the min and max values of x, y, z
min_x, max_x = min(x_lst), max(x_lst)
min_y, max_y = min(y_lst), max(y_lst)
min_z, max_z = min(z_lst), max(z_lst)

# Gather the range values of x, y, z
range_x = max_x - min_x
range_y = max_y - min_y
range_z = max_z - min_z

# Gather standard deviation values of x, y, z
std_dev_x = std_dev(x_lst, mean_x)
std_dev_y = std_dev(y_lst, mean_y)
std_dev_z = std_dev(z_lst, mean_z)

# Convert each list as strings
time_txt = "t = " + str(seconds) + ";\n\n" 
x_txt = "x ="+ str(x_lst) + ";\n\n"
y_txt = "y ="+ str(y_lst) + ";\n\n"
z_txt = "z ="+ str(z_lst) + ";\n\n"
vector_sum_txt = "vs =" + str(vector_sum) + ";"


# Increment the number in count.txt and overwrite the file
# count.txt is used to determine how many accelerometer data readings we have done
count_file = open("/Users/james/Dropbox/SFU Courses/CMPT 275/accelerometer data/count", "r+")
count = str(int(count_file.readline()) + 1)
count_file.seek(0)
count_file.write(count)
count_file.truncate()

out_file = open("/Users/james/Dropbox/SFU Courses/CMPT 275/accelerometer data/accelData" + count, "w")
comment = input("Enter comment: ")
out_file.write("% Date: {0}\n% Test Duration: {1} - {2}\n".format(date, duration[0], duration[len(duration)-1]))
out_file.write("% Comment:" + comment + "\n\n")

out_file.write("% Statistics:\n")
heading = "%{0:^25} {1:^25} {2:^25} {3:^25} {4:^25}\n".format('Mean', 'Min', 'Max', 'Range', 'Std.Dev')
stat_format_x = "% X: {0: <25} {1: <25} {2: <25} {3: <25} {4: <25}\n".format(mean_x, min_x, max_x, range_x, std_dev_x)
stat_format_y = "% Y: {0: <25} {1: <25} {2: <25} {3: <25} {4: <25}\n".format(mean_y, min_y, max_y, range_y, std_dev_y)
stat_format_z = "% Z: {0: <25} {1: <25} {2: <25} {3: <25} {4: <25}\n\n".format(mean_z, min_z, max_z, range_z, std_dev_z)
out_file.write(heading)
out_file.write(stat_format_x)
out_file.write(stat_format_y)
out_file.write(stat_format_z)

out_file.write(time_txt)
out_file.write(x_txt)
out_file.write(y_txt)
out_file.write(z_txt)
out_file.write(vector_sum_txt)

accel_Data.close()
out_file.close()
count_file.close()

print('Finished')