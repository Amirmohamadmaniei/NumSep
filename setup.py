from setuptools import setup, find_packages

setup(
    # the name must match the folder name 'verysimplemodule'
    name="NumSep",
    version='0.0.1',
    author="AmirMohamad Maniei",
    description='100000 ---> 100,000',
    long_description="""
    
    separate payment and numbers with your sing and count that you want
    
    100000 ---> 100,000
    """,
    packages=find_packages(),

    # add any additional packages that
    # needs to be installed along with your package.
    install_requires=[],

    keywords=['separate', 'payment', 'num'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ]
)
