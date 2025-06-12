# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Kx509(Package):
    """kx509 - get an X.509 certificate for Fermilab using kerberos"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://redmine.fnal.gov/projects/dcafi"
    url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/dcafi.kx509-v3_1_1.tbz2"

    version("3.1.1", sha256="916131a6a327ece2e14fe3fb73203f84c6d6193558c4da4d430a8053c699f0fa")
    version("3.1.0", sha256="ada03d41bc77e7723eafbe4382e8a3017ca00c1ea68efd7bacc61734328d4652")
    version("3.0.0", sha256="80fa4636ca0840b87966623470d84fad9ab390ff39e3dde59a50f3706759e116")

    depends_on("cigetcert", type="run")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/dcafi.kx509-v{0}.tbz2"
        return url.format(version.underscored)

    def install(self, spec, prefix):
        mkdir(prefix.ups)
        mkdir(prefix.bin)
        mkdir(prefix.man)
        install_tree(self.stage.source_path + "/upsupd/kx509", prefix.ups)
        install(self.stage.source_path + "/kx509/kx509", prefix.bin)
        install(self.stage.source_path + "/kx509/kx509.1", prefix.man)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
