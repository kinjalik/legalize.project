import json
import time

import os
stream = os.popen(' whsniff -c 11 | tshark -i - -Tjson')
output = stream.read()
print(output)
def write_device(device):
    file = open("devices.txt", "a")
    file.write(device + '\n')

def json_handle():
    with open('packets.json') as json_file:
        data = json.load(json_file)
        print(data)

