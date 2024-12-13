# fake recipe from ups_to_spack
from spack.package import *
import os

class Encp(Package):
    pass

    version("3.11c", sha256="c7614efe8c2279f02ee22d268f8a49213e0b2d12080d076d99785b753e19139d")


    variant("ups_to_spack", default=False)

    with when("+ups_to_spack"):
        def url_for_version(self, version):

            url = 'file:///tmp/empty.tar'
            return url


    with when("+ups_to_spack"):
        def install(self, spec, prefix):
            pkgprd = ""
            if ("cflags" in self.spec.compiler_flags and
                    len(self.spec.compiler_flags["cflags"])):
                pkgprd=self.spec.compiler_flags["cflags"][0]
                loc = pkgprd.find("UPS_PROD_DIR=")
                if loc > 0:
                    pkgprd=pkgprd[loc+13:]

            if not pkgprd:
                raise LookupError("variant +ups_to_spack needs cflags=-DUPS_PROD_DIR=/path")

            if os.path.isdir(pkgprd):
                os.system("cd {0} && find . -print | cpio -dumpv {1}".format(pkgprd, prefix))
            else:
                # UPS packages can be empty, spack wants *something* there...
                os.system("echo Converted empty UPS package > {0}/README".format(prefix))
            os.system("cd {0} && ln -s . /Linux64bit-2-6-2-12".format(prefix))
        
