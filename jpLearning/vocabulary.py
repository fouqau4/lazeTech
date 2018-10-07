#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
from random import shuffle

_dir_vocs = './vocabulary.json'
_num = int(sys.argv[2]) if len(sys.argv) > 2 else 10

with open(_dir_vocs) as f:
	data = json.load(f)[int(sys.argv[1])]

keys = data.keys()
shuffle(keys)

print sys.stdin.encoding


for idx in xrange(min(_num,len(keys))):
	fail=True
	for i in xrange(3) :
		ans = raw_input(keys[idx].encode('utf-8') + " : ")
		if ans == data[keys[idx]].encode('utf-8'):
			fail=False
			break
	if fail:
		print data[keys[idx]]	
	else:
		print 'O'

