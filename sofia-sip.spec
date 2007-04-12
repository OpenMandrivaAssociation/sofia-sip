%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

%define	name    sofia-sip
%define	version 1.11.7
%define	release %mkrel 2

Summary:	An open-source SIP  User-Agent library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://sofia-sip.sourceforge.net/
Group:		Networking/Instant messaging
Source0:	http://ovh.dl.sourceforge.net/sourceforge/sofia-sip/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  pkgconfig

%description

Sofia-SIP is an open-source SIP  User-Agent library, 
compliant with the IETF RFC3261 specification (see the 
feature table). It can be used as a building block for 
SIP client software for uses such as VoIP, IM, and many 
other real-time and person-to-person communication services. 
The primary target platform for Sofia-SIP is GNU/Linux. 
Sofia-SIP is based on a SIP stack developed at the Nokia 
Research Center. Sofia-SIP is licensed under the LGPL.

%package -n %{libname}
Summary:	Sophia-sip library
Group:		Graphical desktop/KDE
Provides:	%{libname_orig} = %{version}-%{release}
Requires:	%name = %version-%release

%description -n %{libname}
Library for %{name}

%package -n %{libname}-devel
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description -n %{libname}-devel
Headers of %{name} for development.

%prep
%setup -q

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std}


%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig


%files -n %{name}
%defattr(-,root,root)
%{_bindir}/addrinfo
%{_bindir}/localinfo
%{_bindir}/sip-date
%{_bindir}/sip-options

%{_mandir}/man1/addrinfo.1.bz2
%{_mandir}/man1/localinfo.1.bz2
%{_mandir}/man1/sip-date.1.bz2
%{_mandir}/man1/sip-options.1.bz2

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsofia-sip-ua.so.0
%{_libdir}/libsofia-sip-ua.so.0.0.0
%{_libdir}/libsofia-sip-ua-glib.so.0
%{_libdir}/libsofia-sip-ua-glib.so.0.0.0

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/sofia-sip-1.11/sofia-sip/
%{_libdir}/libsofia-sip-ua-glib.a
%{_libdir}/libsofia-sip-ua-glib.la
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/libsofia-sip-ua.a
%{_libdir}/libsofia-sip-ua.la
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc
%{_libdir}/pkgconfig/sofia-sip-ua.pc
%{_libdir}/sofia/msg_parser.awk
%{_libdir}/sofia/tag_dll.awk
%{_datadir}/aclocal/sac-general.m4
%{_datadir}/aclocal/sac-su.m4

