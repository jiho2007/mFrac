import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mfrac",
    version="0.2.1",
    author="jiho2007",
    author_email="zzang-9@naver.com",
    description="A Small Fraction Class Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiho2007/mFrac",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
