from setuptools import setup, find_packages

setup(
    name='Clean_folder',
    version=1.00,
    description='Cleaning_folder_script by Python',
    long_description="README.md",
    author='Imukr',
    author_email='I0979887766@gmail.com',
    license="MIT",
    url=URL,
    packages=find_packages(),
    package_data=find_package_data(PACKAGE, only_in_packages=False),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)