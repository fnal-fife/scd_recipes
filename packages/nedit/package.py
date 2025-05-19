# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Nedit(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://en.wikipedia.org/wiki/NEdit"
    url = "https://github.com/unixwork/xnedit/archive/refs/tags/v1.5.3.tar.gz"

    maintainers("marcmengel")

    license("GPL")

    version("1.5.3", sha256="89421abbcb91f27e122b874769ca60021802735ea527fc6ae5b3d50061f81120")
    version("1.5.2", sha256="2f9710b661f8ec5d371a3385fa480c7424e2f863938a8e2ae71cb17397be3f91")
    version("1.5.1", sha256="c871589e912ed9f9a02cc57932f5bb9694ec91cc5487be0cd55e7d3aade372d6")

    depends_on("motif")
    depends_on("libx11")
    depends_on("xproto")
    depends_on("freetype")
    depends_on("pkg-config", type="build")

    def patch(self):
        filter_file(r"\$\(shell pkg-config --cflags xft fontconfig\)", "$(shell pkg-config --cflags xft fontconfig freetype2)", "makefiles/Makefile.linux")

    def build(self, spec, prefix):
        make(str(spack.platforms.host()))

    def install(self, spec, prefix):
        make("DESTDIR=%s" % prefix, "install")

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass
