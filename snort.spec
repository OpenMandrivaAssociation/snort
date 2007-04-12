%bcond_with snmp
%bcond_with clamav

Summary:        An Intrusion Detection System (IDS)
Name:           snort
Version:        2.6.1.3
Release:        %mkrel 2
License:        GPL
Group:          Networking/Other
URL:            http://www.snort.org/
Source0:        http://www.snort.org/dl/current/%{name}-%{version}.tar.gz
Source1:        http://www.snort.org/dl/current/%{name}-%{version}.tar.gz.sig
Source2:        http://www.snort.org/dl/current/%{name}-%{version}.tar.gz.md5
Source3:        snort.init
Source4:        snort.logrotate
Source5:        snort.sysconfig
Source6:        snortdb-extra
# OE: SNMP support originates from:
# http://www.cysols.com/contrib/snortsnmp/index.html
# http://www.cysol.co.jp/contrib/snortsnmp/SnortSnmpMod-2.2.0-01.tgz
Patch0:         snort-2.6.0-SNMP.diff
Patch1:         snort-2.6.0-lib64.diff
# OE: clamav support originates from:
# http://sourceforge.net/tracker/download.php?group_id=78497&atid=553469&file_id=131549&aid=1184861
# http://www.inliniac.net/blog/
# http://www.bleedingsnort.com/cgi-bin/viewcvs.cgi/*checkout*/snort-clamav/snort-2.6.0.2-clamav.diff?rev=1.4&root=Snort-Clamav
Patch2:         snort-2.6.1.3-clamav.diff
# (oe): make -L work as stated in the man page.
Patch3:         snort-2.3.0-no_timestamp.diff
# (oe) disable some code to make it build
Patch4:         snort-2.3.0-net-snmp_fix.diff
# (oe) http://www.snortsam.net/files/snort-plugin/snortsam-patch.tar.gz
Patch5:         snort-2.6.0-snortsam.diff
Patch7:         snort-2.6.1-plugins_fix.patch
Requires(post): rpm-helper snort-rules
Requires(preun): rpm-helper snort-rules
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:       pcre
Requires:       libpcap >= 0.6
Requires:       snort-rules
BuildRequires:  autoconf
BuildRequires:  automake1.7
BuildRequires:  libpcap-devel >= 0.6
%if %with snmp
BuildRequires:  net-snmp-devel
%endif
BuildRequires:  MySQL-devel >= 5.0
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel
BuildRequires:  texinfo
BuildRequires:  zlib-devel
BuildRequires:  pcre-devel
BuildRequires:  libdnet-devel >= 1.10
BuildRequires:  libnet1.0.2-devel
BuildRequires:  chrpath
BuildRequires:  iptables-devel
%if %with clamav
BuildRequires:  clamav-devel >= 0.80
%endif
#BuildRequires: automake1.7
BuildRequires:  autoconf2.5
BuildRequires:  latex2html
BuildRequires:  libgnutls-devel
BuildRequires:  libprelude-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%if %with snmp
snmp(19)                snmp+flexresp(20)
%endif
prelude(21)             prelude+flexresp(22)

Please see the documentation in %{_docdir}/%{name}-%{version}

%package        plain+flexresp
Summary:        Snort with Flexible Response
Group:          Networking/Other
Requires:       snort = %{version}

%description    plain+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with flexresp support. FlexResp allows snort to actively close
offending connections.

%package        mysql
Summary:        Snort with MySQL database support
Group:          Networking/Other
Requires:       snort = %{version}

%description    mysql
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with mysql support.

%package        mysql+flexresp
Summary:        Snort with MySQL database and Flexible Response support
Group:          Networking/Other
Requires:       snort = %{version}

%description    mysql+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with mysql+flexresp support. FlexResp allows snort to actively
close offending connections.

%package        postgresql
Summary:        Snort with PostgreSQL database support
Group:          Networking/Other
Requires:       snort = %{version}

%description    postgresql
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with postgresql support. 

%package        postgresql+flexresp
Summary:        Snort with PostgreSQL database and Flexible Response support
Group:          Networking/Other
Requires:       snort = %{version}

%description    postgresql+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with postgresql+flexresp support. FlexResp allows snort to
actively close offending connections.

%package        bloat
Summary:        Snort with flexresp+mysql+postgresql+snmp+inline support
Group:          Networking/Other
Requires:       snort = %{version}

%description    bloat
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with flexresp+mysql+postgresql+snmp+inline support.

%package        inline
Summary:        Snort with Inline support
Group:          Networking/Other
Requires:       iptables
%if %with clamav
Requires:       clamav >= 0.80-1mdk
Requires:       clamav-db >= 0.80-1mdk
%endif
Requires:       snort = %{version}

%description    inline
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with inline support. Snort-Inline takes packets from iptables
instead of libpcap. It then uses new rule types to help iptables make pass or
drop decisions based on snort rules.  

%package        inline+flexresp
Summary:        Snort with Inline and Flexible Response support
Group:          Networking/Other
Requires:       iptables
%if %with clamav
Requires:       clamav >= 0.80-1mdk
Requires:       clamav-db >= 0.80-1mdk
%endif
Requires:       snort = %{version}

%description    inline+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with inline+flexresp support. FlexResp allows snort to actively
close offending connections. Snort-Inline takes packets from iptables instead
of libpcap. It then uses new rule types to help iptables make pass or drop
decisions based on snort rules.  

%if %with snmp
%package        snmp
Summary:        Snort with SNMP support
Group:          Networking/Other
URL:            http://www.cysols.com/contrib/snortsnmp/index.html
Requires:       snort = %{version}

%description    snmp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with snmp support. The snortSnmpPlugin enables snort to send
snmp alerts to network managemement systems (NMS). The alerts can be traps
(the alert will not be acknowledged by the receiver) or informs (the alert will
be acknowledged by the receiver ). This adds significant power to the NMS by
allowing it to monitor the security of the network. It also allows the snort
sensor to exploit the features that are built into existing network management
systems. 

%package        snmp+flexresp
Summary:        Snort with SNMP and Flexible Response support
Group:          Networking/Other
URL:            http://www.cysols.com/contrib/snortsnmp/index.html
Requires:       snort = %{version}

%description    snmp+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with snmp+flexresp support. FlexResp allows snort to actively
close offending connections. The snortSnmpPlugin enables snort to send snmp
alerts to network managemement systems (NMS). The alerts can be traps (the
alert will not be acknowledged by the receiver) or informs (the alert will be
acknowledged by the receiver ). This adds significant power to the NMS by
allowing it to monitor the security of the network. It also allows the snort
sensor to exploit the features that are built into existing network management
systems. 
%endif

%package        prelude
Summary:        Snort with Prelude support
Group:          Networking/Other
Requires:       snort = %{version}

%description    prelude
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with prelude support.

%package        prelude+flexresp
Summary:        Snort with Prelude and Flexible Response support
Group:          Networking/Other
Requires:       snort = %{version}

%description    prelude+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with prelude+flexresp support. FlexResp allows snort to actively
close offending connections.

%prep
%setup -q

%if %with snmp
%patch0 -p1 -b .SNMP
%endif

%patch1 -p0 -b .lib64

%if %with clamav
%patch2 -p1 -b .clamav
# fix a small bug
perl -pi -e "s|cl_scanbuff|cl_scandesc|g" configure*
%endif

%patch3 -p0 -b .no_timestamp

%if %with snmp
%patch4 -p0 -b .net-snmp_fix
%endif

%patch5 -p1 -b .snortsam
%patch7 -p1 -b .plugins_fix

# fix pid file path
/bin/echo "#define _PATH_VARRUN \"%{_var}/run/%{name}\"" >> acconfig.h

%{__cp} -a %{SOURCE6} .

%build
export WANT_AUTOCONF_2_5=1
%{__rm} -f configure
%{__libtoolize} --copy --force; %{__aclocal} -I m4; %{__automake} --foreign --add-missing --copy; %{__autoconf}

# build snort
%{__rm} -rf building && %{__mkdir_p} building && cd building
SNORT_BASE_CONFIG="--prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libdir}/%{name} \
    --mandir=%{_mandir} \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --disable-prelude \
    --enable-snortsam \
    --enable-shared \
    --enable-pthread \
    --enable-rulestate \
    --enable-dynamicplugin \
    --enable-timestats \
    --enable-perfprofiling \
    --enable-linux-smp-stats \
    --cache-file=../../config.cache"

%if %with snmp
# snmp
{
%{__mkdir_p} snmp; cd snmp
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --with-snmp=%{_prefix} \
    --with-openssl=%{_prefix} \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-snmp
# %{__make} distclean 
cd ..
}

# snmp+flexresp
{
%{__mkdir_p} snmp+flexresp; cd snmp+flexresp
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --with-snmp=%{_prefix} \
    --with-openssl=%{_prefix} \
    --enable-flexresp2 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-snmp+flexresp
# %{__make} distclean 
cd ..
}
%endif

# there are some strange configure errors
# when not doing a distclean between major builds.
# plain 
{
%{__mkdir_p} plain; cd plain
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-plain
#%{__make} distclean 
cd ..
}

# plain+flexresp
{
%{__mkdir_p} plain+flexresp; cd plain+flexresp
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --enable-flexresp2 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-plain+flexresp
# %{__make} distclean 
cd ..
}

# mysql+flexresp
{
%{__mkdir_p} mysql+flexresp; cd mysql+flexresp
../../configure $SNORT_BASE_CONFIG \
    --with-mysql=%{_prefix} \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --enable-flexresp2 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-mysql+flexresp
# %{__make} distclean 
cd ..
}

# mysql
{
%{__mkdir_p} mysql; cd mysql
../../configure $SNORT_BASE_CONFIG \
    --with-mysql=%{_prefix} \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-mysql
# %{__make} distclean 
cd ..
}

# postgresql+flexresp
{
%{__mkdir_p} postgresql+flexresp; cd postgresql+flexresp
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --with-postgresql=%{_prefix} \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --enable-flexresp2 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-postgresql+flexresp
# %{__make} distclean 
cd ..
}

# postgresql
{
%{__mkdir_p} postgresql; cd postgresql
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --with-postgresql=%{_prefix} \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-postgresql
# %{__make} distclean 
cd ..
}

# bloat
{
%{__mkdir_p} bloat; cd bloat
../../configure $SNORT_BASE_CONFIG \
    --with-mysql=%{_prefix} \
    --with-postgresql=%{_prefix} \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --with-openssl=%{_prefix} \
    --enable-flexresp2 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --with-inline --enable-inline \
%if %with clamav
    --with-clamav --enable-clamav \
    --with-clamav-includes=%{_includedir} \
    --with-clamav-defdir=%{_localstatedir}/clamav \
%endif
    --with-libipq-includes=%{_includedir} \
    --with-libipq-libraries=%{_libdir}
%{__make}
%{__mv} src/%{name} ../%{name}-bloat
# %{__make} distclean
cd ..
}

# inline
{
%{__mkdir_p} inline; cd inline
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --with-inline --enable-inline \
%if %with clamav
    --with-clamav --enable-clamav \
    --with-clamav-includes=%{_includedir} \
    --with-clamav-defdir=%{_localstatedir}/clamav \
%endif
    --with-libipq-includes=%{_includedir} \
    --with-libipq-libraries=%{_libdir}
%{__make}
%{__mv} src/%{name} ../%{name}-inline
#%{__make} distclean 
cd ..
}

# inline+flexresp
{
%{__mkdir_p} inline+flexresp; cd inline+flexresp
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --enable-flexresp2 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --with-inline --enable-inline \
%if %with clamav
    --with-clamav --enable-clamav \
    --with-clamav-includes=%{_includedir} \
    --with-clamav-defdir=%{_localstatedir}/clamav \
%endif
    --with-libipq-includes=%{_includedir} \
    --with-libipq-libraries=%{_libdir}
%{__make}
%{__mv} src/%{name} ../%{name}-inline+flexresp
#%{__make} distclean 
cd ..
}

# prelude+flexresp
{
%{__mkdir_p} prelude+flexresp; cd prelude+flexresp
../../configure $SNORT_BASE_CONFIG \
    --enable-prelude --with-libprelude-prefix=%{_prefix} \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --enable-flexresp2 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-prelude+flexresp
# %{__make} distclean 
cd ..
}

# prelude
{
%{__mkdir_p} prelude; cd prelude
../../configure $SNORT_BASE_CONFIG \
    --enable-prelude --with-libprelude-prefix=%{_prefix} \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-snmp --disable-snmp \
    --without-inline --disable-inline \
    --without-clamav --disable-clamav
%{__make}
%{__mv} src/%{name} ../%{name}-prelude
# %{__make} distclean 
cd ..
}

cd ..

## make the html versions of the faq and manual
#pushd doc
#    latex2html -info 0 -local_icons -show_section_numbers -link +2 -split +1 faq.tex
#    latex2html -info 0 -local_icons -show_section_numbers -link +2 -split +2 -noaddress snort_manual.tex
#    # cleanup
#    %{__rm} -f faq/WARNINGS faq/*.tex faq/*.idx faq/*.log faq/*.aux faq/*.pl
#    %{__rm} -f snort_manual/WARNINGS snort_manual/*.tex snort_manual/*.aux snort_manual/*.log snort_manual/*.pl
#popd

%install
%{__rm} -rf %{buildroot} 

%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}/rules
%{__mkdir_p} %{buildroot}%{_sysconfdir}/sysconfig
%{__mkdir_p} %{buildroot}%{_sysconfdir}/logrotate.d
%{__mkdir_p} %{buildroot}/var/log/%{name}/empty
%{__mkdir_p} %{buildroot}/var/run/%{name}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__mkdir_p} %{buildroot}%{_initrddir}
%{__mkdir_p} %{buildroot}%{_mandir}/man8

%{makeinstall_std} -C building/plain

# cleanup
%{__rm} -f %{buildroot}%{_bindir}/%{name}
%{__rm} -rf %{buildroot}%{_prefix}/src
%{__rm} -f %{buildroot}%{_libdir}/%{name}/dynamicengine/*.{a,la}
%{__rm} -f %{buildroot}%{_libdir}/%{name}/dynamicpreprocessor/*.{a,la}

{
pushd building
%{__install} %{name}-plain %{buildroot}%{_sbindir}/%{name}-plain
%{__install} %{name}-plain+flexresp %{buildroot}%{_sbindir}/%{name}-plain+flexresp
%{__install} %{name}-mysql %{buildroot}%{_sbindir}/%{name}-mysql
%{__install} %{name}-mysql+flexresp %{buildroot}%{_sbindir}/%{name}-mysql+flexresp
%{__install} %{name}-postgresql %{buildroot}%{_sbindir}/%{name}-postgresql
%{__install} %{name}-postgresql+flexresp %{buildroot}%{_sbindir}/%{name}-postgresql+flexresp
%{__install} %{name}-bloat %{buildroot}%{_sbindir}/%{name}-bloat
%{__install} %{name}-inline %{buildroot}%{_sbindir}/%{name}-inline
%{__install} %{name}-inline+flexresp %{buildroot}%{_sbindir}/%{name}-inline+flexresp
%if %with snmp
%{__install} %{name}-snmp %{buildroot}%{_sbindir}/%{name}-snmp
%{__install} %{name}-snmp+flexresp %{buildroot}%{_sbindir}/%{name}-snmp+flexresp
%endif
%{__install} %{name}-prelude %{buildroot}%{_sbindir}/%{name}-prelude
%{__install} %{name}-prelude+flexresp %{buildroot}%{_sbindir}/%{name}-prelude+flexresp
popd
}

[[ -f "%{name}.8.bz2" ]] || %{__bzip2} %{name}.8
%{__install} %{name}.8* %{buildroot}%{_mandir}/man8
%{__perl} -pi -e "s|var RULE_PATH ../rules|var RULE_PATH rules|" etc/%{name}.conf

%{__install} -m0644 etc/*.conf %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -m0644 etc/*.config %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -m0644 etc/*.map %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -m0644 etc/generators %{buildroot}%{_sysconfdir}/%{name}/
#%{__install} -m0644 rules/*.rules %{buildroot}%{_sysconfdir}/%{name}/rules/

%{__install} -m0755 %{SOURCE3} %{buildroot}%{_initrddir}/snort
%{__install} -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -m0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# strip rpath
chrpath -d %{buildroot}%{_sbindir}/%{name}-*

# where does this zero file come from? from outer space?
%{__rm} -f doc/README.SNMP.SNMP

# fix libexecdir
%{__perl} -pi -e "s|/usr/local/lib/snort_|%{_libdir}/%{name}/|g" %{buildroot}%{_sysconfdir}/%{name}/snort.conf

%pre
%_pre_useradd snort /var/log/snort /bin/false

%post
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-plain 10
%_post_service snort

%preun
%_preun_service snort

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

%if %with snmp
%post snmp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-snmp 19

%postun snmp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-snmp

%post snmp+flexresp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-snmp+flexresp 20

%postun snmp+flexresp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-snmp+flexresp
%endif

%post prelude
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-prelude 21

%postun prelude
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-prelude

%post prelude+flexresp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-prelude+flexresp 22

%postun prelude+flexresp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-prelude+flexresp

%clean
%{__rm} -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc COPYING ChangeLog RELEASE.NOTES doc/AUTHORS doc/BUGS doc/CREDITS doc/NEWS doc/PROBLEMS doc/TODO doc/USAGE doc/WISHLIST 
%doc doc/README doc/README.alert_order doc/README.asn1 doc/README.csv doc/README.database doc/README.event_queue
%doc doc/README.FLEXRESP doc/README.flow doc/README.flowbits doc/README.flow-portscan doc/README.http_inspect doc/README.PLUGINS
%doc doc/README.sfportscan doc/README.thresholding doc/README.UNSOCK doc/README.wireless snortdb-extra
%doc doc/*.pdf doc/*.tex doc/CRYPTIX-LICENSE.TXT doc/README.sam
# latex2html is borked...
#%doc  doc/snort_manual doc/faq
%attr(0755,root,root) %{_sbindir}/%{name}-plain
%attr(0755,root,root) %{_mandir}/man8/%{name}.8*
%attr(0755,snort,snort) %dir /var/log/%{name}
%attr(0755,snort,snort) %dir /var/log/%{name}/empty
%attr(0755,snort,snort) %dir /var/run/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/rules
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*.config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/threshold.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*.map
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/rules/*.rules
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/generators
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0755,root,root) %{_initrddir}/snort
%attr(0755,root,root) %dir %{_libdir}/%{name}
%attr(0755,root,root) %dir %{_libdir}/%{name}/dynamicengine
%attr(0755,root,root) %dir %{_libdir}/%{name}/dynamicpreprocessor
%attr(0755,root,root) %{_libdir}/%{name}/dynamicengine/libsf_engine.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dcerpc_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dns_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_ftptelnet_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_smtp_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_ssh_preproc.so

%files plain+flexresp
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-plain+flexresp

%files mysql
%defattr(-,root,root)
%doc schemas/create_mysql
%attr(0755,root,root) %{_sbindir}/%{name}-mysql

%files mysql+flexresp
%defattr(-,root,root)
%doc schemas/create_mysql
%attr(0755,root,root) %{_sbindir}/%{name}-mysql+flexresp

%files postgresql
%defattr(-,root,root)
%doc schemas/create_postgresql
%attr(0755,root,root) %{_sbindir}/%{name}-postgresql

%files postgresql+flexresp
%defattr(-,root,root)
%doc schemas/create_postgresql
%attr(0755,root,root) %{_sbindir}/%{name}-postgresql+flexresp

%files bloat
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-bloat

%files inline
%defattr(-,root,root)
%doc doc/README.INLINE
%if %with clamav
%doc doc/README.clamav
%endif
%attr(0755,root,root) %{_sbindir}/%{name}-inline

%files inline+flexresp
%defattr(-,root,root)
%doc doc/README.INLINE
%if %with clamav
%doc doc/README.clamav
%endif
%attr(0755,root,root) %{_sbindir}/%{name}-inline+flexresp

%if %with snmp
%files snmp
%defattr(-,root,root)
%doc doc/README.SNMP etc/SnortCommonMIB.txt etc/SnortIDAlertMIB.txt
%attr(0755,root,root) %{_sbindir}/%{name}-snmp

%files snmp+flexresp
%defattr(-,root,root)
%doc doc/README.SNMP etc/SnortCommonMIB.txt etc/SnortIDAlertMIB.txt
%attr(0755,root,root) %{_sbindir}/%{name}-snmp+flexresp
%endif

%files prelude
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-prelude

%files prelude+flexresp
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-prelude+flexresp


