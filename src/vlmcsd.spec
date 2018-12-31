Name:           vlmcsd
Version:        svn1112
Release:        1%{?dist}
Summary:        A fully Microsoft compatible KMS server

License:        Unknown
URL:            https://github.com/Wind4/vlmcsd
Source0:        https://github.com/Wind4/vlmcsd/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vlmcsd.service
Patch0:         vlmcsd-svn1112-build.patch

BuildRequires: systemd-devel
Requires(pre): /usr/sbin/useradd
Requires(pre): /usr/sbin/groupadd
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): systemd-units

%description
vlmcsd is a fully Microsoft compatible KMS server that provides product
activation services to clients. It is meant as  a  drop-in  replacement
for  a Microsoft KMS server (Windows computer with KMS key entered). It
currently supports KMS protocol versions 4, 5 and 6.
Although vlmcsd does neither require an activation key nor a payment to
anyone,  it  is not meant to run illegal copies of Windows. Its purpose
is to ensure that owners of legal copies can use their software without
restrictions,  e.g.  if  you buy a new computer or motherboard and your
key will be refused activation from Microsoft servers due  to  hardware
changes.

%prep
%autosetup

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 $RPM_SOURCE_DIR/vlmcsd.service $RPM_BUILD_ROOT%{_unitdir}/vlmcsd.service

%pre
# Add the "vlmcsd" group and user
/usr/sbin/groupadd -r vlmcsd 2> /dev/null || :
/usr/sbin/useradd -c "vlmcsd" -g vlmcsd -s /sbin/nologin -r vlmcsd -M 2> /dev/null || :

%post
%systemd_post vlmcsd.service

%preun
%systemd_preun vlmcsd.service

%postun
%systemd_postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/vlmcs
/usr/bin/vlmcsd
/etc/vlmcsd/vlmcsd.ini
/etc/vlmcsd/vlmcsd.kmd
/usr/share/man/man1/vlmcs.1.gz
/usr/share/man/man5/vlmcsd.ini.5.gz
/usr/share/man/man7/vlmcsd.7.gz
/usr/share/man/man8/vlmcsd.8.gz
%{_unitdir}/vlmcsd.service

%changelog
* Mon Dec 31 2018 - svn1112-1
- Support for Windows 10 1809, Windows Server 2019 and Office 2019 built-in
- vlmcsd now has fully configurable CSVLKs that allow a custom EPID and HwId for each CSVLK to be specified.
- Options -w, -0, -3, -6 and -G have been removed in favor for the new -a option.
- The -H option has been redefined: It now allows a fixed host build to be specified in random EPIDs
- New INI file directive HostBuild= that does the same as the new -H option.
- Fix using configuration file vlmcsd.ini in systemd unit.
- Run under vlmcsd user and group.