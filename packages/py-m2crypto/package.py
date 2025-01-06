# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyM2crypto(PythonPackage):
    """M2Crypto is the most complete Python wrapper for OpenSSL"""

    homepage = "https://gitlab.com/m2crypto/m2crypto"
    pypi = "M2Crypto/M2Crypto-0.38.0.tar.gz"

    maintainers = [
        "marcmengel",
    ]

    version(
        "0.38.0",
        sha256="99f2260a30901c949a8dc6d5f82cd5312ffb8abc92e76633baf231bbbcb2decb",
    )

    depends_on("py-setuptools", type="build")
    depends_on("swig@2.0.10:", type="build")
    depends_on("openssl@1.0.1e:", type=("build", "run"))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = [
            "--openssl={0}".format(self.spec["openssl"].prefix),
        ]
        return args
