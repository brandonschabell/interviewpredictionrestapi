from setuptools import setup, find_packages

requirements = [
    'Flask==1.1.1'
]

test_requirements = [
    'pytest==5.4.1',
    'pytest-runner==5.2'
]

setup(
    name='interviewprediction',
    version='0.0.1',
    packages=find_packages(),
    author='Brandon Schabell',
    author_email='brandonschabell@gmail.com',
    python_requires='==3.7.*',
    install_requires=requirements,
    tests_require=test_requirements,
    extras_require={
        'test': test_requirements
    }
)
