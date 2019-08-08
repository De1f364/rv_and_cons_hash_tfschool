#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def search(circle, hash_client):
    keys = sorted(circle.keys())
    for i, j in enumerate(keys):
        if keys[i-1] < hash_client <= keys[i]:
            return circle[keys[i]]
    return circle[keys[0]]


def cons_hash(clientid, servers):
	number_of_node = 10000
	hash = hashlib.md5()
	circle = {}
	for srv in servers:
		for i in range(number_of_node):
			srv_hash = srv + '_%d' % i
			hash.update(srv_hash.encode('utf-8'))
			circle[hash.hexdigest()] = srv
	hash.update(clientid.encode('utf-8'))
	print(clientid, " : ", search(circle, hash.hexdigest()))

cons_hash('client-06', ["s1","s2", "s3", "s4", "s5", "s6"])