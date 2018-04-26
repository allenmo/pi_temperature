import os
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=","").replace("'C\n","")

CPU_temp = getCPUtemperature()
print('CPU Temperature = ' + CPU_temp)

