=================
Using Package Bin
=================

How Python Packages Work
========================

#. Python uses different tools for uploading packages and downloading packages

   #. `distribute <http://packages.python.org/distribute/>`_ for packaging and uploading.
   
   #. `pip <http://www.pip-installer.org/en/latest/index.html>`_ for installing and managing within a project or environment.

#. Each tool uses different mechanisms and protocols.

   #. ``distribute`` uses an `XML-RPC-based API <http://wiki.python.org/moin/PyPiXmlRpc>`_ for creating a package entry (registering) and uploading the package contents to the package index.
   
      #. There is a `JSON API <http://wiki.python.org/moin/PyPiJson>`_ for querying information regarding individual packages.
   
   #. ``pip`` works by either parsing an HTML page or FTP listing for links, or checking out a source repository. It doesn't use an API.


Using Package Bin as Your Primary Index
=======================================



index-servers =
    pypi
    pkgbin

[pypirc]
servers =
    pypi
    pkgbin

[pkgbin]
username:joecool
password:Pa55w0rd
repository:http://pkgbin.com/joecool/pypi/

[pypi]
username:joecool
password:MyPa55w0rd
