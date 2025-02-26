# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Htgettoken(PythonPackage):
    """Utility to fetch webtokens from Vault"""

    homepage = "https://github.com/fermitools/htgettoken"
    url = "https://github.com/fermitools/htgettoken/archive/refs/tags/v1.15.tar.gz"

    maintainers = ["marcmengel", "DrDaveD"]

    version("2.0-2", sha256="80b1b15cc4957f9d1cb5e71a1fbdc5d0ac82de46a888aeb7fa503b1465978b13")
    version("2.0", sha256="6c14bbc8909d5ecd3fd21a4bef92334aa353a9f8d5ae73d7c42edf1caa37b0b9")
    version("1.21", sha256="d0651cac41f2dafce5ba160dccef9abd2ba950e318700a4deebf36adb3af1ff1")
    version("1.20", sha256="11d53046276986403c9e9d3eacc10fb4baa3d385d453111ecf3054438957dc36")
    version("1.19", sha256="944652d0c0dc170f0851fc73329660d4bda4055e12eeac6869963495f5ba1422")
    version("1.18", sha256="5f0833e9352c2881f7d08571e48e6370d7a9714ea15d90eb89588684c63bd2b3")
    version("1.17", sha256="92b1c7d76dd8b103b24f7cec564c62fca9f4f2b01a5513dd8746eab6b0db06f3")
    version("1.15", sha256="87e2e72d6d79cf8df7d7b1fcf4d4570acf6e6d85566b7d2817bd777cbb82d653")
    version("1.14", sha256="69b9f725ea63231d05fb53757f18c8bbf0192419d196953f684a5f297e19aeeb")

    depends_on("python@3.8:")
    depends_on("py-pip", type="build", when="@1.99:")
    depends_on("py-wheel", type="build", when="@1.99:")
    depends_on("py-setuptools", type="build", when="@1.99:")

    depends_on("py-gssapi", when="@1.99:")
    depends_on("py-paramiko", when="@1.99:")
    depends_on("py-urllib3", when="@1.99:")

    depends_on("py-m2crypto", when="@:1.98")
    depends_on("py-pyopenssl", when="@:1.98")
    depends_on("py-kerberos", when="@:1.98")

    depends_on("jq")
    depends_on("coreutils", type="run")  # for 'base64'

    with when("@:1.15"):

        def install(self, spec, prefix):
            mkdir(prefix.bin)
            mkdir(prefix.man)
            pip = which("pip3")
            pip("install", "--prefix", prefix, ".")
            # filter_file("#!/usr/bin/python3", "#!/usr/bin/env python3", "htgettoken")
            # install("htgettoken", prefix.bin)
            # install("httokendecode", prefix.bin)
            # install("htgettoken.1", prefix.man)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix + "lib/python3.9/site-packages")
