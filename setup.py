from setuptools import setup, find_packages

setup(
    name='asyncpg_wrapper',
    version='0.1.0',
    description='AsyncPG Easy-To-Use wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nissle',
    author_email='nixncom@gmail.com',
    url='https://github.com/nissle59/asyncpg_wrapper',  # или URL вашего проекта
    packages=find_packages(),
    install_requires=[
        'asyncpg>=0.29.0',  # или другие зависимости
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
