# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Htcondor(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://htcondor.org/"
    url = "https://github.com/htcondor/htcondor/archive/refs/tags/V9_11_0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = [ "marcmengel" ]

    version( "main", git="https://github.com/marcmengel/htcondor.git", branch="main")
    version( "9.0.16", sha256="c505c3e72c8dd7d6b30f7f7922ccdd20627b6dcf385b40b17c3022973d2852eb", preferred=True)
    version( "9.11.0", sha256="5309121ad9d0da42f77211456854bfad97bcb94a0ee001d18db04f8b61e48695")
    version( "9.10.1", sha256="12bfec4b00cb148afbdc8bd63695507d0cc29d8b76696346adca48c04fa7e2c9")
    version( "9.10.0", sha256="02d3f2d70ace2d40e7cde813b0bea24baa92bc4be6cb0b62bfc7168d24fb0117")
    version( "9.9.1", sha256="fc58aa48c3b35d9ce54535946dc52a0d3232c728090c79209359d4b8e2171ae0")
    version( "9.9.0", sha256="bf958c0687cc9c9fd524cd19f8014eb03e0d2949c9b8da3fe93b4bd25f16a741")
    version( "9.8.1", sha256="9e51983043639661a09e0a6df9fdec47b568b55d6724ae0522ee096582420fea")


    def url_for_version(self, version):
        urlf = "https://github.com/htcondor/htcondor/archive/refs/tags/V{0}.tar.gz"
        return urlf.format(version.underscored)

    depends_on("autoconf@2.59:", type="build")
    depends_on("boost +python+thread+pic+system", type=("build", "run"))
    depends_on("cmake@2.8.3:", type="build")
    depends_on("globus-toolkit", type=("build", "run"))
    depends_on("krb5", type=("build", "run"))
    depends_on("munge", type=("build", "run"))
    depends_on("openldap", type=("build", "run"))
    depends_on("sqlite", type=("build", "run"))
    depends_on("openssl", type=("build", "run"))
    depends_on("scitokens-cpp", type=("build", "run"))
    depends_on("tar@1.14:", type=("build", "run"))
    depends_on("voms", type=("build", "run"))
    depends_on("wget@1.9.1:", type=("build", "run"))
    # other things in their 'externals' bundle:
    # depends_on('blahp', type=('build','run'))
    # depends_on('cream', type=('build','run'))
    # depends_on('hadoop', type=('build','run'))
    # depends_on('libvirt', type=('build','run'))
    # depends_on('boinc', type=('build','run'))
    # depends_on('curl', type=('build','run'))
    # depends_on('libxml2', type=('build','run'))
    # depends_on('pcre', type=('build','run'))
    # depends_on('unicoregahp', type=('build','run'))
    # depends_on('libcgroup', type=('build','run'))
    # depends_on('qpid', type=('build','run'))

    def flag_handler(self, name, flags):
        # their CMakefiles dont findpackage various dependencies, so...
        plist = [
            "boost",
            "openldap",
            "globus-toolkit",
            "munge",
            "voms",
            "scitokens-cpp",
            "sqlite",
        ]
        if name in ["cflags", "cxxflags", "cppflags"]:
            # find our package headers
            for pkg in plist:
                flags.append("-I{0}".format(self.spec[pkg].prefix.include))
            # silliness for condor_types.h(?), things that ought to have configured
            flags.append("-DHAVE_LONG")
            flags.append("-DSIZEOF_LONG=8")
            flags.append("-DHAVE_STRCASESTR")
            return (flags, None, None)
        if name == "ldflags":
            for pkg in plist:
                flags.append("-L{0}".format(self.spec[pkg].prefix.lib))
            flags.append("-L/usr/lib64")
            if "-L/usr/lib" in flags:
                flags.remove("-L/usr/lib")
            return (flags, None, None)
        return (flags, None, None)

    def cmake_args(self):
        pyver = self.spec["python"].version
        pymajor = pyver.version[0]
        pyminor = pyver.version[1]
        args = [
            "-DCMAKE_INSTALL_PREFIX:PATH={0}".format(self.prefix),
            "-D_DEBUG:BOOL=TRUE",
            "-D_BUILDID:STRING=spack_hash_{0}".format(self.spec.dag_hash()),
            "-DBOOST_INCLUDE={0}".format(self.spec["boost"].prefix.include),
            "-DBOOST_LD={0}".format(self.spec["boost"].prefix.lib),
            "-DBOOST_VER=boost-{0}".format(self.spec["boost"].version),
            "-DWITH_PYTHON_BINDINGS:BOOL=TRUE",
            "-DPYTHON_EXECUTABLE:FILEPATH={0}/bin/python3".format(
                self.spec["python"].prefix
            ),
            "-DPYTHON3_EXECUTABLE:FILEPATH={0}/bin/python3".format(
                self.spec["python"].prefix
            ),
            "-DPYTHON_VERSION_STRING:STRING={0}".format(pyver),
            "-DPYTHON_VERSION_MAJOR:STRING={0}".format(pymajor),
            "-DPYTHON_VERSION_MINOR:STRING={0}".format(pyminor),
            "-DPYTHON3_VERSION_MAJOR:STRING={0}".format(pymajor),
            "-DPYTHON3_VERSION_MINOR:STRING={0}".format(pyminor),
            "-DPYTHON_BOOST_LIBRARY=boost_python{0}{1} -L{2}".format(
                pymajor, pyminor, self.spec["python"].prefix.lib
            ),
            "-DSQLITE3_LIB={0}".format(self.spec["sqlite"].libs[0]),
            "-DHAVE_SQLITE3_H={0}".format(self.spec["sqlite"].prefix.include+'/sqlite3.h'),
        ]
        return args

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path("PATH", self.prefix.bin)
        run_env.prepend_path("PYTHONPATH", self.prefix.lib.python3)
