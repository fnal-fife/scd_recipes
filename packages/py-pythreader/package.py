# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPythreader(PythonPackage):
    """ A set of useful tools built on top of standard Python threading module """

    homepage = "https://github.com/imandr/pythreader"
    pypi = "pythreader/pythreader-2.8.4.tar.gz"

    maintainers = ["marcmengel","imandr"]

    version("2.15.0", sha256="acf59f8ff2419272a39603b76770b653fe64538ee99b57f0b57ef609ed1cf0f0") 
    version("2.8.4", sha256="10dc326931443877e55cfa712a9532f504bd3126bb8863d51b68b900b210b317")
    version("2.8.2", sha256="2396de70d20518f1a64f75516a6d429989787823cc735ef401da8394f4b20c36")
    version("2.8.0", sha256="aa4f1ef297dbb1f49a2c005eaa8420e416eba940b20c3103dbe0f81b5798ff52")

    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type="build")
