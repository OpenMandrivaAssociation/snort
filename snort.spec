Summary:	An Intrusion Detection System (IDS)
Name:		snort
Version:	2.9.3
Release:	2
License:	GPLv2
Group:		Networking/Other
URL:		http://www.snort.org/
Source0:	http://www.snort.org/dl/current/%{name}-%{version}.tar.gz
Source1:	http://www.snort.org/dl/current/%{name}-%{version}.tar.gz.sig
Source3:	snort.init
Source4:	snort.logrotate
Source5:	snort.sysconfig
Source6:	snortdb-extra
Patch0:		snort-lib64.diff
# (oe) http://www.inliniac.net/files/
Patch2:		snort-2.9.1-plugins_fix.diff
Patch3:		snort-2.8.5-werror_antibork.diff
Patch4:		snort-2.9.3-plugins_fix.patch
Patch5:		snort-2.9.3-automake113.patch
Requires(post): rpm-helper snort-rules
Requires(preun): rpm-helper snort-rules
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	pcre
Requires:	pcap
Requires:	snort-rules
BuildRequires:	pkgconfig
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRequires:	pcap-devel
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	postgresql-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
BuildRequires:	pcre-devel
BuildRequires:	dnet-devel
BuildRequires:	net1.0-devel
BuildRequires:	chrpath
BuildRequires:	iptables-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	latex2html
BuildRequires:	libgcrypt-devel
BuildRequires:	gnutls-devel
BuildRequires:	prelude-devel
BuildRequires:	iptables-ipq-devel
BuildRequires:	daq-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Suggests:	snortsam

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

%package	plain+flexresp
Summary:	Snort with Flexible Response
Group:		Networking/Other
Requires:	snort >= %{version}

%description	plain+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with flexresp support. FlexResp allows snort to actively close
offending connections.

%package	mysql
Summary:	Snort with MySQL database support
Group:		Networking/Other
Requires:	snort >= %{version}

%description	mysql
snort is a libpcap-based packet sniffer/logger which can be used as a
hightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
o detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with mysql support.

%package	mysql+flexresp
Summary:	Snort with MySQL database and Flexible Response support
Group:		Networking/Other
Requires:	snort >= %{version}

%description	mysql+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with mysql+flexresp support. FlexResp allows snort to actively
close offending connections.

%package	postgresql
Summary:	Snort with PostgreSQL database support
Group:		Networking/Other
Requires:	snort >= %{version}

%description	postgresql
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with postgresql support. 

%package	postgresql+flexresp
Summary:	Snort with PostgreSQL database and Flexible Response support
Group:		Networking/Other
Requires:	snort >= %{version}

%description	postgresql+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with postgresql+flexresp support. FlexResp allows snort to
actively close offending connections.

%package	bloat
Summary:	Snort with flexresp+mysql+postgresql+inline+prelude support
Group:		Networking/Other
Requires:	snort >= %{version}

%description	bloat
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with flexresp+mysql+postgresql+inline+prelude support.

%package	inline
Summary:	Snort with Inline support
Group:		Networking/Other
Requires:	iptables
Requires:	snort >= %{version}

%description	inline
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

%package	inline+flexresp
Summary:	Snort with Inline and Flexible Response support
Group:		Networking/Other
Requires:	iptables
Requires:	snort >= %{version}

%description	inline+flexresp
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

%package	prelude
Summary:	Snort with Prelude support
Group:		Networking/Other
Requires:	snort >= %{version}

%description	prelude
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with prelude support.

%package	prelude+flexresp
Summary:	Snort with Prelude and Flexible Response support
Group:		Networking/Other
Requires:	snort >= %{version}

%description	prelude+flexresp
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

Snort compiled with prelude+flexresp support. FlexResp allows snort to actively
close offending connections.

%package        devel
Summary:        Snort development files
Group:          Networking/Other
Requires:       snort = %{version}

%description    devel
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
port scans, CGI attacks, SMB probes, OS fingerprinting attempts, and much more.
Snort has a real-time alerting capabilty, with alerts being sent to syslog, a
separate "alert" file, or as a WinPopup message via Samba's smbclient

This are snort H files.


%prep

%setup -q -n %{name}-%{version}
%patch0 -p0 -b .lib64
%patch2 -p1 -b .plugins_fix
%patch3 -p0 -b .werror_antibork
%patch4 -p0 -b .plugins_fix
%patch5 -p1 -b .automake113

# fix pid file path
/bin/echo "#define _PATH_VARRUN \"%{_var}/run/%{name}\"" >> acconfig.h

%{__cp} -a %{SOURCE6} .

%build
%serverbuild
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --automake --copy --force; aclocal -I m4; autoheader; automake --foreign --add-missing --copy; autoconf

# build snort
%{__rm} -rf building && %{__mkdir_p} building && cd building
SNORT_BASE_CONFIG="--prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libdir}/%{name} \
    --mandir=%{_mandir} \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --disable-prelude \
    --enable-shared \
    --enable-pthread \
    --enable-dynamicplugin \
    --enable-perfprofiling \
    --enable-linux-smp-stats \
    --disable-static-daq \
    --enable-ppm \
    --enable-decoder-preprocessor-rules \
    --cache-file=../../config.cache \
    --enable-reload \
    --enable-reload-error-restart \
    --enable-zlib \
    --enable-mpls \
    --enable-targetbased \
    --enable-perfprofiling \
    --enable-active-response \
    --enable-normalizer \
    --enable-react \
    --with-daq-includes=%{_includedir} \
    --with-daq-libraries=%{_libdir}"

# Will be, when I port razorback into Mandriva/Mageia
#    --enable-rzb-saac"

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
    --without-inline --disable-inline
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
    --enable-flexresp3 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline
%{__make}
%{__mv} src/%{name} ../%{name}-plain+flexresp
# %{__make} distclean 
cd ..
}

# mysql+flexresp
{
%{__mkdir_p} mysql+flexresp; cd mysql+flexresp
../../configure $SNORT_BASE_CONFIG \
    --with-mysql-includes=%{_includedir} \
    --with-mysql-libraries=%{_libdir} \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --enable-flexresp3 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline
%{__make}
%{__mv} src/%{name} ../%{name}-mysql+flexresp
# %{__make} distclean 
cd ..
}

# mysql
{
%{__mkdir_p} mysql; cd mysql
../../configure $SNORT_BASE_CONFIG \
    --with-mysql-includes=%{_includedir} \
    --with-mysql-libraries=%{_libdir} \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-inline --disable-inline
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
    --enable-flexresp3 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline
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
    --without-inline --disable-inline
%{__make}
%{__mv} src/%{name} ../%{name}-postgresql
# %{__make} distclean 
cd ..
}

# bloat
{
%{__mkdir_p} bloat; cd bloat
../../configure $SNORT_BASE_CONFIG \
    --with-mysql-includes=%{_includedir} \
    --with-mysql-libraries=%{_libdir} \
    --with-postgresql=%{_prefix} \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --with-openssl=%{_prefix} \
    --enable-flexresp3 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --with-inline --enable-inline \
    --with-libipq-includes=%{_includedir} \
    --with-libipq-libraries=%{_libdir} \
    --enable-prelude --with-libprelude-prefix=%{_prefix}
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
    --with-inline --enable-inline \
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
    --enable-flexresp3 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --with-inline --enable-inline \
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
    --enable-flexresp3 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline
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
    --without-inline --disable-inline
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
%{__rm} -f  %{buildroot}%{_bindir}/%{name}
%{__rm} -rf %{buildroot}%{_prefix}/src
%{__rm} -f  %{buildroot}%{_libdir}/%{name}/dynamicengine/*.{a,la}
%{__rm} -f  %{buildroot}%{_libdir}/%{name}/dynamicpreprocessor/*.{a,la}
#%{__rm} -f %{buildroot}%{_libdir}/%{name}/dynamicrules/*.{a,la}
%{__rm} -f  %{buildroot}%{_libdir}/%{name}/dynamic_preproc/*.{a,la}

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
%{__install} %{name}-prelude %{buildroot}%{_sbindir}/%{name}-prelude
%{__install} %{name}-prelude+flexresp %{buildroot}%{_sbindir}/%{name}-prelude+flexresp
popd
}

%{__install} %{name}.8* %{buildroot}%{_mandir}/man8
%{__perl} -pi -e "s|var RULE_PATH ../rules|var RULE_PATH rules|" etc/%{name}.conf

%{__install} -m0644 etc/*.conf %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -m0644 etc/*.config %{buildroot}%{_sysconfdir}/%{name}/
%{__install} -m0644 etc/*.map %{buildroot}%{_sysconfdir}/%{name}/

%{__install} -m0755 %{SOURCE3} %{buildroot}%{_initrddir}/snort
%{__install} -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -m0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# strip rpath
chrpath -d %{buildroot}%{_sbindir}/%{name}-*

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

%post prelude
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-prelude 19

%postun prelude
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-prelude

%post prelude+flexresp
%{_sbindir}/update-alternatives --install %{_sbindir}/%{name} %{name} %{_sbindir}/%{name}-prelude+flexresp 20

%postun prelude+flexresp
%{_sbindir}/update-alternatives --remove %{name} %{_sbindir}/%{name}-prelude+flexresp

%clean
%{__rm} -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc COPYING ChangeLog RELEASE.NOTES
%doc doc/AUTHORS doc/BUGS doc/CREDITS doc/generators doc/INSTALL doc/NEWS doc/PROBLEMS doc/README
%doc doc/README.alert_order doc/README.asn1 doc/README.csv
%doc doc/README.dcerpc2 doc/README.decode doc/README.dns doc/README.event_queue 
%doc doc/README.flowbits doc/README.frag3 doc/README.daq doc/README.decoder_preproc_rules doc/README.reload
%doc doc/README.ftptelnet doc/README.gre doc/README.http_inspect doc/README.ipip doc/README.filters
%doc doc/README.ipv6 doc/README.pcap_readmode doc/README.PerfProfiling doc/README.PLUGINS doc/README.ppm
%doc doc/README.sfportscan doc/README.SMTP doc/README.ssh doc/README.ssl doc/README.multipleconfigs
%doc doc/README.stream5 doc/README.tag doc/README.thresholding doc/README.UNSOCK doc/README.variables
%doc doc/README.WIN32 doc/TODO doc/USAGE doc/WISHLIST doc/README.active 
%doc doc/README.sensitive_data 
%doc doc/*.pdf doc/*.tex
#%doc %doc doc/CRYPTIX-LICENSE.TXT doc/README.sam
# latex2html is borked...
#%doc  doc/snort_manual doc/faq
%attr(0755,root,root) %{_sbindir}/%{name}-plain
%attr(0755,root,root) %{_bindir}/u2boat
%attr(0755,root,root) %{_bindir}/u2spewfoo
%attr(0755,root,root) %{_mandir}/man8/%{name}.8*
%attr(0755,snort,snort) %dir /var/log/%{name}
%attr(0755,snort,snort) %dir /var/log/%{name}/empty
%attr(0755,snort,snort) %dir /var/run/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/rules
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*.config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/threshold.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*.map
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0755,root,root) %{_initrddir}/snort
%attr(0755,root,root) %dir %{_libdir}/%{name}
%attr(0755,root,root) %dir %{_libdir}/%{name}/dynamicengine
%attr(0755,root,root) %dir %{_libdir}/%{name}/dynamicpreprocessor
#%attr(0755,root,root) %dir %{_libdir}/%{name}/dynamicrules
%attr(0755,root,root) %{_libdir}/%{name}/dynamicengine/libsf_engine.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dce2_preproc.so
#attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dcerpc_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dns_preproc.so
#%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/lib_sfdynamic_preprocessor_example.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_ftptelnet_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_smtp_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_ssh_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_ssl_preproc.so
#%attr(0755,root,root) %{_libdir}/%{name}/dynamicrules/lib_sfdynamic_example_rule.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_sdf_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_imap_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_pop_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_reputation_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_sip_preproc.so

%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dnp3_preproc.*
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_gtp_preproc.*
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_modbus_preproc.*
%attr(0755,root,root) %{_libdir}/%{name}/dynamic_output/libsf_dynamic_output.*

%files plain+flexresp
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-plain+flexresp

%files mysql
%defattr(-,root,root)
#%doc schemas/create_mysql
%attr(0755,root,root) %{_sbindir}/%{name}-mysql

%files mysql+flexresp
%defattr(-,root,root)
#%doc schemas/create_mysql
%attr(0755,root,root) %{_sbindir}/%{name}-mysql+flexresp

%files postgresql
%defattr(-,root,root)
#%doc schemas/create_postgresql
%attr(0755,root,root) %{_sbindir}/%{name}-postgresql

%files postgresql+flexresp
%defattr(-,root,root)
#%doc schemas/create_postgresql
%attr(0755,root,root) %{_sbindir}/%{name}-postgresql+flexresp

%files bloat
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-bloat

%files inline
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-inline

%files inline+flexresp
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-inline+flexresp

%files prelude
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-prelude

%files prelude+flexresp
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-prelude+flexresp

%files devel
%defattr(-,root,root)
%attr(0755,root,root) %dir %{_libdir}/pkgconfig
%attr(0644,root,root) %{_libdir}/pkgconfig/snort_output.pc
%attr(0644,root,root) %{_libdir}/pkgconfig/snort.pc
%attr(0644,root,root) %{_libdir}/pkgconfig/snort_preproc.pc
%attr(0755,root,root) %dir %{_includedir}/%{name}/dynamic_preproc
%attr(0755,root,root) %dir %{_includedir}/%{name}/dynamic_output/*.h
%attr(0644,root,root) %{_includedir}/%{name}/dynamic_preproc/*.h



%changelog
* Wed Aug 08 2012 Danila Leontiev <danila.leontiev@rosalab.ru> 2.9.3-1
- Fixed libs for 86_64

* Wed Aug 01 2012 Danila Leontiev <danila.leontiev@rosalab.ru> 2.9.3-1
- Updated for new version
- From spec removed schemas/create_mysql, schemas/create_postgresql (a few README files)
- Added: /usr/include/snort/dynamic_output/*.h
	 /usr/lib/pkgconfig/snort_output.pc
	 /usr/lib/snort/dynamic_output/libsf_dynamic_output*
	 /usr/lib/snort_dynamicpreprocessor/libsf_dnp3_preproc*
	 /usr/lib/snort_dynamicpreprocessor/libsf_gtp_preproc*
	 /usr/lib/snort_dynamicpreprocessor/libsf_modbus_preproc*
- Removed patch snort-2.8.5-missing-header.patch, snortsam-2.9.0-dlucio.diff
- Fixed patch	snort-2.9.1-plugins_fix.diff, snort-lib64.diff (for 2.9.3 version)



* Thu Aug 25 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.1-1mdv2011.0
+ Revision: 697128
- 2.9.1
  new devel subpackage
  P2 rediffed

* Wed Apr 06 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.0.5-1
+ Revision: 651355
- 2.9.0.5

* Thu Mar 24 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.0.4-4
+ Revision: 648416
- Ipv6 enabled
  GRE enabled

* Sun Mar 20 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.0.4-3
+ Revision: 647086
- Rebuild

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 2.9.0.4-2
+ Revision: 645759
- relink against libmysqlclient.so.18

* Fri Feb 11 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.0.4-1
+ Revision: 637340
- 2.9.0.4

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.9.0.3-4mdv2011.0
+ Revision: 627717
- don't force the usage of automake1.7

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 2.9.0.3-3mdv2011.0
+ Revision: 627009
- rebuilt against mysql-5.5.8 libs, again

* Mon Dec 27 2010 Oden Eriksson <oeriksson@mandriva.com> 2.9.0.3-2mdv2011.0
+ Revision: 625430
- rebuilt against mysql-5.5.8 libs

* Wed Dec 22 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.0.3-1mdv2011.0
+ Revision: 623833
- 2.9.0.3

* Thu Dec 02 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.0.2-1mdv2011.0
+ Revision: 605036
- 2.9.0.2

* Tue Nov 02 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.0.1-1mdv2011.0
+ Revision: 592693
- 2.9.0.1

* Sun Oct 10 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.9.0-1mdv2011.0
+ Revision: 584501
- 2.9.0
  All patches were diffed
  docs were fixed
  new config options we were missing (i was missing :P )

* Fri Jul 23 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.6.1-1mdv2011.0
+ Revision: 557103
- 2.8.6.1

* Wed Apr 28 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.6-2mdv2010.1
+ Revision: 540364
- P1 rediffed

* Tue Apr 27 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.6-1mdv2010.1
+ Revision: 539419
- 2.8.6
  P1 & P2 rediffed

* Thu Apr 08 2010 Eugeni Dodonov <eugeni@mandriva.com> 2.8.5.3-4mdv2010.1
+ Revision: 533101
- Add BR on ipw-devel

  + Luis Daniel Lucio Quiroz <dlucio@mandriva.org>
    - Rebuild for new OpenSSL
    - Rebuild for new OpenSSL

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.5.3-2mdv2010.1
+ Revision: 511638
- rebuilt against openssl-0.9.8m

* Thu Feb 18 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.5.3-1mdv2010.1
+ Revision: 507339
- 2.8.5.3

* Wed Feb 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.5.2-3mdv2010.1
+ Revision: 507044
- rebuild

* Mon Feb 08 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.5.2-2mdv2010.1
+ Revision: 501879
- service snort reload done

* Wed Dec 30 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.5.2-1mdv2010.1
+ Revision: 484156
- New 2.8.5.2

* Mon Oct 26 2009 Oden Eriksson <oeriksson@mandriva.com> 2.8.5.1-1mdv2010.0
+ Revision: 459357
- fix build
- 2.8.5.1

* Mon Oct 12 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.5-5mdv2010.0
+ Revision: 456851
- Lets dissable P4, it is not needed because libnet1.0 is fixed

* Sun Oct 11 2009 Oden Eriksson <oeriksson@mandriva.com> 2.8.5-4mdv2010.0
+ Revision: 456633
- rebuilt against a fixed libnet1.0.2

* Sat Oct 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.8.5-3mdv2010.0
+ Revision: 456580
- Patch4: add missing header, which fixes compilation

  + Luis Daniel Lucio Quiroz <dlucio@mandriva.org>
    - Back to libnet1.0, snort doest need that version
    - We use now libnet1.1 instead of libnet1.0
    - SILENCE:P1 rediff, bad option should be OPT_TYPE_ACTION
    - P1 rediff, bad option should be OPT_TYPE_ACTION
    - P1 rediff, fwsam option was not registered

* Thu Sep 24 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.5-1mdv2010.0
+ Revision: 448114
- Install cleanup #3
- Install cleanup #2
- Install cleanup
- Muchas gracias a Oden, Tryke (SnortTeam)
- All patches differed
- New release 2.8.5
  new --enable-reload flag

  + Oden Eriksson <oeriksson@mandriva.com>
    - P3: fix build

* Mon Jun 29 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.4.1-3mdv2010.0
+ Revision: 390703
- Patch1 updated, it fix a 64bits twofish problem
- Patch3 no needed anymore, patch1 already fix agains 2.8.4.1

* Sat May 02 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.4.1-2mdv2010.0
+ Revision: 370604
- new version 2.8.4.1 #4
- new version 2.8.4.1 #3
- new version 2.8.4.1 #3
- new version 2.8.4.1

* Thu Apr 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.8.4-1mdv2009.1
+ Revision: 365482
- 2.8.4
- drop redundant patches (P3,P4)
- rediffed P1
- make snortsam build (P3)

* Fri Mar 20 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.3.2-3mdv2009.1
+ Revision: 358262
- Add snortsam suggestion

* Thu Mar 19 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.8.3.2-2mdv2009.1
+ Revision: 358203
- Patch1 updated, SnortSAM support enable
- Patch1 update, SnortSAM support enable

* Wed Jan 21 2009 Oden Eriksson <oeriksson@mandriva.com> 2.8.3.2-1mdv2009.1
+ Revision: 332198
- 2.8.3.2
- fix build with -Werror=format-security (P4)

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.3.1-4mdv2009.1
+ Revision: 311207
- rebuilt against mysql-5.1.30 libs

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.3.1-3mdv2009.1
+ Revision: 298372
- rebuilt against libpcap-1.0.0

* Sat Oct 25 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.3.1-2mdv2009.1
+ Revision: 297273
- rebuild

* Wed Oct 15 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.3.1-1mdv2009.1
+ Revision: 293882
- 2.8.3.1

* Fri Sep 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.3-1mdv2009.0
+ Revision: 281092
- 2.8.3

* Tue Aug 26 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.2.2-2mdv2009.0
+ Revision: 276116
- rebuild

* Sun Aug 03 2008 Frederik Himpe <fhimpe@mandriva.org> 2.8.2.2-1mdv2009.0
+ Revision: 261918
- update to new version 2.8.2.2

* Mon Jun 23 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.2.1-3mdv2009.0
+ Revision: 228236
- bump release due to build system problems
- rebuild

* Sun Jun 22 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.2.1-1mdv2009.0
+ Revision: 227929
- 2.8.2.1

* Thu May 08 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.2-0.rc1.2mdv2009.0
+ Revision: 204496
- rebuild
- license is GPLv2 (Charles A Edwards)

* Wed May 07 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.2-0.rc1.1mdv2009.0
+ Revision: 202817
- whoops!
- 2.8.2.rc1
- rediffed P1
- bump release
- 2.8.1
- major cleanup
- remove dead addons
- rediffed some patches
- added lfs headers in the init script

* Thu Jan 24 2008 Funda Wang <fwang@mandriva.org> 2.8.0.1-0.2mdv2008.1
+ Revision: 157294
- rebuild

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.0.1-0.1mdv2008.1
+ Revision: 141695
- 2.8.0.1
- fix deps
- drop P3, implemented upstream
- rediffed P5 though it won't compile with it...
- rediffed P7
- added P6 to make it compile with the new respond2 code
- neither snmp or clamav support works atm, maybe later?

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 David Walluck <walluck@mandriva.org> 2.7.0.1-2mdv2008.0
+ Revision: 79689
- remove some version requirements on BuildRequires
- fix snort requires
- don't bzip2 the manpage
- fix lib BuildRequires on 64-bit
- fix gnutls-devel and prelude-devel BuildRequires
- 2.7.0.1
- rediff lib64 patch due to mysqlclient check changes

* Wed Jul 04 2007 Andreas Hasenack <andreas@mandriva.com> 2.6.1.5-1mdv2008.0
+ Revision: 48285
- updated to version 2.6.1.5
- updated no_timestamp patch for this version
- using serverbuild macro (-fstack-protector-all)


* Tue Feb 27 2007 Oden Eriksson <oeriksson@mandriva.com> 2.6.1.3-2mdv2007.0
+ Revision: 126207
- updated the inline clamav patch (P2, rediffed)

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 2.6.1.3-1mdv2007.1
+ Revision: 123561
- 2.6.1.3 (fixes CVE-2006-5276)

* Fri Dec 29 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.1.2-3mdv2007.1
+ Revision: 102554
- call the correct initscript in the logrotation script (Frank Griffin)

* Tue Dec 26 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.1.2-2mdv2007.1
+ Revision: 102095
- switch S4 with S5 in the install section (Frank Griffin)

* Thu Dec 21 2006 David Walluck <walluck@mandriva.org> 2.6.1.2-1mdv2007.1
+ Revision: 100929
- fix libnet BuildRequires
- 2.6.1.2
- use macros
- 2.6.1

* Wed Oct 25 2006 David Walluck <walluck@mandriva.org> 2.6.0.2-2mdv2007.1
+ Revision: 72237
- bump release
- really fix libsf_dns_preproc
- 2.6.0.2
- Import snort

* Sun Sep 17 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.0-3mdv2007.0
- fix #25796

* Tue Sep 05 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.0-1mdv2007.0
- rebuilt against MySQL-5.0.24a-1mdv2007.0 due to ABI changes

* Wed Jul 26 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.0-1mdv2007.0
- 2.6.0
- don't build with snmp and clamav support per default, maybe later
- rediffed patches; P0,P1,P2,P5
- nuke bundled libtool (P6)
- fix the dynamic plugin dir and don't use -version-info (P6)
- fix deps
- use the new flexresp2 (uses libdnet, inline still uses libnet1.0.2)
- parallel building is borked (thanks Christiaan Welvaart)

* Fri Jun 30 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.5-1mdv2007.0
- 2.4.5
- rediffed P0
- fix #15368

* Fri Jun 30 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.4-1mdv2007.0
- rebuilt against gnutls-1.4.0

* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.4-2mdk
- rebuilt against libnet1.0.2

* Tue Mar 14 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.4-1mdk
- 2.4.4
- rediffed P0

* Mon Jan 30 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-7mdk
- added the prelude stuff

* Wed Jan 04 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-6mdk
- rebuilt against new net-snmp with new major (10)

* Wed Dec 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-5mdk
- rebuilt against net-snmp that has new major (9)

* Tue Dec 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-4mdk
- added the snortsam patch (P5)

* Sun Nov 13 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-3mdk
- rebuilt against openssl-0.9.8a

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-2mdk
- it's a good idea to build against latest build deps... (MySQL)

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-1mdk
- 2.4.3
- rediffed patches; P0,P1,P2
- the rules are now packed separately
- disable prelude support for now (--disable-prelude)

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Sun May 29 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-1mdk
- 2.3.3
- use conditional restart in S4 (Martin Ma=E8ok)
- nuke prereq

* Thu Apr 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.1-3mdk
- rebuilt against new postgresql libs

* Tue Mar 15 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.1-2mdk
- provide the /var/log/snort/empty directory to mask a bug in 
  logrotate

* Sat Mar 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.1-1mdk
- 2.3.1

* Sat Mar 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.0-2mdk
- fix #14477
- added P3 so that -L work as stated in the man page
- own the %%{_sysconfdir}/snort directory
- use the %%mkrel macro
- added P4 to make the snmp enabled snort binary build
- misc spec file fixes

* Mon Jan 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.0-1mdk
- 2.3.0 final
- provide the html versions of the faq and manual

* Mon Jan 24 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.0-0.RC2.4mdk
- rebuild

* Sat Jan 22 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.0-0.RC2.3mdk
- rebuilt against a bunch on new deps
- fix deps

* Fri Dec 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.0-0.RC2.2mdk
- added one line of code to P2

* Fri Dec 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.3.0-0.RC2.1mdk
- 2.3.0RC2
- rediffed P0
- rediffed P1 and added lib64 fixes to it
- drop P3, it's implemented upstream
- deactivate the snmp stuff for now as it won't build with net-snmp-5.2 libs
- added rediffed P2 from the snort_inline patch archive
- added S5 because the bundled contribs is gone

* Tue Nov 09 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.0-3mdk
- fix forgotten "%%defattr(-,root,root)" for the inline sub packages

* Fri Nov 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.0-2mdk
- new P2 (snort_inline-2.2.0a)

* Mon Nov 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.0-1mdk
- 2.2.0
- new P0
- speed up configure by using --cache-file
- added inline support (P2), thanks to William Metcalf for helping out

* Fri May 14 2004 Florin <florin@mandrakesoft.com> 2.1.3-0.RC1.1mdk
- 2.1.3RC1
- add md5 source1
- merge gb's package with with cooker
- strib the binaries

* Mon Mar 08 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.1.0-1.2mdk
- fix requires

* Fri Mar 05 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.1.0-1.1mdk
- buildrequires net1.0-devel

