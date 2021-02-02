import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
	name = 'moshoodscrumy',
	version = '0.01',
	author = 'Olawale',
	author_email = 'folarinolawale3415@gmail.com',
	description = ('A Linuxjobber Internship project.'),
	license = 'BSD',
	keywords = 'Linuxjobber internship moshoodscrumy',
	url = 'https://oladev.herokuapp.com',
	packages = ['moshoodscrumy'],
	long_description = read('README.rst'),
)
