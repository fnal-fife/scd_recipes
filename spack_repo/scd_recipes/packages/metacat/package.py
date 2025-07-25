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

    version("4.1.1", sha256="12a4e5dd9aed7159531b9de685f739b4093a6d9d4bf76dcaaff72dd89a435ce8")
    version("4.1.0", sha256="4c7ebdf5eeed52a731d3286fea72bfd0037f952e6aafa33f0f18fc1cc3f35f59")
    version("4.0.2", sha256="84b46108779db6e3c9d2bd8f68a2ab5326c05ffaec7d40986dcc18219f9f799e")
    version("4.0.1.1", sha256="477271395ad2a12de716bf6ff8cbe5e21392e6fbfa4ad94b6fa7141aa8c4b9ba")
    version("4.0.1", sha256="477271395ad2a12de716bf6ff8cbe5e21392e6fbfa4ad94b6fa7141aa8c4b9ba")
    version("4.0.0", sha256="d453a628e6b0b623234254e0ccb5ad9bad826433cbffe615f146a7f433273041")
    version("3.43.0", sha256="536114ad6a68f199335ae2de6f5e1edc698b2f74c7988a992b21c48add018df8")
    version("3.42.1", sha256="af26f91dae527ae102e9229357a392ffad6b790768b8575ba7fcb3fe5285f4b7")
    version("3.38.0", sha256="2d3a5313590db47a98cea25f68947325203fb4b466751f2c2c841172027e666a")
    version("3.37.0", sha256="af47c1ef1ad0ee343c7e785342298247dbf2d0f8062d3f38a23e8808b1c0a808")
    version("3.35.0", sha256="8e6806a62fcade61111879f0fb29ec52f8029b860869fb9793fb704829799eb3")
    version("3.34.0", sha256="3be8816f74f4d8be0ef46c3042731576a4e67e4424506d58fb06030411903214")
    version("3.33.9", sha256="98f8a81f40d99149b0862d58421b697e19dd97996dd45833f4ebb2cd1ffa22e5")
    version("3.33.7", sha256="1f40229c982560d0a39e547df20e23c4a058c1ee7a81fbb97d9549644b15ce16")
    version("3.33.0", sha256="024e790bc887e9611516754aefef3b98cba3c42fed76814739067fece0ecb976")
    version("3.30.0", sha256="7c4e6711a1fe18ceb68b77bf50b1cad34d09370c15c77b016c7717967e199f41")

    version("3.20.0", sha256="4f981b755bb914c503db9480b4dab19093a3f5680622c5d9b1913deb17b7ed12")
    version("3.19.1", sha256="c7473233a80926905ec310dfb78a5d61cb52fec9e3f2e154fed577a020573512")
    version("3.19.0", sha256="6366f1379eb9946e7ff29d972b3abb253a59f7e183f43fb598e1ae6ded6b1424")

    version("main", branch="main")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    with when("@3.20.1:"):
        variant("client_only", default=True)

    with when("@:3.20.0"):
        variant("client_only", default=False)

    depends_on("py-pyjwt", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-pythreader@2.8.0:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"), when="~client_only")
    depends_on("py-scitokens", type=("build", "run"), when="~client_only")
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
