# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class Cigetcert(PythonPackage):
    """cigetcert gets an X.509 certificate from a SAML 2.0 Service Provider
    (SP) such as CILogon using the Enhanced Client or Proxy (ECP)
    profile. Optionally it can also get a grid proxy certificate and/or
    transfer a grid proxy to MyProxy. It was developed for the Fermilab
    Distributed Computing Access with Federated Identities (DCAFI) project
    but is intended to be usable by other projects."""

    homepage = "https://github.com/fermigtools/cigetcert"
    url = "https://github.com/fermitools/cigetcert/archive/refs/tags/1.20.tar.gz"

    maintainers = ["marcmengel", "DrDaveD"]

    version(
        "1.20",
        sha256="31831bb6f26ed2f43ee10b5d3c2529c26eb1fb52ca9b9f9fabdd547c25593525",
    )

    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-lxml")
    depends_on("py-m2crypto")
    depends_on("py-kerberos")
    depends_on("py-pyopenssl")

    def global_options(self, spec, prefix):
        options = []
        return options

    def install_options(self, spec, prefix):
        options = []
        return options

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
