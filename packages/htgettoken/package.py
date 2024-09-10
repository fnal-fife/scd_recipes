# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Htgettoken(PythonPackage):
    """Utility to fetch webtokens from Vault"""

    homepage = "https://github.com/fermitools/htgettoken"
    url = "https://github.com/fermitools/htgettoken/archive/refs/tags/v1.15.tar.gz"

    maintainers = ["marcmengel", "DrDaveD"]

    version("1.17", sha256="92b1c7d76dd8b103b24f7cec564c62fca9f4f2b01a5513dd8746eab6b0db06f3")
    version("1.15", sha256="87e2e72d6d79cf8df7d7b1fcf4d4570acf6e6d85566b7d2817bd777cbb82d653")
    version("1.14", sha256="69b9f725ea63231d05fb53757f18c8bbf0192419d196953f684a5f297e19aeeb")

    depends_on("python@3.8:")
    depends_on("py-pip", type="build", when="@1.16:")
    depends_on("py-wheel", type="build", when="@1.16:")
    depends_on("py-setuptools", type="build", when="@1.16:")

    depends_on("py-gssapi", when="@1.16:")
    depends_on("py-paramiko", when="@1.16:")
    depends_on("py-urllib3", when="@1.16:")

    depends_on("py-m2crypto")
    depends_on("py-pyopenssl")
    depends_on("py-kerberos")

    depends_on("jq")
    depends_on("coreutils", type="run")  # for 'base64'

    with when("@:1.15"):
        def install(self, spec, prefix):
            mkdir(prefix.bin)
            mkdir(prefix.man)
            filter_file("#!/usr/bin/python3", "#!/usr/bin/env python3", "htgettoken")
            install("htgettoken", prefix.bin)
            install("httokendecode", prefix.bin)
            install("htgettoken.1", prefix.man)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)

