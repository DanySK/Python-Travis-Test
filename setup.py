import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="a_chart",
    version="0.1.0",
    author="Danilo Pianini",
    author_email="danilo.pianini@unibo.it",
    description="Creates a chart with a sinusoid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanySK/example-project",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
