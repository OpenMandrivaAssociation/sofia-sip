%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}
%define staticdevelname %mklibname -d -s %{name}

%define	name    sofia-sip
%define	version 1.12.6
%define	release %mkrel 3

Summary:	An open-source SIP User-Agent library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://sofia-sip.sourceforge.net/
Group:		Networking/Instant messaging
Source0:	http://downloads.sourceforge.net/sofia-sip/sofia-sip-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel
BuildRequires:	libopenssl-devel
BuildRequires:	pkgconfig

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

%package -n %{develname}
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n %{develname}
Headers of %{name} for development.

%package -n %{staticdevelname}
Summary:	Static development files for %{name}
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Provides:	%{libname_orig}-static-devel = %{version}-%{release}
Obsoletes:	%{libname}-static-devel

%description -n %{staticdevelname}
Static development files for %{name}

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
%{_bindir}/sip-dig
%{_bindir}/sip-options
%{_bindir}/stunc
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsofia-sip-ua.so.0
%{_libdir}/libsofia-sip-ua.so.0.5.0
%{_libdir}/libsofia-sip-ua-glib.so.3
%{_libdir}/libsofia-sip-ua-glib.so.3.0.0

%files -n %{develname}
%defattr(-,root,root)
%{_datadir}/sofia-sip/msg_parser.awk
%{_datadir}/sofia-sip/tag_dll.awk
%{_includedir}/sofia-sip-1.12
%{_libdir}/libsofia-sip-ua-glib.la
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/libsofia-sip-ua.la
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc
%{_libdir}/pkgconfig/sofia-sip-ua.pc

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/libsofia-sip-ua.a
%{_libdir}/libsofia-sip-ua-glib.a
