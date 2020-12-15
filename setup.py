from setuptools import setup
from io import open
import os

setup(
    name='docassemble-textstat',
    packages=['docassemble_textstat'],
    version='0.7.1',
    description='Calculate statistical features from text',
    author='Shivam Bansal, Chaitanya Aggarwal, Jonathan Pyle',
    author_email='jhpyle@gmail.com',
    url='https://github.com/jhpyle/textstat',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    package_data={'': [os.path.join('resources', 'en', '*.*'), os.path.join('resources', 'es', '*.*')]},
    install_requires=['hyphenate==1.1.0'],
    license='MIT',
    python_requires=">=3.6",
    zip_safe = False,
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing",
        ),
)
