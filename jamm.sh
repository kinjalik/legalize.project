while :
do
    mosquitto_pub -h localhost -p 1883 -t zigbee2mqtt/0x00158d0003221f28/set -m '{"state":"ON"}';
done;
