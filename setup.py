from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = "colorful-festival-gy",
    version = "0.1.7",
    author = "Guyutongxue",
    author_email = "guyutongxue@163.com",
    description = "An OSS course practice",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/OSSDevelopment-Course-2021-Autumn/colorful-festival-gy",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    package_dir = {
       "": "src"
    },
    license='WTFPL',
    packages = find_packages(where="src"),
    # install_requires = [
    #     "string-color",
    #     "LunarCalendar",
    #     "date-string"
    # ],
    python_requires = ">=3.6"
)