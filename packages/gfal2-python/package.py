# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Gfal2Python(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://gitlab.cern.ch/dmc"
    url = "https://gitlab.cern.ch/dmc/gfal2-bindings/-/archive/v1.8.3/gfal2-bindings-v1.8.3.tar.gz"

    maintainers = [
        "marcmengel",
    ]

    version(
        "1.10.0",
        sha256="f20a39b1093e28fa4337f0c9dc1cc6789284203931aef4fbf8cd62ec2076da5d",
    )
    version(
        "1.9.5",
        sha256="5834e595c7c1800b1c68b5ae76296ea62d852136688645ef229966dcadee4f5a",
    )
    version(
        "1.9.4",
        sha256="6562fc19ff96f515fcdd12c9f0383c46c86f65e181ed196c032441c0c4a875f9",
    )
    version(
        "1.9.3",
        sha256="0142cbb822f45f833104f2eaef24bfcd88b45a3ea7ddf13d5b327dd020572918",
    )

    depends_on("boost+python")
    depends_on("gfal2")
    depends_on("python")
    extends("python")

    patch("find_package_boost.patch")

    def cmake_args(self):
        args = [
            "-DSKIP_DOC=ON",
            "-DALT_PYTHON_LOCATION=%s" % self.spec["python"].prefix.bin,
        ]
        return args
