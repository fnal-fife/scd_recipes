# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class Gsoap(AutotoolsPackage):
    """gSOAP is the top-rated agile development framework for C/C++ Web service APIs and XML"""

    homepage = "https://www.genivia.com/products.html"

    url = "https://sourceforge.net/projects/gsoap2/files/gsoap_2.8.114.zip/download"
    list_url = "https://sourceforge.net/projects/gsoap2/files/"

    def url_for_version(self, version):
        # these days sourceforge only has a URL that ends in the zip file if you followed
        # the download link recently:
        # so we have curl ping that and then take from where it sends you...
        fetch_first = (
            "https://sourceforge.net/projects/gsoap2/files/gsoap_%s.zip/download" % version
        )
        os.system("curl --output /dev/null --silent --max-redirs 0 '%s'" % fetch_first)
        return "https://downloads.sourceforge.net/project/gsoap2/gsoap_%s.zip" % version

    maintainers = [
        "marcmengel",
    ]
    version("2.8.131", sha256="e5e1a4ea25fea56ebd62d7b94a089c29e9394b6394ad362762297b7cb31622df")
    version("2.8.126", sha256="b65190ebf8c2517d6fafbdc2000bc7bc650d921a02f4aa53eb1e3df267592c4a")
    version("2.8.123", sha256="e018500ac942bb7627612cc9a8229610efe293a450359c413da1a006eb7c193d")
    version("2.8.121", sha256="d5a66b9d5189143a6adba757a085f84d3c31c03b2948939cf99851003a2934a8")
    version("2.8.119", sha256="8997c43b599a2bfe4a788e303a5dd24bbf5992fd06d56f606ca680ca5b0070cf")
    version("2.8.114", sha256="aa70a999258100c170a3f8750c1f91318a477d440f6a28117f68bc1ded32327f")
    version("2.8.113", sha256="e73782b618303cf55ea6a45751b75ba96797a7a12967ed9d02e6d5761977e73a")
    version("2.8.112", sha256="05345312e0bb4d81c98ae63b97cff9eb097f38dafe09356189f9d8e235c54095")
    version("2.8.111", sha256="f1670c7e3aeaa66bc5658539fbd162e5099f022666855ef2b2c2bac07fec4bd3")

    depends_on("openssl")
    depends_on("pkgconfig", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")

    def configure_args(self):
        return ["--enable-ipv6"]

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.prepend_path("PKG_CONFIG_PATH", "%s/lib/ldconfig" % self.prefix)

    def flag_handler(self, name, flags):
        if not name in ["cflags", "cxxflags", "cppflags"]:
            return (flags, None, None)

        flags.append(self.compiler.cc_pic_flag)

        return (None, None, flags)
