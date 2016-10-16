Psynteract OpenSesame integration
=================================

**Easily build real-time interactive experiments with OpenSesame.**

This repository provides the OpenSesame integration of the *psynteract*
library. The documentation of the package can be found in its `own
repository <https://github.com/psynteract/psynteract-docs>`__.

----

``psynteract-os`` is developed jointly by **Pascal Kieslich** and **Felix
Henninger**, with a focus on the OpenSesame integration and the underlying
Python library and backend, respectively. It is published under the `GNU General
Public License (version 3) <LICENSE>`__.

Installation
------------

**Latest stable version**

To install the latest release, please run the following commands in OpenSesame's
`debug window <http://osdoc.cogsci.nl/manual/interface/#the-debug-window>`__:

.. code-block:: python

    import pip
    pip.main(['install', '--process-dependency-links',
      'https://github.com/psynteract/psynteract-os/archive/stable.zip'])

You'll need to restart OpenSesame after the installation for the plugins and
extension to work.

If the installation fails due to missing write access, you may have to run
OpenSesame with administrator privileges for the installation (on Windows,
right-click the OpenSesame program icon and select `Run as Administrator
<https://technet.microsoft.com/en-us/library/cc732200.aspx>`__).

The `installation of plugins
<http://osdoc.cogsci.nl/manual/environment/#installing-plugins-and-extensions>`__
is covered in more detail in the OpenSesame documentation, which also covers
alternate methods. To install the package manually, please download the archive
attached to the `latest release
<https://github.com/psynteract/psynteract-os/releases/latest>`__. In this case,
you'll need to install `psynteract-py
<https://github.com/psynteract/psynteract-py>`__ and its dependencies manually.

`Release notes for the latest version
<https://github.com/psynteract/psynteract-os/releases/latest>`__ are available,
as for all `previous releases
<https://github.com/psynteract/psynteract-os/releases>`__.

**Development version**

To install the latest development version, please follow the above instructions,
replacing the command with the following:

.. code-block:: python

    import pip
    pip.main(['install', '--process-dependency-links',
      'https://github.com/psynteract/psynteract-os/archive/master.zip'])

Citation
--------

Please drop us a line if you've used the library: We sincerely love to hear
from our users!

If you use ``psynteract`` in your published research, we kindly ask that you
cite the associated article as follows:

    Henninger, F., Kieslich, P. J., & Hilbig, B. E. (in press). Psynteract:
    A flexible, cross-platform, open framework for interactive experiments.
    *Behavior Research Methods*. doi:`10.3758/s13428-016-0801-6
    <https://dx.doi.org/10.3758/s13428-016-0801-6>`__

Acknowledgments
---------------

We would like to thank Anja Humbs at the `University of Mannheim Chair of
Experimental Psychology <http://cognition.uni-mannheim.de/>`__ for her help in
selecting the icons and testing the plugins, Luisa Horsten and Sina Klein at
the `University of Landau Cognition Lab <http://cognition.uni-landau.de/>`__,
and Hosam Alqaderi and Susann Fiedler at the `Max Planck Institute for Research
on Collective Goods, Bonn <http://coll.mpg.de/>`__, for testing the software and
providing valuable feedback.

This work was supported by the University of Mannheim’s `Graduate School of
Economic and Social Sciences <http://gess.uni-mannheim.de/>`__, which is funded
by the German Research Foundation.

**Shoulders of giants**

Psynteract depends heavily on several additional libraries. In particular, we
are indebted to the authors of and contributors to `PyCouchDB (written by Andrey
Antukh) <https://pycouchdb.readthedocs.org/>`__ and `Requests (by Kenneth Reitz
and collaborators) <http://python-requests.org/>`__. The OpenSesame integration
also incorporates our own `Python library
<https://github.com/psynteract/psynteract-py>`__.

Of course, none of this would be possible without the excellent work of the
`OpenSesame development team <http://osdoc.cogsci.nl/about/>`__ led by
`Sebastiaan Mathôt <http://www.cogsci.nl/smathot>`__.

The icons for ``psynteract-os`` are based on the `Moka Icon Theme  (by Sam
Hewitt) <https://snwh.org/moka>`__, and contain elements from the `Faenza Icon
Set (by Titheum) <http://tiheum.deviantart.com/art/Faenza-Icons-173323228>`__,
both of which make us look undeservedly professional.
