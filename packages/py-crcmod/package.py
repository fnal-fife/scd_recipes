# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCrcmod(PythonPackage):
    """a Python module for generating objects that compute the Cyclic Redundancy Check (CRC)"""

    homepage = "http://crcmod.sourceforge.net/"
    url = "https://pypi.io/packages/source/c/crcmod/crcmod-1.7.tar.gz"

    version(
        "1.7", sha256="dc7051a0db5f2bd48665a990d3ec1cc305a466a77358ca4492826f41f283601e"
    )

    depends_on("py-setuptools", type="build")
