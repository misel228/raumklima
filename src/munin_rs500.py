#!/usr/bin/env python3

from rs500reader.reader import Rs500Reader
import sys

def get_and_print():
    reader = Rs500Reader()
    data = reader.get_data()
    for i in range(1, 9, 1):
        chan_data = data.get_channel_data(i)
        if chan_data is not None:
            print('temp_{:d}.value {:0.1f}'.format(i, chan_data.temperature))
            # print('{:d}_humidity {:d}'.format(i, chan_data.humidity))
    #print('.')

def output_config():
    print("graph_title Apartment Temperatures ")
    print("graph_args --base 1000 -l 0 --upper-limit 50")
    print("graph_vlabel temperature")
    print("graph_scale no ")
    print("graph_category sensors ")
    print("graph_info appartment temps")

    text_file = open("/etc/munin/plugin-conf.d/sensor_names.txt", "r")
    sensors = text_file.read().splitlines()
    sensors.insert(0, "")

    reader = Rs500Reader()
    data = reader.get_data()
    for i in range(1, 9, 1):
        chan_data = data.get_channel_data(i)
        if chan_data is not None:
            print('temp_{:d}.label {:s}'.format(i, sensors[i]))



if __name__ == '__main__':
    if(len(sys.argv) == 1):
        get_and_print()
    else:
        if sys.argv[1] == 'config':
            output_config()
        
