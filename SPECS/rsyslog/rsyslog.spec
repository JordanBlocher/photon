Summary:        Rocket-fast system for log processing
Name:           rsyslog
Version:        8.1910.0
Release:        2%{?dist}
License:        GPLv3+ and ASL 2.0
URL:            http://www.rsyslog.com/
Source0:        http://www.rsyslog.com/files/download/rsyslog/%{name}-%{version}.tar.gz
%define sha1    rsyslog=ac36de817e69450d88e4a2b822f9d69f3fbcf0f4
Source1:        rsyslog.service
Source2:        50-rsyslog-journald.conf
Source3:        rsyslog.conf
Patch0:         fix_openssl_version_1910.patch
Group:          System Environment/Base
Vendor:         VMware, Inc.
Distribution:   Photon
BuildRequires:  systemd-devel
BuildRequires:  libestr-devel
BuildRequires:  libfastjson-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  liblogging-devel
BuildRequires:  librelp-devel
BuildRequires:  autogen
BuildRequires:  gnutls-devel
BuildRequires:  curl-devel
Requires:       gnutls
Requires:       systemd
Requires:       libestr
Requires:       libfastjson
Requires:       libgcrypt
Requires:       liblogging
Requires:       librelp
%description
RSYSLOG is the rocket-fast system for log processing.
It offers high-performance, great security features and a modular design. While it started as a regular syslogd, rsyslog has evolved into a kind of swiss army knife of logging, being able to accept inputs from a wide variety of sources, transform them, and output to the results to diverse destinations.
%prep
%setup -q

%patch0 -p1

autoreconf -fvi
%build
sed -i 's/libsystemd-journal/libsystemd/' configure
%configure \
    --enable-relp \
    --enable-gnutls\
    --enable-imfile \
    --enable-imjournal \
    --enable-impstats \
    --enable-imptcp \
    --enable-imtcp \
    --enable-openssl

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -vd %{buildroot}%{_libdir}/systemd/system/
install -vd %{buildroot}%{_sysconfdir}/systemd/journald.conf.d/
rm -f %{buildroot}/lib/systemd/system/rsyslog.service
install -p -m 644 %{SOURCE1} %{buildroot}%{_libdir}/systemd/system/
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/systemd/journald.conf.d/
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/rsyslog.conf
find %{buildroot} -name '*.la' -delete

%check
make %{?_smp_mflags} check

%post
/sbin/ldconfig
%systemd_post rsyslog.service

%preun
%systemd_preun rsyslog.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart rsyslog.service

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_libdir}/rsyslog/*.so
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_libdir}/systemd/system/rsyslog.service
%{_sysconfdir}/systemd/journald.conf.d/*
%{_sysconfdir}/rsyslog.conf
%changelog
*   Mon Nov 04 2019 Tapas Kundu <tkundu@vmware.com> 8.1910.0-2
-   Built with imtcp and openssl
-   Added patch to fix openssl version in rsyslog source
*   Wed Oct 16 2019 Tapas Kundu <tkundu@vmware.com> 8.1910.0-1
-   Update to 8.1910.0 release
-   Fix CVE-2019-17041 and CVE-2019-17042
*   Fri Oct 04 2019 Keerthana K <keerthanak@vmware.com> 8.1907.0-1
-   Update to 8.1907.0
-   Fix CVE-2019-17040
*   Mon Sep 10 2018 Keerthana K <keerthanak@vmware.com> 8.37.0-1
-   Updated to version 8.37.0
*   Thu Apr 12 2018 Xiaolin Li <xiaolinl@vmware.com> 8.26.0-5
-   Add $IncludeConfig /etc/rsyslog.d/ to rsyslog.conf
*   Fri Dec 15 2017 Anish Swaminathan <anishs@vmware.com>  8.26.0-4
-   Remove kill SIGHUP from service file
*   Mon Nov 13 2017 Xiaolin Li <xiaolinl@vmware.com> 8.26.0-3
-   Add a default rsyslog.conf.
*   Tue Aug 15 2017 Dheeraj Shetty <dheerajs@vmware.com>  8.26.0-2
-   Fix CVE-2017-12588
*   Mon  Apr 24 2017 Siju Maliakkal <smaliakkal@vmware.com>  8.26.0-1
-   Update to latest
*   Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  8.15.0-7
-   Change systemd dependency
*   Wed Oct 05 2016 ChangLee <changlee@vmware.com> 8.15.0-6
-   Modified %check
*   Thu May 26 2016 Divya Thaluru <dthaluru@vmware.com>  8.15.0-5
-   Fixed logic to restart the active services after upgrade
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 8.15.0-4
-   GA - Bump release of all rpms
*   Wed May 4 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com>  8.15.0-3
-   Use systemd macros for post, preun and postun to respect upgrades
*   Wed Feb 17 2016 Anish Swaminathan <anishs@vmware.com>  8.15.0-2
-   Add journald conf and new service file.
*   Mon Jan 11  2016 Xiaolin Li <xiaolinl@vmware.com> 8.15.0-1
-   Update rsyslog to 8.15.0
*   Wed Jun 17 2015 Divya Thaluru <dthaluru@vmware.com> 8.10.0-1
-   Initial build. First version

