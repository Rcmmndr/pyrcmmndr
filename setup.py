from setuptools import setup, find_packages

DESCRIPTION = "PyRcmmndr - Rcmmndr Rest Client for Python"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 1 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Recommendation Engine',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: BSD License',
]

setup(name='pyrcmmndr',
      packages=find_packages(exclude=('tests', 'test')),
      author='Rcmmndr Team',
      author_email='admin@rcmmndr.com',
      url='http://www.rcmmndr.com',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      classifiers=CLASSIFIERS,
      install_requires=['httplib2'],
      version='0.0.1',
      zip_safe=False
)