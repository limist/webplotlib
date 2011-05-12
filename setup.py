from setuptools import setup

setup(
    name='django-webplotlib',
    packages=['webplotlib', ],
    version='0.1',
    description='A Django app for serving charts/graphs using matplotlib.',
    author='Kai',
    author_email='k@limist.com',
    url='http://github.com/limist/django-webplotlib',
    download_url='',
    keywords="django chart graph matplotlib app",
    license='BSD',
    install_requires=[
        'Django',
        'matplotlib',
        'pytest >= 2',
        'setuptools',
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'],
    long_description=open('README', 'r').read()
    )
