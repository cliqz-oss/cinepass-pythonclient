from setuptools import setup

setup(
    author='Konstiantyn Snihyr',
    author_email='konstantin.s@cliqz.com',
    name='cinepass-python',
    version='0.1',
    provides=['cinepass'],
    url='https://github.com/cliqz-oss/cinepass-python/',
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
