# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PomsClient(Package):
    """python / command line package for POMS clients"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/poms-client/wiki"
    url = "https://github.com/fermitools/poms/archive/refs/tags/v4_4_2.tar.gz"

    version("4.5.2", sha256="a424ebf860cec198c8ab6edadf80f17ccbc0edb5914a870026d5e0332a50c131")
    version("4.4.2", sha256="d5b2d602072af08a46343a59d8ecad1c6daec8fd5fb351f8a91eb5164311c2e7")

    def url_for_version(self, version):
        url = "https://github.com/fermitools/poms/archive/refs/tags/client_v{0}.tar.gz"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")

    def install(self, spec, prefix):
        install_tree(self.stage.source_path+"/poms_client", prefix)

    def setup_run_environment(self, run_env):
        run_env.set("POMS_CLIENT_DIR", self.prefix)
        run_env.set("CURL_CA_PATH", "/etc/grid-security/certificates")
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "/python")
