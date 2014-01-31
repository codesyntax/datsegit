from setuptools import setup, find_packages

version = '0.1'

with open('docs/requirements.txt') as f:
    required = f.read().splitlines()
    
setup(name='datsegit',
      version=version,
      description="This is the project that runs www.datsegit.com",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Aitzol Naberan',
      author_email='anaberan@codesyntax.com',
      url='http://www.datsegit.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
