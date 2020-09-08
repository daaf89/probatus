import setuptools
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="probatus",
    version="1.1.1",
    description="Tools for machine learning model validation",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="RPAA ING",
    author_email="ml_risk_and_pricing_aa@ing.com",
    license="ING Open Source",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(
        exclude=["probatus.interpret", "tests.interpret",]
    ),
    install_requires=[
        "scikit-learn>=0.22.2",
        "pandas>=0.25",
        "matplotlib>=3.1.1",
        "scipy>=1.4.0",
        "joblib>=0.13.2",
        "tqdm>=4.41.0",
        "shap>=0.32.0",
    ],
    url="https://gitlab.com/ing_rpaa/probatus",
    zip_safe=False,
)
