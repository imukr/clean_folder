from setuptools import setup, find_namespace_packages
setup(
    name='Clean_folder_Imukr',
    version=1.01,
    description='Cleaning_folder_script by Python',
    long_description="README.md",
    author='Imukr',
    author_email='I0979887766@gmail.com',
    license="MIT",
    url="https://github.com/imukr/clean_folder.git",
    packages = find_namespace_packages(),
    entry_points = {"console_scripts": ["clean-folder = clean_folder.main:main"]}
)