# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
import os
import glob


class RucioClients(PythonPackage):
    """Client interface to Rucio."""

    homepage = "https://rucio.cern.ch"
    pypi = "rucio_clients/rucio_clients-1.30.0.tar.gz"

    # maintainers = ["marcmengel","bari12"]

    version("38.3.0", sha256="49f8809b5378d1c9e9edc5f1a74fbf7eebe45db27084945f748b2c73a841efed")
    version("38.2.0", sha256="7495d7274e17e4099f9ccd2672667236e17f806292954387145e99c7c688414a")
    version("37.0.0", sha256="c37a0570c54574f06926679967031e9fc418e18c51094631890b83ed4007554c")
    version("36.5.0", sha256="6e6090c112eed772449ac2741ce08f533ea20add4ece8d6dbdd87842d18d2079")
    version("36.4.0", sha256="3a85092e08a4bc17ac23803d390b34471166521fa48f5735b7f1c4560f4743bc")
    version("35.6.1", sha256="3a07c5791e6248fb1867b097e5b1c6376e5bf89c03a06b8807905ceeccac57c1")
    version("35.4.1", sha256="d87405785776d7522100cda2ebc16892f94cda94d3c257896ee4817c4e03c06b")
    version("35.2.1", sha256="244b2219e4e8e3bc77a347536350ffe3e82be4e8647e8f90df48d233059b5fc5")
    version("34.4.3", sha256="f3fa99f647e5efa7b81167d148254b6ca45bd5fc636f70f78711c10c66c083a1")
    version("33.3.0", sha256="08c32a046ae7695f5785e712f7208633656e451b312eb518fd4a5b9c9736dd67")
    version("33.2.0", sha256="307480b57feefe827e1fdab64daf1a95fea2f3b3ea1f12913a1d331af695f76f")
    version("32.4.0", sha256="847f8db44f6f7f2c53cfb596afcefefd310c5791d5fbee86bc487d904c130801")
    version("1.31.7", sha256="99f7c981a9aff726f7fbbc0774b53d9df15d6a33798afb14ea0b4b3acaeadc53")
    version("1.29.12", sha256="4b3e11726e75f89a04b513be16a53e5b9f7d33023ae8f0b7aa9032a2a1b8ae75")

    def url_for_version(self, version):
        urlf = "https://files.pythonhosted.org/packages/source/r/rucio-clients/rucio-clients-{0}.tar.gz"
        # sometimes they upload it as rucio_clients vs rucio-clients...
        if str(version) in ["34.4.1", "34.4.2", "34.4.3"]:
            urlf = urlf.replace("rucio-clients", "rucio_clients")
        return urlf.format(version)

    variant("gfal2", default=False)

    depends_on("py-setuptools", type=("build"))
    depends_on("py-pip", type="build")

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-urllib3", type=("build", "run"))
    depends_on("py-dogpile-cache", type=("build", "run"))
    depends_on("py-tabulate", type=("build", "run"))
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-paramiko", type=("build", "run"))
    depends_on("py-kerberos", type=("build", "run"))
    depends_on("py-requests-kerberos", type=("build", "run"))
    depends_on("py-python-swiftclient", type=("build", "run"))
    depends_on("py-argcomplete", type=("build", "run"))
    depends_on("py-python-magic", type=("build", "run"))
    depends_on("gfal2-python", type=("build", "run"), when="+gfal2")
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"), when="@36:")
    depends_on("py-rich", type=("build", "run"), when="@36:")
    depends_on("py-click", type=("build", "run"), when="@37:")

    #
    # if we're not building a Spack gfal2, try to put a symlink to the
    # system one in our site-packages directory.
    #
    with when("-gfal2"):

        @run_after("install")
        def add_system_gfal_link(self):
            if not os.path.exists("/usr/bin/python3"):
                return

            incantation = """ /usr/bin/python3 -E -c "import sys,os; print([x for x in sys.path if os.path.exists(os.path.join(x,'gfal2.so'))>0][0])" """

            with os.popen(incantation) as fd:
                src = fd.read().strip()

            try:
                wc = "/lib*/python*/site-packages"
                dst = glob.glob(self.prefix + wc)[0]
            except:
                return

            if os.path.exists(src) and os.path.exists(dst):
                os.symlink(os.path.join(src, "gfal2.so"), os.path.join(dst, "gfal2.so"))
