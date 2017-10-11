from setuptools import setup

setup(
    author='Konstiantyn Snihyr',
    author_email='konstantin.s@cliqz.com',
    name='cinepass-pythonclient',
    version='0.2',
    provides=['cinepass'],
    url='https://github.com/cliqz/cinepass-pythonclient',
    packages=[
        'cinepass',
        'cinepass.client',
        'cinepass.client.v4',
    ],
    zip_safe=False,
    platforms='any',
    tests_require=[
        'pytest',
    ]
)
