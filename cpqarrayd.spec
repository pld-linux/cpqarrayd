Summary:	Cpqarrayd - SmartArray controllers monitoring
Summary(pl):	Cpqarrayd - monitorowanie kontrolerów SmartArray
Name:		cpqarrayd
Version:	2.0
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://starbreeze.knoware.nl/~hugo/compaq/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	c53247d26e769d154a810a498dd0322c
URL:		http://starbreeze.knoware.nl/~spark/compaq/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cpqarrayd monitors SmartArray controllers for you and notifies by
sending SNMP traps and via syslog.

%description -l pl
Cpqarrayd monitoruje kontrolery SmartArray i powiadamia przez
wysy³anie pu³apek SNMP oraz sysloga.

%prep
%setup -q

%build
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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
