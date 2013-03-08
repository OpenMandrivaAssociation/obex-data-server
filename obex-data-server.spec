Name:		obex-data-server
Version:	0.4.6
Release:	5
Summary:	D-Bus service for Obex access

Group:		System/Servers
License:	GPLv2+
Source0:	http://tadas.dailyda.com/software/%{name}-%{version}.tar.gz
Url:		http://tadas.dailyda.com/blog

BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(openobex)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	libtool

%description
obex-data-server is a D-Bus service to allow sending and receiving files
using the ObexFTP and Obex Push protocols, common on mobile phones and
other Bluetooth-equipped devices.

%prep
%setup -q

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
#test/ods-dbus-test.c test/ods-server-test.py test/ods-session-test.py
%{_bindir}/obex-data-server
%{_datadir}/dbus-1/services/obex-data-server.service
%config %{_sysconfdir}/obex-data-server/*.xml
%{_mandir}/man1/obex-data-server.1.*



%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 0.4.6-1mdv2011.0
+ Revision: 659080
- update to new version 0.4.6

* Wed Dec 02 2009 Götz Waschk <waschk@mandriva.org> 0.4.5-1mdv2011.0
+ Revision: 472594
- update to new version 0.4.5

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.4-2mdv2010.0
+ Revision: 426263
- rebuild

* Wed Feb 18 2009 Frederic Crozat <fcrozat@mandriva.com> 0.4.4-1mdv2009.1
+ Revision: 342570
- Release 0.4.4
- Enable libusb and BIP through gdk-pixbuf

* Sun Jan 04 2009 Guillaume Bedot <littletux@mandriva.org> 0.4.2-1mdv2009.1
+ Revision: 324491
- New release 0.4.2

* Tue Aug 12 2008 Emmanuel Andry <eandry@mandriva.org> 0.3.2-1mdv2009.0
+ Revision: 271129
- New version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.3-2mdv2009.0
+ Revision: 223355
- rebuild

* Sun Feb 24 2008 Emmanuel Andry <eandry@mandriva.org> 0.3-1mdv2008.1
+ Revision: 174422
- New version

* Tue Feb 19 2008 Frederic Crozat <fcrozat@mandriva.com> 0.2-1mdv2008.1
+ Revision: 173019
- Release 0.2

* Mon Feb 11 2008 Frederic Crozat <fcrozat@mandriva.com> 0.1-1mdv2008.1
+ Revision: 165153
- import obex-data-server


