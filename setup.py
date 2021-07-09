#!/usr/bin/env python

from distutils.core import setup


setup(name='avonage',
      version='0.1',
      description='Asynchronous Vonage / Nexmo client',
      url='https://github.com/adyachok/avonage',
      author='Andras Gyacsok',
      author_email='atti.dyachok@gmail.com',
      license='MIT',
      packages=['avonage'],
      install_requires=[
          'aiohttp',
      ],
      zip_safe=False)
