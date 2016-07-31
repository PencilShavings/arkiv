#!/usr/bin/env python
__author__ = 'dummy'

import sys
import osutil

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print 'Please specify a dir to archive'
	else:
		if osutil.dir_exists(sys.argv[1]):
			osutil.targz(sys.argv[1])
		else:
			print str(sys.argv[1]) + ' does not exist.'