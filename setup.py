#! /usr/bin/env python
#
# Copyright (C) 2015 SNSurvey Developers

DESCRIPTION = "snsurvey: Tools for planning of transient surveys"
LONG_DESCRIPTION = """\
Tools for planning of transient surveys 
"""

DISTNAME = 'snsurvey'
AUTHOR = 'SNSurvey Developers'
MAINTAINER = 'Raphael Ferretti' 
MAINTAINER_EMAIL = 'raphael.ferreti@fysik.su.se'
URL = 'https://github.com/ZwickyTransientFacility/snsurvey/'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/ZwickyTransientFacility/snsurvey/'
VERSION = '0.0.1.dev'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():
   install_requires = []

   # Just make sure dependencies exist, I haven't rigorously
   # tested what the minimal versions that will work are
   # (help on that would be awesome)
   try:
       import numpy
   except ImportError:
       install_requires.append('numpy')
   try:
       import sncosmo
   except ImportError:
       install_requires.append('sncosmo')

   return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
        author=AUTHOR,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=install_requires,
        packages=['snsurvey'],
        classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 2.7',
                     'License :: OSI Approved :: BSD License',
                     'Topic :: Scientific/Engineering :: Astronomy',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
          )
