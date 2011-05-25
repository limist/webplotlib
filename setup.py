from setuptools import setup

setup(
    name='webplotlib',
    packages=['webplotlib', ],
    version='0.1',
    description='A package for creating server-side charts/graphs using matplotlib; examples are also given for serving those charts directly via Django.',
    author='Kai',
    author_email='k@limist.com',
    url='http://github.com/limist/webplotlib',
    download_url='',
    keywords="django chart graph matplotlib server-side",
    license='GPL',
    install_requires=[
        'Django',
        'matplotlib',
        'numpy',
        'pytest >= 2',
        'setuptools',
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Internet :: WWW/HTTP'],
    long_description=open('README', 'r').read()
    )
