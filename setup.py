from setuptools import setup, find_packages

setup(
    name='my-font',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2',  # dopasuj do wersji InvenTree
    ],
    entry_points={
        'inventree.plugins': [
            'my-font = my_font.plugin:MyFontPlugin',
        ],
    },
)
