from setuptools import setup

setup(name='ska_namespace_wrappers',
      author='John ZuHone',
      description='Compatibility wrappers for the Ska namespace',
      author_email='john.zuhone@cfa.harvard.edu',
      use_scm_version=True,
      setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
      zip_safe=False,
      packages=['Ska'],
      )
