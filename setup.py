#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) <year> <copyright holders>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
package = "MySQL-python" if sys.version_info.major < 3 else "mysqlclient"

print("WARNING: `mysql` is a virtual package. Please use `%s` as a dependency directly.\n" % package)

setup(
    name='mysql',
    version='0.0.3',
    description='Virtual package for MySQL-python',
    long_description=open('README.rst').read(),
    author='Merlijn van Deen',
    author_email='valhallasw@arctus.nl',
    install_requires=[package],
    license="MIT",
    url="https://github.com/valhallasw/virtual-mysql-pypi-package",
)
