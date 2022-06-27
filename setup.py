from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirement_file:
    requirements_list = requirement_file.readlines()
    requirements_list = [lib.replace("\n", "") for lib in requirements_list]

requirements = requirements_list

setup(
    name="AgriTech-USGS_LIDAR",
    version="0.1.0",
    description="AgriTech-USGS_LIDAR is a Python module that will allow users to quickly handle, convert, sample, "
                "and visualize the geographical data from 3DEP.",
    url="https://github.com/DiyeMark/AgriTech-USGS_LIDAR.git",
    author="Diye Mark",
    author_email="diyye101@gmail.com",
    license="MIT License",
    install_requires=requirements,
    long_description=readme,
)