# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *
import glob


class Metacat(PythonPackage):
    """"""

    homepage = "https://metacat.readthedocs.io/en/latest/index.html"
    pypi = "metacat-client/metacat_client-4.0.1.tar.gz"
    git = "https://github.com/fermitools/metacat.git"

    maintainers = ["marcmengel", "ivmfnal"]

    version("4.1.5", sha256="0fc59bc0f8b834c19204010125124b8196115698197b5a46a6cd24f7b1ed02a1")
    version("4.1.4", sha256="37344baf0c91ec974d6f123306f86f02c38e9a8c38119652da0537b11117e45c")
    version("4.1.3", sha256="7605dba55c9ea63241f21a483859e7a2d54924d96f34f8b4ab51a85a89c3446b")
    version("4.1.2", sha256="01e0d0af3b632c836fc6da587b3a2ca7c3aadd0f362875c38fc6a60d946d53a1") 
    version("4.1.1", sha256="12a4e5dd9aed7159531b9de685f739b4093a6d9d4bf76dcaaff72dd89a435ce8")
    version("4.1.0", sha256="4c7ebdf5eeed52a731d3286fea72bfd0037f952e6aafa33f0f18fc1cc3f35f59")
    version("4.0.2", sha256="84b46108779db6e3c9d2bd8f68a2ab5326c05ffaec7d40986dcc18219f9f799e")
    version("4.0.1.1", sha256="477271395ad2a12de716bf6ff8cbe5e21392e6fbfa4ad94b6fa7141aa8c4b9ba")
    version("4.0.1", sha256="477271395ad2a12de716bf6ff8cbe5e21392e6fbfa4ad94b6fa7141aa8c4b9ba")
    version("4.0.0", sha256="d453a628e6b0b623234254e0ccb5ad9bad826433cbffe615f146a7f433273041")

    version("main", branch="main")
    version("develop", branch="develop")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-pyjwt", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-pythreader@2.8.0:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-scitokens", type=("build", "run"))
    depends_on("py-lark", type=("build", "run"))
    depends_on("py-wsdbtools", type=("build", "run"))

    # @run_before("install")
    # def use_setup_full(self):
    #    with when("~client_only @3.20.1:"):
    #        rename("setup.py","setup_client_only.py")
    #        rename("setup_full.py", "setup.py")

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PATH", self.spec.prefix.bin)
        libdir = glob.glob(str(self.spec.prefix.lib) + "/python*/site-packages")[0]
        run_env.prepend_path("PYTHONPATH", libdir)
