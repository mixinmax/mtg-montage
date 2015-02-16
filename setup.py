from setuptools import setup

setup(
	name = 'mtg-montage',
	version = '0.1.1',
	description = 'Creates proxy pages from Magic: The Gathering cards ready for printing',
	author = 'Max Mackie',
	author_email = 'mtg-montage@f33r.com',
	license = 'LICENSE.txt',
	keywords = 'montage imagemagick magic mtg proxy',
	url = 'https://github.com/maxmackie/mtg-montage',
	long_description=open('README.md').read(),
	scripts = [
		'bin/mtg-montage'
	]
)