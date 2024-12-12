# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-cvs2svn
#
# You can edit this file again by typing:
#
#     spack edit py-cvs2svn
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyCvs2svn(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = ""
    url = "https://github.com/marcmengel/cvs2svn/archive/refs/tags/v2.4.0_pre.tar.gz"

    version(
        "2.4.0_pre",
        sha256="29ac8a3ab60d0eab231529297d9a83ac2fc7bed1cf152b720185f233a59b7d3d",
    )

    maintainers = [
        "marcmengel",
    ]

    depends_on("python@:3.0.0")
    # depends_on('py-setuptools', type='build')

    def build_args(self, spec, prefix):
        args = []
        return args
