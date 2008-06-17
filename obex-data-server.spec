Name:		obex-data-server
Version:	0.3
Release:	%mkrel 2
Summary:	D-Bus service for Obex access

Group:		System/Servers
License:	GPLv2+
Source0:	http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
Url:		http://tadas.dailyda.com/blog
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	dbus-glib-devel
BuildRequires:	bluez-devel
BuildRequires:	openobex-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool

%description
obex-data-server is a D-Bus service to allow sending and receiving files
using the ObexFTP and Obex Push protocols, common on mobile phones and
other Bluetooth-equipped devices.

%prep
%setup -q

%build
%configure2_5x
%make

cat << EOF > README
Bug tracking system is at:
http://bugs.muiline.com/view_all_bug_page.php

Web page is at:
http://tadas.dailyda.com/blog/

SVN tree:
svn://svn.muiline.com/obex-data-server/trunk/

SVN browsing:
http://svn.muiline.com/cgi-bin/viewvc.cgi/obex-data-server/trunk/

EOF

%install
rm -rf $RPM_BUILD_ROOT
# FIXME files missing: http://bugs.muiline.com/view.php?id=42
#chmod a-x test/*.py
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING dbus-api.txt
#test/ods-dbus-test.c test/ods-server-test.py test/ods-session-test.py
%{_bindir}/obex-data-server
%{_datadir}/dbus-1/services/obex-data-server.service
