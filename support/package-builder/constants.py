import platform
from Logger import Logger

class constants(object):
    specPath = ""
    sourcePath = ""
    rpmPath = ""
    logPath = ""
    logLevel = "info"
    topDirPath = ""
    buildRootPath = "/mnt"
    prevPublishRPMRepo = ""
    prevPublishXRPMRepo = ""
    pullsourcesURL = ""
    extrasourcesURLs = {}
    buildPatch = False
    inputRPMSPath = ""
    rpmCheck = False
    sourceRpmPath = ""
    publishBuildDependencies = False
    packageWeightsPath = None
    dockerUnixSocket = "/var/run/docker.sock"
    buildContainerImage = "photon_build_container:latest"
    userDefinedMacros = {}
    dist = None
    buildNumber = None
    releaseVersion = None
    katBuild = None
    testForceRPMS = []
    tmpDirPath = "/dev/shm"
    buildOptions = {}
    # will be extended later from listMakeCheckRPMPkgtoInstall
    listMakeCheckRPMPkgWithVersionstoInstall = None
    buildArch = platform.machine()
    targetArch = platform.machine()
    crossCompiling = False
    currentArch = buildArch

    noDepsPackageList = [
        "texinfo",
        "bzip2",
        "bzip2-libs",
        "gettext",
        "nspr",
        "bison",
        "go",
        "sqlite",
        "sqlite-devel",
        "sqlite-libs"]

    # These packages will be built in first order as build-core-toolchain stage
    listCoreToolChainPackages = [
        "filesystem",
        "linux-api-headers",
        "glibc",
        "zlib",
        "file",
        "binutils",
        "binutils-libs",
        "gmp",
        "mpfr",
        "mpc",
        "gcc",
        "pkg-config",
        "ncurses",
        "readline",
        "bash"]

    # These packages will be built in a second stage to replace publish RPMS
    listToolChainPackages = [
        "filesystem",
        "linux-api-headers",
        "glibc",
        "zlib",
        "file",
        "binutils",
        "binutils-libs",
        "gmp",
        "mpfr",
        "mpc",
        "gcc",
        "pkg-config",
        "ncurses",
        "bash",
        "bzip2",
        "sed",
        "procps-ng",
        "coreutils",
        "m4",
        "grep",
        "readline",
        "diffutils",
        "gawk",
        "findutils",
        "gettext",
        "gzip",
        "make",
        "patch",
        "util-linux",
        "tar",
        "xz",
        "libtool",
        "flex",
        "bison",
        "popt",
        "nspr",
        "nspr-devel",
        "sqlite",
        "nss",
        "elfutils",
        "expat",
        "libffi",
        "libpipeline",
        "gdbm",
        "perl",
        "texinfo",
        "autoconf",
        "automake",
        "openssl",
        "openssl-devel",
        "libdb",
        "rpm"]

    # List or RPMS that will be installed in a chroot prior to build each
    # package. This list should be ordered by install order. On a stage1
    # and stage2 published rpms will/might be used after stage2 only local
    # RPMS will be used
    listToolChainRPMsToInstall = [
        "filesystem",
        "linux-api-headers",
        "glibc",
        "glibc-devel",
        "glibc-iconv",
        "glibc-tools",
        "zlib",
        "zlib-devel",
        "file-libs",
        "file",
        "binutils",
        "binutils-libs",
        "binutils-devel",
        "gmp",
        "gmp-devel",
        "mpfr",
        "mpfr-devel",
        "mpc",
        "libgcc",
        "libgcc-devel",
        "libgcc-atomic",
        "libstdc++",
        "libstdc++-devel",
        "libgomp",
        "libgomp-devel",
        "gcc",
        "pkg-config",
        "ncurses",
        "ncurses-libs",
        "ncurses-devel",
        "bash",
        "bzip2",
        "bzip2-libs",
        "bzip2-devel",
        "sed",
        "procps-ng",
        "coreutils",
        "m4",
        "grep",
        "readline",
        "diffutils",
        "gawk",
        "findutils",
        "gettext",
        "gzip",
        "make",
        "patch",
        "util-linux",
        "util-linux-libs",
        "util-linux-devel",
        "tar",
        "xz",
        "xz-libs",
        "libtool",
        "flex",
        "flex-devel",
        "bison",
        "readline-devel",
        "popt",
        "popt-devel",
        "nspr",
        "nspr-devel",
        "sqlite",
        "sqlite-libs",
        "nss",
        "nss-libs",
        "nss-devel",
        "elfutils-libelf",
        "elfutils",
        "elfutils-libelf-devel",
        "elfutils-devel",
        "expat",
        "expat-libs",
        "libffi",
        "libpipeline",
        "gdbm",
        "perl",
        "texinfo",
        "autoconf",
        "automake",
        "openssl",
        "openssl-devel",
        "libcap",
        "libdb",
        "libdb-devel",
        "lua",
        "lua-devel",
        "rpm",
        "rpm-build",
        "rpm-devel",
        "rpm-libs",
        "cpio"]

    # List of RPMs which are not published. They will be created during the
    # build process
    listOfRPMsProvidedAfterBuild = [
        "util-linux-devel",
        "flex-devel",
        "nspr-devel",
        "glibc-iconv",
        "glibc-tools",
        "bzip2-libs",
        "expat-libs",
        "ncurses-libs",
        "util-linux-libs",
        "nss-libs",
        "xz-libs",
        "sqlite",
        "sqlite-libs",
        "file-libs",
        "rpm-libs"]

    # List of packages that will be installed in addition for each
    # package to make check
    listMakeCheckRPMPkgtoInstall = [
        "python2",
        "python2-devel",
        "python2-libs",
        "python2-tools",
        "PyYAML",
        "libyaml",
        "libffi",
        "python-setuptools",
        "python3-setuptools",
        "ca-certificates",
        "linux",
        "createrepo_c",
        "sudo",
        "ruby",
        "curl",
        "pcre-devel",
        "boost-devel",
        "which",
        "go",
        "e2fsprogs-devel",
        "shadow",
        "check",
        "libacl-devel",
        "device-mapper",
        "wget",
        "tar",
        "pkg-config",
        "git",
        "openssl",
        "openssl-devel",
        "net-tools",
        "less",
        "iana-etc",
        "libdb",
        "rpm-devel",
        "rpm",
        "libxml2",
        "python-xml",
        "python3-xml",
        "libacl",
        "tzdata",
        "libgcrypt-devel",
        "Linux-PAM",
        "unzip",
        "systemd-devel",
        "gnupg",
        "ncurses-terminfo"]

    # List of packages that requires privileged docker
    # to run make check.
    listReqPrivilegedDockerForTest = [
        "elfutils", # SYS_PTRACE
        "gdb",
        "glibc",
        "tar"]

    # List of Packages which causes "Makecheck" job
    # to stuck indefinately or getting failed.
    # Until these pkgs %check is fixed, these pkgs will be
    # skip to run makecheck.
    listMakeCheckPkgToSkip = [
        "gtk-doc",
        "libmspack",
        "socat"]

    # .spec file might contain lines such as
    # Requires(post):/sbin/useradd
    # Build system should interpret it as
    # Requires: shadow
    providedBy = {
        "/usr/sbin/useradd":"shadow",
        "/usr/sbin/userdel":"shadow",
        "/usr/sbin/groupadd":"shadow",
        "/sbin/service":"initscripts",
        "/usr/bin/which":"which",
        "/usr/bin/python":"python2",
        "/bin/python":"python2",
        "/bin/python2":"python2",
        "/bin/python3":"python3",
        "/bin/awk":"gawk",
        "/bin/gawk":"gawk",
        "/bin/sed":"sed",
        "/bin/grep":"grep",
        "/bin/sh":"bash",
        "/bin/bash":"bash",
        "/bin/zsh":"zsh",
        "/bin/tcsh":"tcsh",
        "/bin/csh":"csh",
        "/bin/perl":"perl",
        "/bin/mergerepo":"createrepo_c",
        "/bin/modifyrepo":"createrepo_c",
        "/bin/false":"coreutils",
        "/bin/ln":"coreutils",
        "/bin/chown":"coreutils",
        "/bin/cp":"coreutils",
        "/bin/rm":"coreutils",
        "/bin/mv":"coreutils"
    }

    @staticmethod
    def setSpecPath(specPath):
        constants.specPath = specPath

    @staticmethod
    def setSourcePath(sourcePath):
        constants.sourcePath = sourcePath

    @staticmethod
    def setRpmPath(rpmPath):
        constants.rpmPath = rpmPath

    @staticmethod
    def setSourceRpmPath(sourceRpmPath):
        constants.sourceRpmPath = sourceRpmPath

    @staticmethod
    def setTopDirPath(topDirPath):
        constants.topDirPath = topDirPath

    @staticmethod
    def setLogLevel(logLevel):
        constants.logLevel = logLevel

    @staticmethod
    def setLogPath(logPath):
        constants.logPath = logPath

    @staticmethod
    def setPrevPublishRPMRepo(prevPublishRPMRepo):
        constants.prevPublishRPMRepo = prevPublishRPMRepo

    @staticmethod
    def setPrevPublishXRPMRepo(prevPublishXRPMRepo):
        constants.prevPublishXRPMRepo = prevPublishXRPMRepo

    @staticmethod
    def setBuildRootPath(buildRootPath):
        constants.buildRootPath = buildRootPath

    @staticmethod
    def setPullSourcesURL(url):
        constants.pullsourcesURL = url

    @staticmethod
    def setExtraSourcesURLs(packageName, urls):
        constants.extrasourcesURLs[packageName] = urls

    @staticmethod
    def getPullSourcesURLs(packageName):
        urls=[]
        urls.append(constants.pullsourcesURL)
        if packageName in constants.extrasourcesURLs:
            urls.extend(constants.extrasourcesURLs[packageName])
        return urls

    @staticmethod
    def setInputRPMSPath(inputRPMSPath):
        constants.inputRPMSPath = inputRPMSPath

    @staticmethod
    def setRPMCheck(rpmCheck):
        constants.rpmCheck = rpmCheck

    @staticmethod
    def setRpmCheckStopOnError(rpmCheckStopOnError):
        constants.rpmCheckStopOnError = rpmCheckStopOnError

    @staticmethod
    def setPublishBuildDependencies(publishBuildDependencies):
        constants.publishBuildDependencies = publishBuildDependencies

    @staticmethod
    def setPackageWeightsPath(packageWeightsPath):
        constants.packageWeightsPath = packageWeightsPath

    @staticmethod
    def setDist(dist):
        constants.dist = dist

    @staticmethod
    def setBuildNumber(buildNumber):
        constants.buildNumber = buildNumber

    @staticmethod
    def setReleaseVersion(releaseVersion):
        constants.releaseVersion = releaseVersion

    @staticmethod
    def setKatBuild(katBuild):
        constants.katBuild = katBuild

    @staticmethod
    def initialize():
        if constants.rpmCheck:
            constants.testLogger = Logger.getLogger("MakeCheckTest",
                                                    constants.logPath, constants.logLevel)
            constants.addMacro("with_check", "1")
        else:
            constants.addMacro("with_check", "0")

        # adding distribution rpm macro
        if constants.dist is not None:
            constants.addMacro("dist", constants.dist)

        # adding buildnumber rpm macro
        if constants.buildNumber is not None:
            constants.addMacro("photon_build_number", constants.buildNumber)

        # adding releasenumber rpm macro
        if constants.releaseVersion is not None:
            constants.addMacro("photon_release_version", constants.releaseVersion)

        if constants.katBuild is not None:
            constants.addMacro("kat_build", constants.katBuild)

    @staticmethod
    def setTestForceRPMS(listsPackages):
        constants.testForceRPMS = listsPackages

    @staticmethod
    def addMacro(macroName, macroValue):
        constants.userDefinedMacros[macroName] = macroValue

    @staticmethod
    def setBuildOptions(options):
        constants.buildOptions = options

    @staticmethod
    def getAdditionalMacros(package):
        macros = {}
        if package in constants.buildOptions.keys():
            pkg = constants.buildOptions[package]
            for m in pkg["macros"]:
                k, v = m.split(' ', 1)
                macros[k] = v
        return macros
