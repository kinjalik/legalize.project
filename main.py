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

        data = {}  # data
        data['sensor'] = sensor[1:]
        value = pack['ZBEE_ZCL'].get_field_by_showname('Measured Value')

        if sensor.split()[-1] == '(0x0402)' or sensor.split()[-1] == '(0x0405)':
            data['value'] = value[:-2] + ',' + value[-2:]
        else:
            data['value'] = pack['ZBEE_ZCL'].get_field_by_showname('Measured Value')


        return_values = {}
        return_values['data'] = data
        return_values['panID'] = pack.wpan.get_field_by_showname('Destination PAN')[:2] + pack.wpan.get_field_by_showname('Destination PAN')[6:]
        print(return_values)

    f = open('/tmp/whsniff', 'w')
    f.close()
    time.sleep(0.1)
