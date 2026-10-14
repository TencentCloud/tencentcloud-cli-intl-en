#! /usr/bin/env python

"""
distutils/setuptools install script.
"""
from setuptools import setup, find_packages
from tccli import __version__


def main():
    dep_sdk = "tencentcloud-sdk-python-common >= 3.1.180"
    setup(
        name='tccli-intl-en',
        install_requires=[dep_sdk, "jmespath>=0.10.0", "six>=1.16.0"],
        version=__version__,
        description='Universal Command Line Environment for Tencent Cloud',
        long_description=open('README.rst').read(),
        author='Tencent Cloud',
        url='https://github.com/TencentCloud/tencentcloud-cli-intl-en.git',
        maintainer_email="TencentCloudApi@tencent.com",
        packages=find_packages(),
        include_package_data=True,
        platforms=['unix', 'linux', 'win64'],
        scripts=[],
        py_modules=['tccli'],
        entry_points={
            'console_scripts': [
                'tccli = tccli.main:main',
                'tccli_completer  = tccli.completer:complete',
            ]
        },
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
    )


if __name__ == '__main__':
    main()
