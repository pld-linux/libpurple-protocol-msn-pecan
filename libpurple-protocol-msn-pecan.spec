#
# Conditional build:
%bcond_without	tests		# build without tests

%define		realname msn-pecan
Summary:	Alternative MSN protocol plugin for libpurple
Name:		libpurple-protocol-%{realname}
Version:	0.1.2
Release:	1
License:	GPL v2+
Group:		Applications/Networking
URL:		http://code.google.com/p/msn-pecan/
Source0:	http://msn-pecan.googlecode.com/files/%{realname}-%{version}.tar.bz2
# Source0-md5:	e426455fa45b98edb86fb0d801eccdf9
%{?with_tests:BuildRequires:	check-devel >= 0.9.6}
BuildRequires:	gettext-devel
BuildRequires:	libpurple-devel
BuildRequires:	pkgconfig
Provides:	libpurple-protocol
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The project aims to have a much faster development process, low
barrier for contributions, and close contact with the user-base.

Compared to Pidgin's official MSN plug-in:
 - Faster log-in
 - Fewer connection issues
 - Fewer crashes
 - Experimental direct connection support (fast file transfers)
 - Server-side storage for display names (private alias)
 - Support for handwritten messages (read-only)
 - Support for voice clips (receive-only)
 - Support for Plus! sounds (receive-only)
 - Option to hide Plus! tags

Other features:
 - Support for personal status messages
 - Support for offline messaging (read-only)
 - Send custom emoticons (Pidgin >= 2.5)

%prep
%setup -q -n %{realname}-%{version}

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	Q=""

%install
rm -rf $RPM_BUILD_ROOT
install -Dp libmsn-pecan.so $RPM_BUILD_ROOT%{_libdir}/purple-2/libmsn-pecan.so
%{__make} install_locales \
	Q="" \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang libmsn-pecan

%if %{with tests}
%{__make} -C tests clean
%{__make} -C tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f libmsn-pecan.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO README pidgin-copyright ChangeLog
%attr(755,root,root) %{_libdir}/purple-2/libmsn-pecan.so
