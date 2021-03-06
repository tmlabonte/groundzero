from setuptools import find_packages, setup

with open("requirements.txt") as f:
    lines = f.read()
    lines = lines.replace("git+https://github.com/noahgolmant/pytorch-hessian-eigenthings.git@master#egg=hessian-eigenthings\n", "")
    required = lines.splitlines()
    required.append("hessian-eigenthings @ git+https://github.com/noahgolmant/pytorch-hessian-eigenthings.git@master#egg=hessian-eigenthings")

setup(
    name="groundzero",
    install_requires=required,
    packages=["groundzero"],
    version="1.0",
)
