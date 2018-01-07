"""
Setup module for Anansi.

See:
    https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages

setup(
    name='anansi',
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
    ],
    description='Media metadata provider.',
    url='https://github.com/labrys/anansi',
    author='Labrys',
    author_email='labrys.git@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Sound/Audio',
    ],
    keywords='media video audio metadata database',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    python_requires='>=3.6',
)
