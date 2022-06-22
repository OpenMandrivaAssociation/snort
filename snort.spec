%define oname snort3

Summary:        An Intrusion Detection System (IDS)
Name:           snort
Version:        3.1.32.0
Release:        1
License:        GPLv2+
Group:          Networking/Other
Url:            http://www.snort.org/
Source0:        https://github.com/snort3/snort3/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz
#Source1:        http://www.snort.org/dl/current/%{name}-%{version}.tar.gz.
Source3:        snort.service
Source4:        snort.logrotate
Source5:        snort.sysconfig
Source6:        snortdb-extra
Source7:        snort-wrapper.sh
Source100:	%{name}.rpmlintrc
#Patch0:         snort-lib64.diff
# (oe) http://www.inliniac.net/files/
#Patch2:         snort-2.9.7.6-plugins_fix.diff
BuildRequires:  cmake
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  latex2html
BuildRequires:  texinfo
BuildRequires:  daq-devel
BuildRequires:  dnet-devel
BuildRequires:  mysql-devel
BuildRequires:  net1.0.2-devel
BuildRequires:  pcap-devel
BuildRequires:  postgresql-devel
BuildRequires:  pkgconfig(libfl)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libipq)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libprelude)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xtables)
BuildRequires:  pkgconfig(zlib)
Requires(post,preun,pre,postun):        rpm-helper
Requires(preun,post):   snort-rules
Requires:       pcre
Requires:       pcap
Requires:       snort-rules
Suggests:       snortsam

%description
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

This rpm is different from previous rpms and while it will not clobber
your current snort file, you will need to modify it.

There are 9 different packages available

All of them require the base snort rpm.  Additionally, you will need
to chose a binary to install.

%{_sbindir}/snort should end up being a symlink to a binary in one of
the following configurations. We use update-alternatives for this.
Here are the different packages along with their priorities.

plain(10)               plain+flexresp(11)              mysql(12)
mysql+flexresp(13)      postgresql(14)                  postgresql+flexresp(15)
bloat(16)               inline(17)                      inline+flexresp(18)
prelude(19)             prelude+flexresp(20)

Please see the documentation in %{_docdir}/%{name}

%package plain+flexresp
Summary:        Snort with Flexible Response
Group:          Networking/Other
Requires:       snort >= %{version}-%{release}

%description plain+flexresp
Snort compiled with flexresp support. FlexResp allows snort to actively close
offending connections.

%package mysql
Summary:        Snort with MySQL database support
Group:          Networking/Other
Requires:       snort >= %{version}-%{release}

%description mysql
Snort compiled with mysql support.

%package mysql+flexresp
Summary:        Snort with MySQL database and Flexible Response support
Group:          Networking/Other
Requires:       snort >= %{version}-%{release}

%description mysql+flexresp
Snort compiled with mysql+flexresp support. FlexResp allows snort to actively
close offending connections.

%package postgresql
Summary:        Snort with PostgreSQL database support
Group:          Networking/Other
Requires:       snort >= %{version}-%{release}

%description    postgresql
Snort compiled with postgresql support.

%package postgresql+flexresp
Summary:        Snort with PostgreSQL database and Flexible Response support
Group:          Networking/Other
Requires:       snort >= %{version}-%{release}

%description postgresql+flexresp
Snort compiled with postgresql+flexresp support. FlexResp allows snort to
actively close offending connections.

%package bloat
Summary:        Snort with flexresp+mysql+postgresql+inline+prelude support
Group:          Networking/Other
Requires:       snort >= %{version}-%{release}

%description    bloat
Snort compiled with flexresp+mysql+postgresql+inline+prelude support.

%package inline
Summary:        Snort with Inline support
Group:          Networking/Other
Requires:       iptables
Requires:       snort >= %{version}-%{release}

%description inline
Snort compiled with inline support. Snort-Inline takes packets from iptables
instead of libpcap. It then uses new rule types to help iptables make pass or
drop decisions based on snort rules.  

%package inline+flexresp
Summary:        Snort with Inline and Flexible Response support
Group:          Networking/Other
Requires:       iptables
Requires:       snort >= %{version}-%{release}

%description inline+flexresp
Snort compiled with inline+flexresp support. FlexResp allows snort to actively
close offending connections. Snort-Inline takes packets from iptables instead
of libpcap. It then uses new rule types to help iptables make pass or drop
decisions based on snort rules.  

%package prelude
Summary:        Snort with Prelude support
Group:          Networking/Other
Requires:       snort >= %{version}-%{release}

%description prelude
Snort compiled with prelude support.

%package prelude+flexresp
Summary:        Snort with Prelude and Flexible Response support
Group:          Networking/Other
Requires:       snort >= %{version}-%{release}

%description prelude+flexresp
Snort compiled with prelude+flexresp support. FlexResp allows snort to actively
close offending connections.

%package devel
Summary:        Snort development files
Group:          Networking/Other
Requires:       snort = %{version}-%{release}

%description devel
This package includes the development files for %{name}.

%prep
%setup -q -n %{oname}-%{version}
#patch0 -p0 -b .lib64
#patch2 -p1 -b .plugins_fix

# fix pid file path
/bin/echo "#define _PATH_VARRUN \"%{_var}/run/%{name}\"" >> acconfig.h

cp -a %{SOURCE6} .

%build
%cmake

%make_build


%install
%make_install -C build

%pre
%_pre_useradd snort /var/log/snort /bin/false

%post
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-plain 10
%systemd_post snort

%preun
%systemd_preun snort

%postun
%_postun_userdel snort
# remove the link if not upgrade
if [ $1 = 0 ]; then
    %{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-plain
fi

%post plain+flexresp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-plain+flexresp 11

%postun plain+flexresp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-plain+flexresp

%post mysql
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-mysql 12

%postun mysql
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-mysql

%post mysql+flexresp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-mysql+flexresp 13

%postun mysql+flexresp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-mysql+flexresp

%post postgresql
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-postgresql 14

%postun postgresql
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-postgresql

%post postgresql+flexresp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-postgresql+flexresp 15

%postun postgresql+flexresp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-postgresql+flexresp

%post bloat
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-bloat 16

%postun bloat
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-bloat

%post inline
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-inline 17

%postun inline
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-inline

%post inline+flexresp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-inline+flexresp 18

%postun inline+flexresp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-inline+flexresp

%post prelude
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-prelude 19

%postun prelude
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-prelude

%post prelude+flexresp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-prelude+flexresp 20

%postun prelude+flexresp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-prelude+flexresp

%files
#{_sbindir}/%{name}-plain
%{_bindir}/u2boat
%{_bindir}/u2spewfoo
#{_mandir}/man8/%{name}.8*

%files plain+flexresp
#{_sbindir}/%{name}-plain+flexresp

%files mysql
#%doc schemas/create_mysql
#{_sbindir}/%{name}-mysql

%files mysql+flexresp
#%doc schemas/create_mysql
#{_sbindir}/%{name}-mysql+flexresp

%files postgresql
#%doc schemas/create_postgresql
#{_sbindir}/%{name}-postgresql

%files postgresql+flexresp
#%doc schemas/create_postgresql
#{_sbindir}/%{name}-postgresql+flexresp

%files bloat
#{_sbindir}/%{name}-bloat

%files inline
#{_sbindir}/%{name}-inline

%files inline+flexresp
#{_sbindir}/%{name}-inline+flexresp

%files prelude
#{_sbindir}/%{name}-prelude

%files prelude+flexresp
#{_sbindir}/%{name}-prelude+flexresp

%files devel
#dir %{_libdir}/pkgconfig
#{_libdir}/pkgconfig/snort_output.pc
#{_libdir}/pkgconfig/snort.pc
#{_libdir}/pkgconfig/snort_preproc.pc
#dir %{_includedir}/%{name}/dynamic_preproc
#dir %{_includedir}/%{name}/dynamic_output/*.h
#{_includedir}/%{name}/dynamic_preproc/*.h

