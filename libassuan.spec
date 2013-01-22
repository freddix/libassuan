Summary:	IPC library for non-persistent servers
Name:		libassuan
Version:	2.0.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/libassuan/%{name}-%{version}.tar.bz2
# Source0-md5:	179d1918325fdb928c7bd90b8a514fc7
URL:		http://www.gnupg.org/related_software/libassuan/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgpg-error-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libassuan is a small library implementing the so-called Assuan
protocol. This protocol is used for IPC between most newer GnuPG
components. Both, server and client side functions are provided.

%package devel
Summary:	Header files for assuan library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for assuan library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%post	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libassuan.so.0
%attr(755,root,root) %{_libdir}/libassuan.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libassuan-config
%attr(755,root,root) %{_libdir}/libassuan.so
%{_libdir}/libassuan.la
%{_includedir}/assuan.h
%{_aclocaldir}/libassuan.m4
%{_infodir}/assuan.info*
