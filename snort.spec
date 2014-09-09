Summary:        An Intrusion Detection System (IDS)
Name:           snort
Version:        2.9.6.2
Release:        1
License:        GPLv2+
Group:          Networking/Other
Url:            http://www.snort.org/
Source0:        http://www.snort.org/dl/current/%{name}-%{version}.tar.gz
#Source1:        http://www.snort.org/dl/current/%{name}-%{version}.tar.gz.sig
Source3:        snort.service
Source4:        snort.logrotate
Source5:        snort.sysconfig
Source6:        snortdb-extra
Source7:        snort-wrapper.sh
Source100:	%{name}.rpmlintrc
Patch0:         snort-lib64.diff
# (oe) http://www.inliniac.net/files/
Patch2:         snort-2.9.1-plugins_fix.diff
Patch3:         snort-2.8.5-werror_antibork.diff
Patch4:         snort-2.9.3-plugins_fix.patch
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
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libipq)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libprelude)
BuildRequires:  pkgconfig(libtirpc)
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
%setup -q
%patch0 -p0 -b .lib64
%patch2 -p1 -b .plugins_fix
%patch3 -p0 -b .werror_antibork
%patch4 -p0 -b .plugins_fix

# fix pid file path
/bin/echo "#define _PATH_VARRUN \"%{_var}/run/%{name}\"" >> acconfig.h

cp -a %{SOURCE6} .

%build
%serverbuild
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --automake --copy --force; aclocal -I m4; autoheader; automake --foreign --add-missing --copy; autoconf

# build snort
rm -rf building && mkdir -p building && cd building
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
mkdir -p plain; cd plain
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-inline --disable-inline
make
mv src/%{name} ../%{name}-plain
#make distclean 
cd ..
}

# plain+flexresp
{
mkdir -p plain+flexresp; cd plain+flexresp
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --enable-flexresp3 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline
make
mv src/%{name} ../%{name}-plain+flexresp
# make distclean 
cd ..
}

# mysql+flexresp
{
mkdir -p mysql+flexresp; cd mysql+flexresp
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
make
mv src/%{name} ../%{name}-mysql+flexresp
# make distclean 
cd ..
}

# mysql
{
mkdir -p mysql; cd mysql
../../configure $SNORT_BASE_CONFIG \
    --with-mysql-includes=%{_includedir} \
    --with-mysql-libraries=%{_libdir} \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-inline --disable-inline
make
mv src/%{name} ../%{name}-mysql
# make distclean 
cd ..
}

# postgresql+flexresp
{
mkdir -p postgresql+flexresp; cd postgresql+flexresp
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --with-postgresql=%{_prefix} \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --enable-flexresp3 \
    --with-dnet-includes=%{_includedir} \
    --with-dnet-libraries=%{_libdir} \
    --without-inline --disable-inline
make
mv src/%{name} ../%{name}-postgresql+flexresp
# make distclean 
cd ..
}

# postgresql
{
mkdir -p postgresql; cd postgresql
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --with-postgresql=%{_prefix} \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-inline --disable-inline
make
mv src/%{name} ../%{name}-postgresql
# make distclean 
cd ..
}

# bloat
{
mkdir -p bloat; cd bloat
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
make
mv src/%{name} ../%{name}-bloat
# make distclean
cd ..
}

# inline
{
mkdir -p inline; cd inline
../../configure $SNORT_BASE_CONFIG \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --with-inline --enable-inline \
    --with-libipq-includes=%{_includedir} \
    --with-libipq-libraries=%{_libdir}
make
mv src/%{name} ../%{name}-inline
#make distclean 
cd ..
}

# inline+flexresp
{
mkdir -p inline+flexresp; cd inline+flexresp
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
make
mv src/%{name} ../%{name}-inline+flexresp
#make distclean 
cd ..
}

# prelude+flexresp
{
mkdir -p prelude+flexresp; cd prelude+flexresp
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
make
mv src/%{name} ../%{name}-prelude+flexresp
# make distclean 
cd ..
}

# prelude
{
mkdir -p prelude; cd prelude
../../configure $SNORT_BASE_CONFIG \
    --enable-prelude --with-libprelude-prefix=%{_prefix} \
    --without-mysql --disable-mysql \
    --without-postgresql --disable-postgresql \
    --without-oracle --disable-oracle \
    --without-odbc --disable-odbc \
    --without-inline --disable-inline
make
mv src/%{name} ../%{name}-prelude
# make distclean 
cd ..
}

cd ..

## make the html versions of the faq and manual
#pushd doc
#    latex2html -info 0 -local_icons -show_section_numbers -link +2 -split +1 faq.tex
#    latex2html -info 0 -local_icons -show_section_numbers -link +2 -split +2 -noaddress snort_manual.tex
#    # cleanup
#    rm -f faq/WARNINGS faq/*.tex faq/*.idx faq/*.log faq/*.aux faq/*.pl
#    rm -f snort_manual/WARNINGS snort_manual/*.tex snort_manual/*.aux snort_manual/*.log snort_manual/*.pl
#popd

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/rules
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}/var/log/%{name}/empty
mkdir -p %{buildroot}/var/run/%{name}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_mandir}/man8

%makeinstall_std -C building/plain

# cleanup
rm -f  %{buildroot}%{_bindir}/%{name}
rm -rf %{buildroot}%{_prefix}/src
rm -f  %{buildroot}%{_libdir}/%{name}/dynamicengine/*.{a,la}
rm -f  %{buildroot}%{_libdir}/%{name}/dynamicpreprocessor/*.{a,la}
rm -f  %{buildroot}%{_libdir}/%{name}/dynamic_preproc/*.{a,la}

{
pushd building
install %{name}-plain %{buildroot}%{_sbindir}/%{name}-plain
install %{name}-plain+flexresp %{buildroot}%{_sbindir}/%{name}-plain+flexresp
install %{name}-mysql %{buildroot}%{_sbindir}/%{name}-mysql
install %{name}-mysql+flexresp %{buildroot}%{_sbindir}/%{name}-mysql+flexresp
install %{name}-postgresql %{buildroot}%{_sbindir}/%{name}-postgresql
install %{name}-postgresql+flexresp %{buildroot}%{_sbindir}/%{name}-postgresql+flexresp
install %{name}-bloat %{buildroot}%{_sbindir}/%{name}-bloat
install %{name}-inline %{buildroot}%{_sbindir}/%{name}-inline
install %{name}-inline+flexresp %{buildroot}%{_sbindir}/%{name}-inline+flexresp
install %{name}-prelude %{buildroot}%{_sbindir}/%{name}-prelude
install %{name}-prelude+flexresp %{buildroot}%{_sbindir}/%{name}-prelude+flexresp
popd
}

install %{name}.8* %{buildroot}%{_mandir}/man8
perl -pi -e "s|var RULE_PATH ../rules|var RULE_PATH rules|" etc/%{name}.conf

install -m0644 etc/*.conf %{buildroot}%{_sysconfdir}/%{name}/
install -m0644 etc/*.config %{buildroot}%{_sysconfdir}/%{name}/
install -m0644 etc/*.map %{buildroot}%{_sysconfdir}/%{name}/

install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service

install -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -m0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

install -D -m755 %{SOURCE7} %{buildroot}%{_libexecdir}/snort-wrapper.sh
sed "s:libexecdir:%{_libexecdir}:" -i %{buildroot}%{_unitdir}/%{name}.service

# strip rpath
chrpath -d %{buildroot}%{_sbindir}/%{name}-*

# fix libexecdir
perl -pi -e "s|/usr/local/lib/snort_|%{_libdir}/%{name}/|g" %{buildroot}%{_sysconfdir}/%{name}/snort.conf

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
%{_sbindir}/%{name}-plain
%{_bindir}/u2boat
%{_bindir}/u2spewfoo
%{_mandir}/man8/%{name}.8*
%attr(0755,snort,snort) %dir /var/log/%{name}
%attr(0755,snort,snort) %dir /var/log/%{name}/empty
%attr(0755,snort,snort) %dir /var/run/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/rules
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/file_magic.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*.config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/threshold.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*.map
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0644,root,root) %{_unitdir}/%{name}.service
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/dynamicengine
%dir %{_libdir}/%{name}/dynamicpreprocessor
#%dir %{_libdir}/%{name}/dynamicrules
%dir %{_libdir}/%{name}/dynamic_output
%{_libdir}/%{name}/dynamicengine/libsf_engine.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_dce2_preproc.so
#attr(0755,root,root) %{_libdir}/%{name}/dynamicpreprocessor/libsf_dcerpc_preproc.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_dns_preproc.so
#%{_libdir}/%{name}/dynamicpreprocessor/lib_sfdynamic_preprocessor_example.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_ftptelnet_preproc.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_smtp_preproc.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_ssh_preproc.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_ssl_preproc.so
#%{_libdir}/%{name}/dynamicrules/lib_sfdynamic_example_rule.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_sdf_preproc.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_imap_preproc.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_pop_preproc.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_reputation_preproc.so
%{_libdir}/%{name}/dynamicpreprocessor/libsf_sip_preproc.so

%{_libdir}/%{name}/dynamicpreprocessor/libsf_dnp3_preproc.*
%{_libdir}/%{name}/dynamicpreprocessor/libsf_gtp_preproc.*
%{_libdir}/%{name}/dynamicpreprocessor/libsf_modbus_preproc.*
%{_libdir}/%{name}/dynamic_output/libsf_dynamic_output.*

%attr(0755,root,root) %{_libexecdir}/snort-wrapper.sh

%files plain+flexresp
%{_sbindir}/%{name}-plain+flexresp

%files mysql
#%doc schemas/create_mysql
%{_sbindir}/%{name}-mysql

%files mysql+flexresp
#%doc schemas/create_mysql
%{_sbindir}/%{name}-mysql+flexresp

%files postgresql
#%doc schemas/create_postgresql
%{_sbindir}/%{name}-postgresql

%files postgresql+flexresp
#%doc schemas/create_postgresql
%{_sbindir}/%{name}-postgresql+flexresp

%files bloat
%{_sbindir}/%{name}-bloat

%files inline
%{_sbindir}/%{name}-inline

%files inline+flexresp
%{_sbindir}/%{name}-inline+flexresp

%files prelude
%{_sbindir}/%{name}-prelude

%files prelude+flexresp
%{_sbindir}/%{name}-prelude+flexresp

%files devel
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/snort_output.pc
%{_libdir}/pkgconfig/snort.pc
%{_libdir}/pkgconfig/snort_preproc.pc
%dir %{_includedir}/%{name}/dynamic_preproc
%dir %{_includedir}/%{name}/dynamic_output/*.h
%{_includedir}/%{name}/dynamic_preproc/*.h

