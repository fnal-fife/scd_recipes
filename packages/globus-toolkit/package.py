# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
import os


class GlobusToolkit(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.globus.org/toolkit/"
    url = "https://github.com/globus/globus-toolkit/archive/globus_5_2_4.tar.gz"

    maintainers = [
        "marc.mengel@gmail.com",
    ]

    version(
        "6_0", sha256="8091b293d5a08a35128334cb4f17f3da5f83457639415b31c523bb511474be87"
    )
    version(
        "5_2_4rc1",
        sha256="ba48baa52f79d23afa76d6e024a9b33a1bb8b8d915d0458bf0077fdef69bbe2b",
    )
    version(
        "5_2_4",
        sha256="9fd4588c3a0ee6ff80bb8aa0390ab7cf39fa76709c2f61b2da3f2df273ac9c96",
    )
    version(
        "5_2_3",
        sha256="a9b620c19f776f878b165f3a9027352fecefaa37cef90a95927e7901ff05e594",
    )

    patch("globus.patch")

    depends_on("pkgconfig", type="build")
    depends_on(
        "autoconf@2.69", type="build"
    )  # doesnt seem to work with other versions...
    depends_on("automake", type="build")
    depends_on("libtool@2.4.2", type="build")
    depends_on("openssl")

    def autoreconf(self, spec, prefix):
        # make sure there's an ltmain.sh
        os.environ["HAVE_LTDL"] = "1"
        open("ltmain.sh", "a").close()
        try:
            autoreconf("-ivf")
        except:
            pass
        try:
            automake("--add-missing")
        except:
            pass
        autoconf()
        try:
            autoupdate()
        except:
            pass
        try:
            self.patch_configure()
            configure(configure_args())
        except:
            pass
        try:
            os.mkdir("libltdl")
        except:
            pass
        f = open("libltdl/Makefile", "w")
        f.write("all:\n\ninstall:\n\n")
        f.close()

    @run_before("autoreconf")
    def patch_configure(self):
        with working_dir(self.build_directory):
            os.system(
                "find . -name Makefile.in -print | xargs perl -pi.bak -e 's{./config.status --recheck}{/dev/null};'"
            )
            if os.path.exists("aclocal.m4"):
                filter_file("libltdl\.la", "libltdl.so", "aclocal.m4")
            if os.path.exists("configure"):
                filter_file("libltdl\.la", "libltdl.so", "configure")

    def configure_args(self):
        if os.path.exists(self.spec["libtool"].prefix.lib64):
            libpath = self.spec["libtool"].prefix.lib64
        else:
            libpath = self.spec["libtool"].prefix.lib
        return [
            "--with-ltdl-include=%s" % self.spec["libtool"].prefix.include,
            "--with-ltdl-lib=%s" % libpath,
        ]
