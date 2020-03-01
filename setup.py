#!/usr/bin/env python

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='PythonSnake',
      version='0.0.1',
      description='Python Snake Game',
      author='Göktuğ Karakaşlı',
      author_email='karakasligk@gmail.com',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/goktug97/PythonSnake',
      download_url=(
          'https://github.com/goktug97/PythonSnake/archive/v0.0.1.tar.gz'),
      py_modules=[os.path.splitext(os.path.basename(path))[0]
                  for path in ['snake.py',
                               'play.py']],
      entry_points={
              'console_scripts': [
                  'python-snake = play:main',
              ]
          },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
      ],
      install_requires=[
          'numpy',
      ],
      python_requires='>=3.6',
      include_package_data=True)
