Name:           vlmcsd
Version:        svn1111
Release:        1%{?dist}
Summary:        A fully Microsoft compatible KMS server

License:        Unknown
URL:            https://github.com/Wind4/vlmcsd
Source0:        https://github.com/Wind4/vlmcsd/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         vlmcsd-svn1111-build.patch

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
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system
cp $RPM_SOURCE_DIR/vlmcsd.service $RPM_BUILD_ROOT/lib/systemd/system


%files
/usr/bin/vlmcs
/usr/bin/vlmcsd
/etc/vlmcsd/vlmcsd.ini
/etc/vlmcsd/vlmcsd.kmd
/usr/share/man/man1/vlmcs.1.gz
/usr/share/man/man5/vlmcsd.ini.5.gz
/usr/share/man/man7/vlmcsd.7.gz
/usr/share/man/man8/vlmcsd.8.gz
/lib/systemd/system/vlmcsd.service



%changelog
* Sun Sep  2 2018 - svn1111-1
- Support for Windows Professional Workstation and Windows Professional Workstation N (aka Win 10 Pro for Advanced PCs)
- Some internal code optimizations
- Updated Visual C++ Platform Toolset to v141_xp
- Updated gcc to 6.3.0 on many platforms
- Removed 32-bit cygwin OpenSSL binary because 64-bit Cygwin no longer features 32-bit OpenSSL headers and libraries
- Changed Windows build script to use MSBuild 2017
- Updated groff formatting options for ASCII (TXT) man files
- Added support for Enterprise G and Enterprise GN (Windows China Government Edition)
- Added suffix _unused to some local parameters to indicate that MSVC compiler warnings can be ignored
- Renamed some local parameters to avoid compiler warnings
- Added casts to reduce MSVC compiler warnings
- Fixed a bug in memory allocation, if .kmd file has less CSVLKs than built-in minimum