# в ваершарке прописываем ключи
# 01:03:05:07:09:0B:0D:0F:00:02:04:06:08:0A:0C:0D
# 5A:69:67:42:65:65:41:6C:6C:69:61:6E:63:65:30:39

# пишем команды
# mkfifo /tmp/whsniff
# whsniff -c 11 > /tmp/whsniff

import pyshark
import time
<<<<<<< HEAD
import json
import time
import random

last_z = 0

z = 0


global_var = []
=======

>>>>>>> 33928909c41ea05860c4b99b346069cea56d769c
while True:
# for fdas in range(1):
    capture = pyshark.FileCapture('/tmp/whsniff')
    for num, pack in enumerate(capture):
        if "ZBEE_APS" not in pack:
            continue
        aps = str(pack['ZBEE_APS'])
<<<<<<< HEAD

=======
>>>>>>> 33928909c41ea05860c4b99b346069cea56d769c
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

<<<<<<< HEAD
=======

>>>>>>> 33928909c41ea05860c4b99b346069cea56d769c
        return_values = {}
        return_values['data'] = data
        return_values['panID'] = pack.wpan.get_field_by_showname('Destination PAN')[:2] + pack.wpan.get_field_by_showname('Destination PAN')[6:]
        return_values['mac'] = pack.zbee_nwk.get_field_by_showname('Extended Source')
<<<<<<< HEAD
        return_values["rssi"] = random.randint(70,90)
        return_values["counter"] = 999
        global_var.append(return_values)
        # dev = open("devices.txt", "r")
        # all_str = dev.read()
        # for line in all_str.split("\n"):
        #     q = json.loads(line.replace("'", '"'))["data"]["sensor"]
        #     if (q.replace(" ", "").find(data["sensor"].replace(" ", "")) != -1 or data["sensor"].replace(" ", "").find(q.replace(" ", "")) !=-1):
        #         all_str.replace(line, str(return_values))
        print(return_values)
        dev_w = open("devices.txt", "w")
        dev_w.write(str(str(global_var).replace("'", '"')))
        dev_w.close()
        z = z+1
=======
        return_values['sequence_number'] = pack.zbee_zcl.get_field_by_showname('Sequence Number')
        print(return_values)
>>>>>>> 33928909c41ea05860c4b99b346069cea56d769c

    f = open('/tmp/whsniff', 'w')
    f.close()
    time.sleep(0.1)
<<<<<<< HEAD


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 2528)
=======
>>>>>>> 33928909c41ea05860c4b99b346069cea56d769c
