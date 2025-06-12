# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.perl import PerlPackage
from spack.package import *


class PerlDataSectionSimple(PerlPackage):
    """Read data from __DATA__"""

    homepage = "https://metacpan.org/pod/Data::Section::Simple"
    url = "https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Data-Section-Simple-0.07.tar.gz"

    maintainers = ["marcmengel"]

    version("0.07", sha256="0b3035ffdb909aa1f7ded6b608fa9d894421c82c097d51e7171170d67579a9cb")
    version("0.06", sha256="e9587d12180bf2e478bafd36d747c669d03de1d36c7c4623176abe67c4cfd3b8")

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
