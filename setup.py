from distutils.core import setup

setup (
	name		= "FixQueue",
	version		= "0.1.1",
	packages 	= ['FixQueue'],
	author		= 'Mino Ku',
	author_email	= 'happykus@gmail.com',
	url		= 'https://github.com/minoku/FixQueue',
	download_url	= 'https://github.com/minoku/FixQueue',
	license		= 'MIT Lincense',
	keywords	= ['fixqueue','queue', 'list', 'collection','simplequeue','fixed size queue', 'fix queue'],
	description	= 'Simplest Queue module to make a fixed size queue on your platform and apps. You just need to use FixQueue-based queues like normal list-based objects.'
	classifiers	= ['License :: OSI Approved :: MIT License', 'Programming Language :: Python', 'Programming Language :: Python :: Implementation', 'Programming Language :: Python :: Implementation :: Stackless', 'Topic :: Software Development', 'Topic :: Software Development :: Libraries'],
	)