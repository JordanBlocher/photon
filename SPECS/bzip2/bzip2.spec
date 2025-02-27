Summary:        Contains programs for compressing and decompressing files
Name:           bzip2
Version:        1.0.8
Release:        1%{?dist}
License:        BSD
URL:            http://www.bzip.org/
Group:          System Environment/Base
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://www.bzip.org/%{version}/%{name}-%{version}.tar.gz
Provides:       libbz2.so.1()(64bit)
%define sha1 bzip2=bf7badf7e248e0ecf465d33c2f5aeec774209227
Patch0:         http://www.linuxfromscratch.org/patches/lfs/7.2/bzip2-1.0.6-install_docs-1.patch
Requires:       bzip2-libs = %{version}-%{release}
Conflicts:      toybox

%description
The Bzip2 package contains programs for compressing and
decompressing files.  Compressing text files with bzip2 yields a much better
compression percentage than with the traditional gzip.

%package        devel
Summary:        Header and development files for bzip2
Requires:       bzip2
%description    devel
It contains the libraries and header files to create applications

%package libs
Summary:        Libraries for bzip2
Group:          System Environment/Libraries
%description    libs
This package contains minimal set of shared bzip2 libraries.

%prep
%setup -q
%patch0 -p1
sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile
sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile

%build
make VERBOSE=1 %{?_smp_mflags} -f Makefile-libbz2_so
make clean
make VERBOSE=1 %{?_smp_mflags}

%install
make PREFIX=%{buildroot}/usr install
install -vdm 0755 %{buildroot}/%{_lib}
install -vdm 0755 %{buildroot}/bin
cp -av libbz2.so* %{buildroot}/%{_lib}
install -vdm 755 %{buildroot}%{_libdir}
ln -sv libbz2.so.%{version} %{buildroot}%{_lib}/libbz2.so
ln -sv libbz2.so.%{version} %{buildroot}%{_lib}/libbz2.so.1
rm -v %{buildroot}%{_bindir}/{bunzip2,bzcat}
ln -sv bzip2 %{buildroot}/usr/bin/bunzip2
ln -sv bzip2 %{buildroot}/usr/bin/bzcat
find %{buildroot} -name '*.a'  -delete

%check
make %{?_smp_mflags} check

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/bzcat
%{_bindir}/bunzip2
%{_bindir}/bzless
%{_bindir}/bzgrep
%{_bindir}/bzip2
%{_bindir}/bzdiff
%{_bindir}/bzfgrep
%{_bindir}/bzcmp
%{_bindir}/bzip2recover
%{_bindir}/bzegrep
%{_bindir}/bzmore
%{_mandir}/man1/bzmore.1.gz
%{_mandir}/man1/bzfgrep.1.gz
%{_mandir}/man1/bzegrep.1.gz
%{_mandir}/man1/bzgrep.1.gz
%{_mandir}/man1/bzdiff.1.gz
%{_mandir}/man1/bzcmp.1.gz
%{_mandir}/man1/bzless.1.gz
%{_mandir}/man1/bzip2.1.gz

%files devel
%{_includedir}/bzlib.h
%{_libdir}/libbz2.so
%{_docdir}/*

%files libs
%{_lib}/libbz2.so.*

%changelog
*   Fri Oct 18 2019 Shreyas B <shreyasb@vmware.com> 1.0.8-1
-   Upgrade to 1.0.8.
-   Remove CVE-2016-3189.patch as the fix already available in the latest version.
*   Tue Oct 2 2018 Michelle Wang <michellew@vmware.com> 1.0.6-9
-   Add conflicts toybox.
*   Sun Jun 04 2017 Bo Gan <ganb@vmware.com> 1.0.6-8
-   Fix symlink.
*   Fri Apr 14 2017 Alexey Makhalov <amakhalov@vmware.com> 1.0.6-7
-   Added -libs subpackage.
*   Fri Oct 21 2016 Kumar Kaushik <kaushikk@vmware.com> 1.0.6-6
-   Fixing security bug CVE-2016-3189.
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.6-5
-   GA - Bump release of all rpms.
*   Tue Nov 10 2015 Mahmoud Bassiouny <mbassiouny@vmware.com> 1.0.6-4
-   Providing libbz2.so.1, miror fix for devel provides.
*   Fri Jun 5 2015 Divya Thaluru <dthaluru@vmware.com> 1.0.6-3
-   Adding bzip2 package run time required package for bzip2-devel package.
*   Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> 1.0.6-2
-   Update according to UsrMove.
*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 1.0.6-1
-   Initial build First version.
