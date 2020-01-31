from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='ChatPackage',
    version='1.1',
    packages=['chat'],
    url='https://github.com/riturajpandey/ChatPackage',
    license='GNU GENERAL PUBLIC LICENSE VERSION 3',
    author='Ashwini Bokade',
    author_email='ashwini_bokade@yahoo.com',
    description='Testing Chat Package',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License=GNU GENERAL PUBLIC LICENSE Version 3",
        "Operating System :: OS Independent",
    ],
)
