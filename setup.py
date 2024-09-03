

from setuptools import setup, find_packages

extras_require = {
    'cleaning': [
        'openpyxl==3.0.5',
        'pyyaml==5.4.1',
    ],
    'analysis': [
        'matplotlib==3.4.2',
        'seaborn==0.11.1',
        'jupyter==1.0.0',
    ],
    'ml': [
        'xgboost==1.4.2',
        'lightgbm==3.2.1',
        'tensorflow==2.12.1',
    ],
    'production': [
        'flask==2.0.1',
        'gunicorn==20.1.0',
        'docker==5.0.0',
    ],
}

setup(
    name="ecommerce-data-hub",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas==1.3.3',
        'numpy==1.21.2',
        'scikit-learn==0.24.2',
    ],
    extras_require=extras_require,
)
