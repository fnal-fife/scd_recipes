# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install srm-ifce
#
# You can edit this file again by typing:
#
#     spack edit srm-ifce
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class SrmIfce(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://dmc-docs.web.cern.ch/dmc-docs/srm-ifce.html"
    url = "https://github.com/cern-fts/srm-ifce/archive/v1.24.4.tar.gz"

    maintainers = [
        "marcmengel",
    ]

    version(
        "1.24.4",
        sha256="1a4b937e4ecf04e34106eb4652e18beb3e6fc81ba9c815f6d9b21e07a8a12b1e",
    )
    version(
        "1.24.3",
        sha256="3ba3023b0f1ef702dd31e29815f6988178eee1a7bb69014d36494cc2d4d288c7",
    )
    version(
        "1.24.2",
        sha256="f981afc7b40d7fc44c3a2291e8a1116b1eb07734177d87db18844085b2daded2",
    )
    version(
        "1.24.1",
        sha256="c6a7717e4907872d1b3442b3938cf49baff1f3b62dc2ff9aa4394e63cfa790f3",
    )

    depends_on("cgsi-gsoap")
    depends_on("gsoap")
    depends_on("globus-toolkit")
    depends_on("pkgconfig", type="build")
    depends_on("glib")

    def cmake_args(self):
        args = [
            "-DGLOBUS_PREFIX=%s" % self.spec["globus-toolkit"].prefix,
        ]
        return args
