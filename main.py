import contants
import functions

file = contants.File1
init_time = contants.StartTime1
finish_time = contants.FinishTime1
host_name = contants.HostName1


init_time = functions.convert_to_datetime(init_time)
finish_time = functions.convert_to_datetime(finish_time)


print('PART 1')
functions.question1(file,init_time,finish_time,host_name)
print()

file = contants.File2
host_name = contants.HostName2
connection = contants.Connection2
init_time,finish_time = functions.select_time_frame(contants.useCurrentTime)


print('PART 2')
functions.question2(file,init_time,finish_time,host_name,connection)