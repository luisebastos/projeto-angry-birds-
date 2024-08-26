from setuptools import setup, find_packages

setup(
    name="disney_escape",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        "pygame", "numpy"
    ],
    package_data={
        '': ['assets/*.png','disney_escape/assets/*.png',]  # Inclui todos os arquivos .png dentro do diretório 'img' de todos os pacotes
    },
    entry_points={
        "console_scripts": [
            "disney_escape=disney_escape.main:main",  # Se quiser criar um comando de terminal
        ],
    },
    author="Luise e Manuela",  # Seu nome
    author_email="luise@gustavobastos.com.br",  # Seu email
    description="Em um jogo  de física, o jogador deve lançar um AngryBird para acertar um personagem da Disney em um cenário que contém um campo gravitacional para tentar salvar esse personagem.",
    long_description=open("README.md").read(),  # Descrição longa (usualmente do README)
    long_description_content_type="text/markdown",
    url="https://github.com/luisebastos/projeto-angry-birds-.git",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)


