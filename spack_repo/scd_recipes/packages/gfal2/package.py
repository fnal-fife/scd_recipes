# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Gfal2(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://dmc-docs.web.cern.ch/dmc-docs/gfal2/gfal2.html"
    url = "https://gitlab.cern.ch/dmc/gfal2/-/archive/v2.12.0/gfal2-v2.12.0.tar.gz"

    maintainers = ["marc.mengel@gmail.com", "github_user2"]

    version(
        "2.19.0",
        sha256="b80fa6dcb612911ae85897faa0a21e88e666f4319070855a2970f41771a7ed50",
    )
    version(
        "2.18.2",
        sha256="1b75e8431592f82b21eb228ae66bb7731534e2e19f7c7871910895aaaad9b3a9",
    )
    version(
        "2.18.1",
        sha256="ffd56da046049ae56b457ee2a38c21460fdadf966a6e86d1e718a985d4cc6b7d",
    )
    version(
        "2.18.0",
        sha256="3298f353ea46e7ec811ee9364273c868bbd0fde34b17cc33a0dbc4fd591fc585",
    )

    depends_on("boost +python")
    depends_on("davix +thirdparty")
    depends_on("json-c")
    depends_on("globus-toolkit")
    depends_on("libssh2")
    depends_on("glib")
    depends_on("pkgconfig", type="build")
    depends_on("srm-ifce")
    depends_on("xrootd")
    depends_on("googletest")
    #
    # ommitting these 'cause we'ere getting them from RPMS or skipping a plugin
    #
    # depends_on('rfio')
    # depends_on('lcg-dm')
    # depends_on('openldap')

    patch("find_xrootd.patch")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ["-DPLUGIN_RFIO=FALSE"]
        return args
