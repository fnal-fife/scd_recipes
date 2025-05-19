# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class Voms(AutotoolsPackage):
    """
    VOMS server and C++ APIs.

    The Virtual Organization Membership Service (VOMS) is an attribute
    authority which serves as central repository for VO user authorization
    information, providing support for sorting users into group hierarchies,
    keeping track of their roles and other attributes in order to issue
    trusted attribute certificates and SAML assertions used in the Grid
    environment for authorization purposes.
    """

    homepage = "https://italiangrid.github.io/voms/"
    url = "https://github.com/italiangrid/voms/archive/refs/tags/v2.0.16.tar.gz"

    maintainers = ["marcmengel"]

    version(
        "2.0.16",
        sha256="13df81e4f596a059284051fb58d0d7ca596506577c7ef8ba25d4542c5d6ca5a9",
    )
    version(
        "2.0.15",
        sha256="c6d081aba5fc44d8b8d14ae4a6445a24af68e4c5a036afdd788bcb7460459f90",
    )

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("gsoap", type=("build", "run"))
    depends_on("expat", type=("build", "run"))

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        os.mkdir("aux")
        os.mkdir("src/autogen")
        autoreconf("--install", "--verbose")

    @run_before("configure")
    def fix_configure(self):
        filter_file("/usr/bin/soapcpp2", "soapcpp2", "configure")
        filter_file(r"\(\*role\) = '\\0';", "*(*role) = '\\0';", "src/server/vomsd.cc")

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = [
            "--with-gsoap-wsdl2h={0}/wsdl2h".format(self.spec["gsoap"].prefix.bin),
            # '--without-server',
        ]
        return args

    def setup_build_environment(self, env):
        env.prepend_path("PATH", self.spec["gsoap"].prefix.bin)
        env.append_flags("CPPFLAGS", "-I{0}".format(self.spec["gsoap"].prefix.include))
        env.append_flags("LDFAGS", "-L{0}".format(self.spec["gsoap"].prefix.lib))
        env.append_flags("CPPFLAGS", "-I{0}".format(self.spec["expat"].prefix.include))
        env.append_flags("LDFAGS", "-L{0}".format(self.spec["expat"].prefix.lib))
        env.append_flags("LDFLAGS", "-lz")
