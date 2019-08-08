#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

def rv_hash(clientid, servers):
	hash = hashlib.md5()
	srv_dict = {}
	for srv in servers:
		srv_hash = srv + clientid + '_%d'
		hash.update(srv_hash.encode('utf-8'))
		srv_dict[hash.hexdigest()] = srv
	client_goes_to = max(srv_dict.keys())
	print(clientid, " : ", srv_dict[client_goes_to])

rv_hash('client-01', ["s1","s2", "s3", "s4", "s5", "s6"])