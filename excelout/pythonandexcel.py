#!/usr/bin/env python3

import pyexcel
import datetime as dt

def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver=input("What's the driver?")
    d={"IP": input_ip, "driver": input_driver}
    return d

def main():
    mylistdict=[]
    print("Hi this will make you a *.xls file")
    while (True):
        mylistdict.append(get_ip_data())
        keep_going = input("Want another one? or 'q' to quit")
        if keep_going.lower()=='q':
            break
    filename=input("What's name of file?")
    filename=filename+".xls"
    pyexcel.save_as(records=mylistdict,dest_file_name=filename)
    print(f"File {filename} .xls is in local dir")
    print(mylistdict)

main()

