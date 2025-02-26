# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class PomsJobsubWrapper(Package):
    """python / command line package for POMS clients"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/poms-client/wiki"
    url = "https://github.com/fermitools/poms/archive/refs/tags/v4_4_2.tar.gz"

    version("4.5.1", sha256="142b2b5bb8cce8325834f54ed52b65db1619980528a003c98e81c053a13dc051")
    version("4.5.0", sha256="7e7ccad6d22aa48e38f9854823c407d68d68d22f41bdb6eae9cd7fda4bc83ec2")

    def url_for_version(self, version):
        print("in poms-jobsub-wrapper url_for_version:", str(version))
        url = "https://github.com/fermitools/poms/archive/refs/tags/wrapper_v{0}.tar.gz"
        return url.format(version.underscored)

    depends_on("python", type=("build", "run"))
    depends_on("py-requests", type="run")
    depends_on("poms-client", type="run")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/poms_jobsub_wrapper/bin/poms_job_info", prefix.bin)

    def setup_run_environment(self, env):
        env.prepend_path("JOBSUB_EXTRA_JOB_INFO", "{0}/bin/poms_job_info".format(self.spec.prefix))

        env.prepend_path("JOBSUB_EXTRA_LINES", "+FIFE_CATEGORIES='POMS_TASK_ID_{0};POMS_CAMPAIGN_ID_{1};{2}'".format(os.environ.get("POMS_TASK_ID", ""), os.environ.get("POMS_CAMPAIGN_ID", ""), os.environ.get("POMS_CAMPAIGN_TAGS", "")))
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS_TASK_ID={0}".format(os.environ.get("POMS_TASK_ID", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS_CAMPAIGN_ID={0}".format(os.environ.get("POMS_CAMPAIGN_ID", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS_LAUNCHER={0}".format(os.environ.get("POMS_LAUNCHER", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS_CAMPAIGN_NAME='{0}'".format(os.environ.get("POMS_CAMPAIGN_NAME", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_STAGE_ID={0}".format(os.environ.get("POMS4_CAMPAIGN_STAGE_ID", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_STAGE_NAME='{0}'".format(os.environ.get("POMS4_CAMPAIGN_STAGE_NAME", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_ID={0}".format(os.environ.get("POMS4_CAMPAIGN_ID", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_NAME='{0}'".format(os.environ.get("POMS4_CAMPAIGN_NAME", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_SUBMISSION_ID={0}".format(os.environ.get("POMS4_SUBMISSION_ID", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_CAMPAIGN_TYPE='{0}'".format(os.environ.get("POMS4_CAMPAIGN_TYPE", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_LINES", "+POMS4_TEST_LAUNCH={0}".format(os.environ.get("POMS4_TEST_LAUNCH", "")), ",")
        env.prepend_path("JOBSUB_EXTRA_ENVIRONMENT", "POMS_CAMPAIGN_ID", ",")
        env.prepend_path("JOBSUB_EXTRA_ENVIRONMENT", "POMS_TASK_ID", ",")
