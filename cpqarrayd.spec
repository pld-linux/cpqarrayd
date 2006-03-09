# TODO: init script (provided one isn't LSB-compliant)
Summary:	Cpqarrayd - SmartArray controllers monitoring
Summary(pl):	Cpqarrayd - monitorowanie kontrolerów SmartArray
Name:		cpqarrayd
Version:	2.2
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.strocamp.net/opensource/compaq/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	d287d1ad9317443063aff1098f7bc4f4
Patch0:		%{name}-headers.patch
URL:		http://www.strocamp.net/opensource/cpqarrayd.php
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	net-snmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cpqarrayd monitors SmartArray controllers for you and notifies by
sending SNMP traps and via syslog.

%description -l pl
Cpqarrayd monitoruje kontrolery SmartArray i powiadamia przez
wysy³anie pu³apek SNMP oraz sysloga.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/cpqarrayd
%{_mandir}/man1/cpqarrayd.1*
