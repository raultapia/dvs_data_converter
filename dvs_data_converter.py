#!/usr/bin/python3
"""
@file dvs_data_converter.py
@brief Script to convert DVS (Dynamic Vision Sensor) data between different formats.
@author Raul Tapia (github.com/raultapia)
"""

import argparse
import os
import rosbag


def format_topic_name(x):
    if x.startswith('/'):
        return x[1:].replace('/', '_')
    else:
        return x.replace('/', '_')


def bag2txt(filename, columns, zero_offset, separation=" ", extension="txt"):
    bag = rosbag.Bag(filename)
    topics = [key for (key, value) in bag.get_type_and_topic_info()[1].items() if value[0] == 'dvs_msgs/EventArray']
    t0 = 0
    for tpc in topics:
        with open(f"{filename[:-4]}.{extension}", 'w') if len(topics) == 1 else open(f"{filename[:-4]}.{format_topic_name(tpc)}.{extension}", 'w') as output_file:
            for topic, msg, t in bag.read_messages():
                if tpc == topic:
                    for e in msg.events:
                        if t0 == 0 and zero_offset:
                            t0 = e.ts.to_sec()
                        if columns == 'txyp':
                            output_file.write(f"{e.ts.to_sec()-t0:.9f}{separation}{e.x}{separation}{e.y}{separation}{int(e.polarity)}\n")
                        elif columns == 'xytp':
                            output_file.write(f"{e.x}{separation}{e.y}{separation}{e.ts.to_sec()-t0:.9f}{separation}{int(e.polarity)}\n")
                        elif columns == 'ptxy':
                            output_file.write(f"{int(e.polarity)}{separation}{e.ts.to_sec()-t0:.9f}{separation}{e.x}{separation}{e.y}\n")
                        elif columns == 'pxyt':
                            output_file.write(f"{int(e.polarity)}{separation}{e.x}{separation}{e.y}{separation}{e.ts.to_sec()-t0:.9f}\n")


def bag2csv(filename, columns, zero_offset):
    bag2txt(filename, columns, zero_offset, ",", "csv")


def txt2bag():  # TODO
    pass


def csv2bag():  # TODO
    pass


def txt2csv():  # TODO
    pass


def csv2txt():  # TODO
    pass


def check_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    if not (file_path.endswith('.txt') or file_path.endswith('.csv') or file_path.endswith('.bag')):
        raise ValueError(f"The file '{file_path}' is not txt, csv, or bag.")
    return file_path[-3:]


def main():
    parser = argparse.ArgumentParser(description="DVS data converter")
    parser.add_argument('files', metavar='files', type=str, nargs='+', help='file(s) to convert')
    parser.add_argument('--output', '-o', type=str, choices=['txt', 'csv', 'bag'], required=True, help='output format')
    parser.add_argument('--columns', '-c', type=str, choices=['txyp', 'xytp', 'ptxy', 'pxyt'], default='txyp', help='column order for txt and csv')
    parser.add_argument("--zero", '-z', action="store_true", help='add time offset to start at t = 0')
    args = parser.parse_args()

    for file in args.files:
        fn = f"{check_file(file)}2{args.output}"
        if fn in globals():
            globals()[fn](file, args.columns, args.zero)
        else:
            raise ValueError("Conversion not defined.")


if __name__ == "__main__":
    main()
