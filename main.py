# в ваершарке прописываем ключи
# 01:03:05:07:09:0B:0D:0F:00:02:04:06:08:0A:0C:0D
# 5A:69:67:42:65:65:41:6C:6C:69:61:6E:63:65:30:39

# пишем команды
# mkfifo /tmp/whsniff
# whsniff -c 11 > /tmp/whsniff

import pyshark
import time

while True:
    capture = pyshark.FileCapture('/tmp/whsniff')
    for num, pack in enumerate(capture):
        if "ZBEE_APS" not in pack:
            continue
        aps = str(pack['ZBEE_APS'])
        cluster_ind = aps.find('Cluster:')
        if cluster_ind == -1:
            continue
        profile_ind = aps.find('Profile:')
        sensor = aps[cluster_ind + 7:profile_ind].strip()
        if sensor == ' Occupancy Sensing (0x0406)':
            continue

        ret = {}
        ret['sensor'] = sensor[1:]
        value = pack['ZBEE_ZCL'].get_field_by_showname('Measured Value')

        if sensor.split()[-1] == '(0x0402)' or sensor.split()[-1] == '(0x0405)':
            ret['value'] = value[:-2] + ',' + value[-2:]
        else:
            ret['value'] = pack['ZBEE_ZCL'].get_field_by_showname('Measured Value')
        print(ret)
    f = open('/tmp/whsniff', 'w')
    f.close()
    time.sleep(0.1)
