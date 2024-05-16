from setuptools import setup, find_packages

setup(
    name='brent',
    version='0.1.0',
    description='Brent: Binary Runtime Environment for Network Tasks',
    author='Your Name',
    author_email='dj@codetestcode.io',
    url='https://github.com/copyleftdev/brent',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'scipy'
    ],
    entry_points={
        'console_scripts': [
            'brent=brent.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
)
