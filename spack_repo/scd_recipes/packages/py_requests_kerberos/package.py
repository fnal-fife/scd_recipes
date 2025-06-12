# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyRequestsKerberos(PythonPackage):
    """Python kerberos connections package"""

    homepage = "https://github.com/requests/requests-kerberos"
    pypi = "requests-kerberos/requests-kerberos-0.14.0.tar.gz"

    maintainers = [
        "marcmengel",
    ]

    version("0.14.0", sha256="cda9d1240ae5392e081869881c8742d0e171fd6a893a7ac0875db2748e966fd1")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-pyspnego", type=("build", "run"))
    depends_on("py-cryptography", type=("build", "run"))

    def setup_build_environment(self, env):
        env.prepend_path("PYTHONPATH", self.spec["py-setuptools"].prefix)
