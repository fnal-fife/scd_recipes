# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------

from spack.package import *
import os

class Justin(Package):
    """DUNE-Justin workflow manager client package """

    homepage = "https://justin.dune.hep.ac.uk/"

    url = "https://github.com/DUNE/dune-justin/archive/refs/tags/01.03.00.tar.gz"

    maintainers("marcmengel", "Andrew-McNabb-UK", "calcuttj")

    license("Apache-2")

    version("01.04.01", sha256="40d5101140e94a8cf862931e6dfdfc01d30562ba75a0c4bcef7125e0281b4eed")
    version("01.04.00", sha256="46557f0346f96705c94a75e280747d8af209fa1c9b896f08508b98ff4d915e2d")
    version("01.03.00", sha256="688b96531c3190b66e4db4c10efb7ccc6e9bcdfad470f4cd6cde934df0d8fb20")

    depends_on("python@3.3:", type=("build", "run"))
    depends_on("rucio-clients", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path + "/commands", prefix.bin)   
        install_tree(self.stage.source_path + "/jobutils", prefix.jobutils)   
        makedirs(prefix.man.man1)
        os.system("mv %s/*.1 %s" % (prefix.bin, prefix.man.man1))

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("MANPATH", self.prefix.man)

