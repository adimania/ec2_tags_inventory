#!/usr/bin/env python

import boto3
import json
import ConfigParser
import os

def get_address(instance):
	if "PublicIpAddress" in instance:
		address = instance["PublicIpAddress"]
	else:
		address = instance["PrivateIpAddress"]
	return address

if os.path.isfile('ec2.ini'):
	config_path = 'ec2.ini'
elif os.path.isfile(os.path.expanduser('~/ec2.ini')):
	config_path = os.path.expanduser('~/ec2.ini')

config = ConfigParser.ConfigParser()
config.read(config_path)
id = config.get("credentials", "aws_access_key_id", raw=True)
key = config.get("credentials", "aws_secret_access_key", raw=True)

client = boto3.client('ec2', aws_access_key_id = id, aws_secret_access_key = key, region_name="us-east-1")

inventory = {}

reservations = client.describe_instances()['Reservations']
for reservation in reservations:
	for instance in reservation['Instances']:
		address = get_address(instance)
		for tag in instance['Tags']:
			if tag['Key'] == "ansible_role":
				roles = tag['Value'].split(",")
				for role in roles:
					if role in inventory:
						inventory[role].append(address)
					else:
						inventory[role] = [address]

print json.dumps(inventory)