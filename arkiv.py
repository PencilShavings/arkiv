#!/usr/bin/env python
"""A simple cli app for creating & extracting tarballs."""

__author__ = 'PencilShavings'
__version__ = '0.1'


import osutil
import argh

@argh.arg('target', help='Directory to archive')
@argh.arg('--dst', help='Path where to create the archive')
@argh.arg('-v', '--verbose', help='Show more info')
def create(target, dst='', verbose=False):
	"""Create Archive"""

	# Check if the target exists
	if not osutil.dir_exists(target):
		print '"' + target + '" does not exist.'
		exit()

	# Check if the dst exists
	if not dst == '':
		if not osutil.dir_exists(dst):
			print '"' + dst + '" does not exist.'
			exit()

	# Create the Archive
	osutil.targz(target, dst=dst, verbose=verbose)

@argh.arg('target', help='The tarball to extract')
@argh.arg('--dst', help='Path where to extract the archive')
@argh.arg('-i', '--into', help='Extract contents of archive into DST')
@argh.arg('-v', '--verbose', help='Show more info')
@argh.arg('-r', '--remove', help='Remove the tarball after extraction')
def extract(target, dst='', into=False, verbose=False, remove=False):
	"""Extract Archive"""

	# Check if the target exists
	if not osutil.file_exists(target):
		print '"' + target + '" does not exist.'
		exit()

	# Check if the dst exists
	if not dst == '':
		if not osutil.dir_exists(dst):
			print '"' + dst + '" does not exist.'
			exit()

	# Extract the Archive
	osutil.targz(target, dst=dst, extract=True, into=into, verbose=verbose)

	# Remove the Archive
	if remove:
		osutil.rm(target, verbose=verbose)

if __name__ == '__main__':
	praser = argh.ArghParser(prog=__file__.partition('/')[2].rpartition('.')[0], version='%(prog)s ' + __version__, description=__doc__)
	praser.add_commands([create, extract])
	argh.dispatch(praser)