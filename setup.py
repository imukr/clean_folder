from setuptools import setup, find_packages

setup(
    name='Clean_folder',
    version=1.00,
    description='Cleaning_folder_script by Python',
    long_description="README.md",
    author='Imukr',
    author_email='I0979887766@gmail.com',
    license="MIT",
    url="https://github.com/imukr/clean_folder.git",
    packages = find_packages(),
    classifiers=[
        "License :: MIT :: approved",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    entry_points = {"console_scripts": ["clean-folder = clean_folder.main:main"]}
)