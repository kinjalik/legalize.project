# в ваершарке прописываем ключи
# 01:03:05:07:09:0B:0D:0F:00:02:04:06:08:0A:0C:0D
# 5A:69:67:42:65:65:41:6C:6C:69:61:6E:63:65:30:39

import pyshark
import time

capture = pyshark.FileCapture('/tmp/whsniff')
num = 1
while True:
    for package in capture:
            try:
                aps = str(package['ZBEE_APS']).split()
                ind = aps.index('Cluster:')
            except:
                num += 1
                continue

            i = 1
            # print(aps)
            sensor = ''
            while aps[ind + i] != 'Profile:':
                sensor += ' '
                sensor += aps[ind + i]
                i += 1


            ret = {}
            # print(num, ') ', end='', sep='')
            # print('Датчик:', end='')
            # print(sensor, end='')
            ret['sensor'] = sensor[1:]
            # print('; ', end='')
            # print('value: ', end='')
            value = package['ZBEE_ZCL'].get_field_by_showname('Measured Value')

            if sensor == ' Temperature Measurement (0x0402)' or sensor == ' Relative Humidity Measurement (0x0405)':
                ret['value'] = value[:-2] + ',' + value[-2:]
                # print(value[:-2] + ',' + value[-2:])
            else:
                ret['value'] = package['ZBEE_ZCL'].get_field_by_showname('Measured Value')
                # print(pack['ZBEE_ZCL'].get_field_by_showname('Measured Value'))
            num += 1
            # {'sensor': sensor, 'value': value}
            print(ret)
    f = open('/tmp/whsniff', 'w')
    f.close()
    time.sleep(1)
    capture = pyshark.FileCapture('/tmp/whsniff')
