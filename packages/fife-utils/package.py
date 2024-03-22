# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FifeUtils(Package):
    """Utility scripts for SAM, etc. """

    homepage = "https://cdcvs.fnal.gov/redmine/projects/fife-utils/wiki"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/fife-utils.v3_6_1.tar"

    version("3.7.0", sha256="abba73b57202ab316bd63e94193e7627b403359707ffeddec4ff64e37f68d2ab") 
    version("3.6.1", sha256="3cdddd19ebe62d5ec4291a9d718910e30fc1b7d897a4a73e877d6be3819e9d97")
    version("3.6.0", sha256="31840ba816d1d79c3734d455c47072cf60677c7c72ed390e386973e0711c9513")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/fife_utils.v{0}.tbz2"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")
    depends_on("sam-web-client", type="run")
    depends_on("metacat", type="run")
    depends_on("rucio-clients", type="run")
    depends_on("ifdhc", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, run_env):
        run_env.set("FIFE_UTILS_DIR", self.prefix) # for fife_launch... sigh
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
