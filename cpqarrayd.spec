Summary:	Cpqarrayd - SmartArray controllers monitoring
Summary(pl.UTF-8):   Cpqarrayd - monitorowanie kontrolerów SmartArray
Name:		cpqarrayd
Version:	2.2
Release:	0.4
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.strocamp.net/opensource/compaq/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	d287d1ad9317443063aff1098f7bc4f4
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-headers.patch
URL:		http://www.strocamp.net/opensource/cpqarrayd.php
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	net-snmp-devel
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cpqarrayd monitors SmartArray controllers for you and notifies by
sending SNMP traps and via syslog.

%description -l pl.UTF-8
Cpqarrayd monitoruje kontrolery SmartArray i powiadamia przez
wysyłanie pułapek SNMP oraz sysloga.

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
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/cpqarrayd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/cpqarrayd

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add cpqarrayd
%service cpqarrayd restart "Compaq RAID Array Monitor"

%preun
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del cpqarrayd
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/cpqarrayd
%{_mandir}/man1/cpqarrayd.1*
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/cpqarrayd
%attr(754,root,root) /etc/rc.d/init.d/cpqarrayd
