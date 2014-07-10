import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='frecency',
    version='0.1',
    py_modules=['frecency'],
    include_package_data=True,
    install_requires=[],
    license='BSD',
    description='A Pythonic library for computing weight using a frecency algorithm.',
    long_description=README,
    url='https://github.com/rshipp/python-frecency/',
    author='Ryan Shipp',
    author_email='python@rshipp.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
)
