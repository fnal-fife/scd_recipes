# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyServiceIdentity(PythonPackage):
    """service_identity aspires to give you all the tools you need for verifying whether a certificate is valid for the intended purposes."""

    homepage = "https://service-identity.readthedocs.io/"
    url = "https://pypi.io/packages/source/s/service_identity/service_identity-18.1.0.tar.gz"

    version(
        "18.1.0",
        sha256="0858a54aabc5b459d1aafa8a518ed2081a285087f349fe3e55197989232e2e2d",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-attrs@16.0.0:", type=("build", "run"))
    depends_on("py-pyasn1-modules", type=("build", "run"))
    depends_on("py-pyasn1", type=("build", "run"))
    depends_on("py-cryptography", type=("build", "run"))
