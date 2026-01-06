# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class FifeUtils(Package):
    """Utility scripts for SAM, etc."""

    homepage = "https://github.com/fnal-fife/fife-utils/wiki"
    url = "https://github.com/fnal-fife/fife-utils.git"
    list_url = "https://github.com/fnal-fife/fife-utils/tags"
    git = "https://github.com/fnal-fife/fife-utils.git"

    version("3.7.7", sha256="96e940926b58ec21876a92e262b277fda161907e1c561fec592789e34c61f221")
    version("3.7.6", sha256="25118f791516751a410a9b1ba2a42b7ea425764f135b50628c8657c3ebea8e81")
    version("3.7.5", sha256="81b18626b30a03fa63cbcfd13f8959c362bed0871c7c3e828a1ff0b4e9bf783e")
    version("3.7.4", sha256="c0647db710d1a914c4756440fdfde4e5b537845e018bf05b41758354587e5420")
    version("3.7.3", sha256="9b0ed7963adb1bae03207a686196bd4171cb2bc38f3530b18d237292abe15154")
    version("3.7.2", sha256="309b3174e77ed90e5dc155738af702be8e461d957c3dd61c72cb77c6b226c873")
    version("3.7.0", sha256="1b3396a19b93cd9907ae5f0175973d57f2b37a4c5d95f82ec26109aef198dba3")
    version("3.6.1", sha256="4086685e4985db55b4081ef28085da5746e5496a3cbf1c9798bdd28b42b70e1b")
    version("3.6.0", sha256="4cf32203c2382968871d5f959a58106090da954a898255e1979c67db65b72752")
    version("3.5.1", sha256="7b1463ce9fd275152daaf7b54772c0d6ffaa528f65270af65f17bdf038990fe3")
    version("develop", branch="develop", get_full_repo=True)


    def url_for_version(self, version):
        urlf = "https://github.com/fnal-fife/fife-utils/archive/refs/tags/v{0}.tar.gz"
        return urlf.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")
    depends_on("sam-web-client", type="run")
    depends_on("data-dispatcher", type="run", when="@3.6.0:")
    depends_on("metacat", type="run", when="@3.6.0:")
    depends_on("py-rucio-clients", type="run", when="@3.6.0:")
    depends_on("ifdhc", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, run_env):
        run_env.set("FIFE_UTILS_DIR", self.prefix)  # for fife_launch... sigh
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/lib")
