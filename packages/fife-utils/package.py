# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FifeUtils(Package):
    """Utility scripts for SAM, etc. """

    homepage = "https://cdcvs.fnal.gov/redmine/projects/fife-utils/wiki"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/fife-utils.v3_6_1.tar"

    version("3.7.2", sha256="2b4344d821e5650eda011e66375c47f808b5584df4ae2a591f345a94cc45711b")
    version("3.7.0", sha256="8d0efe2e007b0bb821accfad85ad455026fbe59b19f27c80edeb224db66cc74c")
    version("3.6.1", sha256="7bb1e2aeb703cb9b3ed098416c035509be85896f3891bc87afa14e21fa7132f5")
    version("3.6.0", sha256="31840ba816d1d79c3734d455c47072cf60677c7c72ed390e386973e0711c9513")

    def url_for_version(self, version):
        urlf = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/fife_utils.v{0}.tar"
        return urlf.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")
    depends_on("sam-web-client", type="run")
    depends_on("data-dispatcher", type="run")
    depends_on("metacat", type="run")
    depends_on("rucio-clients", type="run")
    depends_on("ifdhc", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, run_env):
        run_env.set("FIFE_UTILS_DIR", self.prefix) # for fife_launch... sigh
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/lib")
