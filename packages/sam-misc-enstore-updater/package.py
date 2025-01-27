# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class SamMiscEnstoreUpdater(Package):
    """Utility to update SAM tape locations from Enstore"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/sam-misc/wiki"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/sam-misc-updater.1_0.tar"

    version("1.1", sha256="4153bf2dcffc3b020755f7ae7f76cdd66e8ba16b392693edbbb5ef0a069759ed")
    version("1.0", sha256="b4b2156647c25fc0d4f65050bc76fb630fe64f7896dd4a3b1ca7a71e57235bcf")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/sam-misc-enstore-updater.{0}.tbz2"
        return url.format(version.underscored)

    depends_on("python@:3", type=("build", "run"), when="@1.0")
    depends_on("python@3.3:", type=("build", "run"), when="@1.1:")
    depends_on("py-pysqlite3", type=("build", "run"))
    depends_on("py-psycopg2", type=("build", "run"))
    depends_on("encp", type=("run",)) 

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
