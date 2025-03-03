# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPyspnego(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/jborean93/pyspnego"
    pypi = "pyspnego/pyspnego-0.6.3.tar.gz"

    maintainers = [
        "marcmengel",
    ]

    version("0.6.3", sha256="6060a0e683171090adcf92c9d319ddd334f15117fa199a703d8c9bd094d9f6c0")

    depends_on("py-cryptography")
    depends_on("py-setuptools")
