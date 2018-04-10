from setuptools import setup, find_packages

__version__ = '0.1.0'

setup(
    name='ecoji',
    version=__version__,
    description='Encode and decode data as emojis.',
    long_description=open("README.md").read(),
    author='mecforlove',
    author_email='mecforlove@outlook.com',
    url='https://github.com/mecforlove/ecoji-py',
    license='Apache',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        ecoji=ecoji.__main__:main
    ''',
    classifiers=[
        'Programming Language :: Python', 'Programming Language :: Python :: 3'
    ])
