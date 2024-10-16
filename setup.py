from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="tratamento_imagem",
    version="0.0.1",
    author="Antonio_Adade",
    author_email="my_email",
    description="Pacote para tratamento de imagem com python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntonioAdade/Python_Pacote_Imagem.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
