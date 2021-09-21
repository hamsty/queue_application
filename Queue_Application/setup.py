from setuptools import setup

setup(
    name='Queue_Application',
    version='0.0.1',
    packages=['qapp', 'qapp.client',
              'qapp.server', 'qapp.entities'],
    url='',
    license='',
    author='talle',
    author_email='tallesdesousacosta@gmail.com',
    description='',
    install_requires=[
        'Twisted>=21.7.0',
    ],
    scripts=['bin/queue_client', 'bin/queue_server']
)
