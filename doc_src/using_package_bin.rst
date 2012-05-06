=================
Using Package Bin
=================

Uploading Packages
==================

#. We need to add some stuff to your ``~/.pypirc`` configuration file. If you don't have one, you can create one using this example. ::
   
      index-servers =
          pypi

      [pypirc]
      servers =
          pypi

      [pypi]
      username:joecool
      password:MyPa55w0rd

#. First add ``pkgbin`` under ``index-servers``. ::
   
      index-servers =
          pypi
          pkgbin
   

#. Add ``pkgbin`` under ``[pypirc] servers``. ::
   
      [pypirc]
      servers =
          pypi
          pkgbin
   

#. Add a ``[pkgbin]`` section with the username, password and repository lines. ::
   
      [pkgbin]
      username:joecool
      password:Pa55w0rd
      repository:http://pkgbin.com/joecool/pypi/

#. Assuming you already have a ``setup.py`` file, to upload a package, simply ::
   
      python setup.py register -r pkgbin sdist upload -r pkgbin
   

If you need help getting your package working, check out `this guide from the distribute project <http://guide.python-distribute.org/>`_

Installation of Packages
========================

Make pip only use Package Bin
-----------------------------

Package Bin is configured to work as a proxy to the public `Python Package Index (PyPI) <http://pypi.python.org/pypi/>`_ so it could work as your only index. There are three ways to specify this

* Specify it each time::
   
      pip install --index-url http://username:password@pkgbin.com/username/simple/ mypackage``
   

* Modify your `pip configuration file <http://www.pip-installer.org/en/latest/configuration.html#config-files>`_ and add or update the ``[global]`` section::
   
      [global]
      index-url = http://username:password@pkgbin.com/username/simple/
   

* Set `an environment variable <http://www.pip-installer.org/en/latest/configuration.html#environment-variables>`_\ ::
   
      export PIP_INDEX_URL=http://username:password@pkgbin.com/username/simple/
   
Make pip use Package Bin as a backup source
-------------------------------------------

If you want ``pip`` to use Package Bin as a source for packages it can't find on the public PyPI, do one of these methods

* Specify it each time::
   
      ``pip install --extra-index-url http://username:password@pkgbin.com/username/simple/ mypackage``
   

* Modify your `pip configuration file <http://www.pip-installer.org/en/latest/configuration.html#config-files>`_ and add or update the ``[global]`` section::
   
      [global]
      extra-index-url = http://username:password@pkgbin.com/username/simple/
   

* Set `an environment variable <http://www.pip-installer.org/en/latest/configuration.html#environment-variables>`_\ ::
   
      export PIP_EXTRA_INDEX_URL=http://username:password@pkgbin.com/username/simple/


Isn't this insecure?
====================

It isn't optimal security, but it is as far as ``pip`` can go right now. If new methods are adopted by ``pip`` then we'll support it.
