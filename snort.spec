Summary:	An Intrusion Detection System (IDS)
Name:		snort
Version:	2.8.5
Release:	%mkrel 1
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
Patch1:		snortsam-2.8.5-dlucio.diff
Patch2:		snort-plugins_fix.diff
Patch3:		snort-2.8.5-werror_antibork.diff
Requires(post): rpm-helper snort-rules
Requires(preun): rpm-helper snort-rules
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	pcre
Requires:	pcap
Requires:	snort-rules
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
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
BuildRequires:	gnutls-devel
BuildRequires:	prelude-devel
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
Snort is a libpcap-based packet sniffer/logger which can be used as a
lightweight network intrusion detection system. It features rules based logging
and can perform protocol analysis, content searching/matching and can be used
to detect a variety of attacks and probes, such as buffer overflows, stealth
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

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0 -b .lib64
%patch1 -p1 -b .snortsam
%patch2 -p1 -b .plugins_fix
%patch3 -p0 -b .werror_antibork

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
    --enable-snortsam \
    --enable-shared \
    --enable-pthread \
    --enable-rulestate \
    --enable-dynamicplugin \
    --enable-timestats \
    --enable-perfprofiling \
    --enable-linux-smp-stats \
    --enable-ppm \
    --enable-decoder-preprocessor-rules \
    --cache-file=../../config.cache \
    --enable-reload"

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
    --enable-flexresp2 \
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
    --with-mysql=%{_prefix} \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --enable-flexresp2 \
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
    --with-mysql=%{_prefix} \
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
    --enable-flexresp2 \
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
    --with-mysql=%{_prefix} \
    --with-postgresql=%{_prefix} \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --with-openssl=%{_prefix} \
    --enable-flexresp2 \
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
    --enable-flexresp2 \
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
    --enable-flexresp2 \
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
%{__rm} -f %{buildroot}%{_bindir}/%{name}
%{__rm} -rf %{buildroot}%{_prefix}/src
%{__rm} -f %{buildroot}%{_libdir}/%{name}/dynamicengine/*.{a,la}
%{__rm} -f %{buildroot}%{_libdir}/%{name}/dynamicpreprocessor/*.{a,la}
##%{__rm} -f %{buildroot}%{_libdir}/%{name}/dynamicrules/*.{a,la}

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
%doc doc/README.alert_order doc/README.ARUBA doc/README.asn1 doc/README.csv doc/README.database
%doc doc/README.dcerpc doc/README.decode doc/README.dns doc/README.event_queue doc/README.FLEXRESP
%doc doc/README.FLEXRESP2 doc/README.flowbits doc/README.frag3
%doc doc/README.ftptelnet doc/README.gre doc/README.http_inspect doc/README.ipip
%doc doc/README.ipv6 doc/README.pcap_readmode doc/README.PerfProfiling doc/README.PLUGINS doc/README.ppm
%doc doc/README.sfportscan doc/README.SMTP doc/README.ssh doc/README.ssl
%doc doc/README.stream5 doc/README.tag doc/README.thresholding doc/README.UNSOCK doc/README.variables
%doc doc/README.WIN32 doc/README.wireless doc/TODO doc/USAGE doc/WISHLIST
%doc doc/*.pdf doc/*.tex
#%doc %doc doc/CRYPTIX-LICENSE.TXT doc/README.sam
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
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0755,root,root) %{_initrddir}/snort
%attr(0755,root,root) %dir %{_libdir}/%{name}
%attr(0755,root,root) %dir %{_libdir}/%{name}/dynamicengine
%attr(0755,root,root) %dir %{_libdir}/%{name}/dynamicpreprocessor
##%attr(0755,root,root) %dir %{_libdir}/%{name}/dynamicrules
%attr(0755,root,root) %{_libdir}/%{name}/dynamicengine/libsf_engine.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dce2_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dcerpc_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dns_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/lib_sfdynamic_preprocessor_example.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_ftptelnet_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_smtp_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_ssh_preproc.so
%attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_ssl_preproc.so
##%attr(0755,root,root) %{_libdir}/%{name}/dynamicrules/lib_sfdynamic_example_rule.so

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
%attr(0755,root,root) %{_sbindir}/%{name}-inline

%files inline+flexresp
%defattr(-,root,root)
%doc doc/README.INLINE
%attr(0755,root,root) %{_sbindir}/%{name}-inline+flexresp

%files prelude
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-prelude

%files prelude+flexresp
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}-prelude+flexresp
