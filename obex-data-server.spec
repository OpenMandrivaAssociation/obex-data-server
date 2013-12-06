Summary:	D-Bus service for Obex access
Name:		obex-data-server
Version:	0.4.6
Release:	12
Group:		System/Servers
License:	GPLv2+
Url:		http://tadas.dailyda.com/blog
Source0:	http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
Patch0:		obex-data-server-0.4.6-build-fixes-1.patch

BuildRequires:	libtool
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(openobex)

%description
obex-data-server is a D-Bus service to allow sending and receiving files
using the ObexFTP and Obex Push protocols, common on mobile phones and
other Bluetooth-equipped devices.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --enable-bip=gdk-pixbuf
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
# FIXME files missing: http://bugs.muiline.com/view.php?id=42
#chmod a-x test/*.py
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README COPYING dbus-api.txt
%config %{_sysconfdir}/obex-data-server/*.xml
#test/ods-dbus-test.c test/ods-server-test.py test/ods-session-test.py
%{_bindir}/obex-data-server
%{_datadir}/dbus-1/services/obex-data-server.service
%{_mandir}/man1/obex-data-server.1.*

