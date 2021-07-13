import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dg_ai_platform",
    version="0.1.8",
    author="Caldron Tech",
    author_email="support@caldrontech.com",
    description="A AI container platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gd4219/test_pip_pck",
    packages=setuptools.find_packages(),
    install_requires = ['oss2', 'pillow'],
    #                    'keras>=2.4.3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)