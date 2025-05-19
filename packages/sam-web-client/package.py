# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class SamWebClient(Package):
    """Client package for SAM data management system webservice"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/sam-web-client/wiki"
    url = "http://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/sam-web-client.v3_0.tar"

    version("3.6", sha256="ba1f59f2ca663271ad69b6aa96ebb4d664055c1af06c3ca986cd918aed0a9e2d")
    version("3.5", sha256="840241c09a10669c1b7f28d178baa8b24ae6377aaaf7e4d619ad234182cf1214")
    version("2.0", sha256="9a2729e01a0e143f8d30fdd17a40038e088a86931b14950dcb370746af7e9cba")
    version("2.1", sha256="d2e875b44ea25fa3a681f24e15d6f525c3be3c9ccc54e162981814dbccaf801a")
    version("3.0", sha256="2e1f7650b0ae0c13b9aead9a3a85b1e2227b2a94ad55a82a09d21e042904df3d")
    version("3.1", sha256="886c4c6eb0790f57e6622a26c3f24fd259ecb4c7f88bbd7b322c3daab8b3613d")
    version("3.2", sha256="f65a65ff683467214babbc2c81ddcf082f638b47fdf7a8af163f1beb18d85e77")
    version("3.3", sha256="d13916a75983eda40812f31aa1329d603e4eb3356ee667496f666cd69767c082")
    version("3.4", sha256="74cc27e4251e6993a2667f526ba19f7686a55249fccc198fee7ddf5a38ebee62")

    def url_for_version(self, version):
        url = "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/sam-web-client.v{0}.tbz2"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
