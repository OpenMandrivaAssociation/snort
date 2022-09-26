%define oname snort3

Summary:        An Intrusion Detection System (IDS)
Name:           snort
Version:        3.1.42.0
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


%files
%doc %{_datadir}/doc/snort
%{_bindir}/snort
%{_bindir}/snort2lua
%{_bindir}/u2boat
%{_bindir}/u2spewfoo
%{_bindir}/appid_detector_builder.sh
%{_prefix}/etc/snort


%files devel
%{_includedir}/snort
%{_libdir}/pkgconfig/snort.pc
%{_libdir}/snort/daq
