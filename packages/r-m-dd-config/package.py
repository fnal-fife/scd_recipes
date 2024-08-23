# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os
import sys
import glob

explist = [
            "hypot",
            "annie",
            "dune",
            "gm2",
            "icarus",
            "lariat",
            "minerva",
            "mu2e",
            "nova",
            "sbn",
            "sbnd",
            "uboone",
        ]
try:
    import grp
    gname = grp.getgrgid(os.getegid()).gr_name
except:
    gname = None

if os.environ.get("GROUP",None) in explist:
    defexp = os.environ.get("GROUP")
elif os.environ.get("EXPERIMENT",None) in explist:
    defexp = os.environ.get("EXPERIMENT")
elif gname in explist:
    defexp = gname
else:
    defexp = "hypot"

class RMDdConfig(BundlePackage):
    """Config for rucio-clients, metacat and data-dispatcher"""

    homepage = "https://fifewiki.fnal.gov/"

    maintainers = ["marcmengel"]

    version("1.0")
    version("1.1")

    depends_on("data-dispatcher")
    depends_on("rucio-clients")
    depends_on("metacat")

    variant("experiment", values=explist, default=defexp)
    
    variant("lab", values= ["fnal.gov"], default="fnal.gov")

    def get_rdict(self):
        ''' 
            Return a dictionary of handy values to substitute into 
            path/url template strings
        '''
        rdict = { 
            "exp": self.spec.variants["experiment"].value,
            "lab": self.spec.variants["lab"].value,
            "msuf": "_meta_prod/app",
            "dsuf": "_dd_prod/data",
            "asuf": "",
            "acct": os.environ.get("GRID_USER", os.environ.get("USER","unk"))
        }
        # irregularities...
        # can set "acct" per experiment here too if needed...
        if rdict["exp"] == "hypot":
            rdict["msuf"] = "_meta_dev/app"
            rdict["dsuf"] = "_dd/data"
            rdict["asuf"] = "_dev"

        if rdict["exp"] == "dune":
            rdict["msuf"] = "_meta_prod/app"
            rdict["dsuf"] = "/dd/data"
        
        return rdict


    def setup_run_environment(self, env):
        '''
           Compute urls and locations for this experiment
           and set appropriate environment variables.
           Also make a per-experiment rucio.cfg for the user if needed

           Uses the rdict generated above with %{name}s format strings
        '''
        rdict = self.get_rdict()
        ddurl = "https://metacat.%(lab)s:9443/%(exp)s%(dsuf)s" % rdict
        msurl = "https://metacat.%(lab)s:9443/%(exp)s%(msuf)s" % rdict
        authurl = "https://metacat.%(lab)s:8143/auth/%(exp)s%(asuf)s" % rdict
        # mu2e is configured on the whole set now, no longer need to 
        # limit it to dbweb5...
        # if rdict["exp"] == "mu2e":
        #    msurl = ( msurl
        #                .replace("https://metacat", "http://dbweb5")
        #                .replace(":9443",":9094")
        #            )

        configbase=os.environ.get(
             "XDG_CONFIG_HOME", 
             os.path.join(os.environ.get("HOME","."),".config"),
        )
        rucio_home = os.path.join(configbase, "rucio", rdict["exp"])

        # use system gfal2 python bits if present
        gl = glob.glob("/usr/lib*/python3*/site-packages")
        if gl and os.path.exists(gl[0] + '/gfal2.so'):
            env.append_path("PYTHONPATH",gl[0])

        env.set( "RUCIO_HOME", rucio_home)
        env.set( "DATA_DISPATCHER_URL", ddurl )
        env.set( "METACAT_SERVER_URL", msurl )
        env.set( "DATA_DISPATCHER_AUTH_URL", authurl)
        env.set( "METACAT_AUTH_SERVER_URL", authurl)

        # now make sure we have a rucio.cfg for this setup
        # if there is one, just leave it alone

        rucio_cfg =  os.path.join(rucio_home, "etc", "rucio.cfg")

        if not os.path.exists(rucio_cfg):
            os.makedirs(os.path.dirname(rucio_cfg))
            with open( rucio_cfg, "w") as rcf:
                rcf.write("""
[client]
rucio_host = https://%(exp)s-rucio.%(lab)s
auth_host = https://%(exp)s-rucio.%(lab)s

ca_cert = /etc/grid-security/certificates
account = %(acct)s
auth_type = x509_proxy
request_retries = 3
"""     % rdict)
