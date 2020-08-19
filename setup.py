from setuptools import setup

setup(
    name='gasprice-blocklytics',
    version='0.0.1',
    description='predict ethereum gas price',
    url='https://github.com/blocklytics/gasprice',
    author='blocklytics',
    py_modules=[
        'gas_price',
    ],
    install_requires=[
        'sanic',
        'pandas',
        'web3>=4.0.0b4',
        'click',
        'retry',
    ],
    entry_points={
        'console_scripts': [
            'gasprice=gas_price:main',
        ]
    }
)
