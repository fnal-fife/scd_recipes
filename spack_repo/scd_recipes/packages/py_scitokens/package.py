# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyScitokens(PythonPackage):
    """Scitokens library for python"""

    homepage = "https://scitokens.org/"
    pypi = "scitokens/scitokens-1.8.1.tar.gz"

    maintainers("marcmengel")

    license("Apache2.0")

    version("1.8.1", sha256="f255383d9c7402b3fcd20d5ed26a6b407b4be8bec6f282d0af29b6275382b54d")

    depends_on("py-setuptools", type="build")
    depends_on("py-cryptography")
    depends_on("py-pyjwt")

    def config_settings(self, spec, prefix):
        settings = {}
        return settings
