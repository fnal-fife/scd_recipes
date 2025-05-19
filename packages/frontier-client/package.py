# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install frontier-client
#
# You can edit this file again by typing:
#
#     spack edit frontier-client
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class FrontierClient(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://frontier.cern.ch/"
    url = "https://github.com/fermitools/frontier/archive/refs/tags/v2_10_2.tar.gz"

    version("2.10.2", sha256="5867230ed178e530147b8d3c756cabe79e6f338f5f8b24436baf94f9096fb31c")

    maintainers("marcmengel", "drDaveD")

    depends_on("gmake", type="build")
    depends_on("zlib")
    depends_on("openssl")
    depends_on("expat")
    depends_on("pacparser")
    depends_on("python")

    license("BSD attribution")

    def url_for_version(self, version):
        urlf = "https://github.com/fermitools/frontier/archive/refs/tags/v{}.tar.gz"
        return urlf.format(version.underscored)

    build_directory = "client"

    # for some reason with dependencies, have to run the build
    # three times -- keep getting this or that undefined

    @run_before("build")
    def double_make(self):
        print("=-=-=-=-=  initial extra builds starting =-=-=-=-=")
        for i in [1, 2, 3]:
            try:
                print("=-=- try %d =-=-=" % i)
                self.build(self.spec, self.spec.prefix)
                print("initial extra build suceeded")
            except:
                print("initial extra build failed")
        print("=-=-=-=-=  initial extra builds finished =-=-=-=-=")

    @property
    def build_targets(self):
        spec = self.spec
        return [
            "PACPARSER_DIR={}".format(spec["pacparser"].prefix),
            "OPENSSL_DIR={}".format(spec["openssl"].prefix),
            "ZLIB_DIR={}".format(spec["zlib"].prefix),
            "EXPAT_DIR={}".format(spec["expat"].prefix),
        ]

    @property
    def install_targets(self):
        return ["distdir={}".format(prefix), "install"]

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass
