import pyshark

cap = pyshark.FileCapture('cap.pcap')
# в ваершарке прописываем ключи
# 01:03:05:07:09:0B:0D:0F:00:02:04:06:08:0A:0C:0D
# 5A:69:67:42:65:65:41:6C:6C:69:61:6E:63:65:30:39

num = 1
for pack in cap:
    try:
        aps = str(pack['ZBEE_APS']).split()
        ind = aps.index('Cluster:')
    except:
        num += 1
        continue

    i = 1

    sensor = ''
    while aps[ind + i] != 'Profile:':
        sensor += ' '
        sensor += aps[ind + i]
        i += 1
    if sensor == ' Occupancy Sensing (0x0406)':
        num += 1
        continue
    ret = {}
    # print(num, ') ', end='', sep='')
    # print('Датчик:', end='')
    # print(sensor, end='')
    ret['sensor'] = sensor[1:]
    # print('; ', end='')
    # print('value: ', end='')
    value = pack['ZBEE_ZCL'].get_field_by_showname('Measured Value')

    if sensor == ' Temperature Measurement (0x0402)' or sensor == ' Relative Humidity Measurement (0x0405)':
        ret['value'] = value[:-2] + ',' + value[-2:]
        print(value[:-2] + ',' + value[-2:])
    else:
        ret['value'] = pack['ZBEE_ZCL'].get_field_by_showname('Measured Value')
        # print(pack['ZBEE_ZCL'].get_field_by_showname('Measured Value'))
    print(ret)
    num += 1