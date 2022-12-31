%define _disable_ld_no_undefined 1

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

Summary:	An open-source SIP User-Agent library
Name:		sofia-sip
Version:	1.13.11
Release:	1
License:	LGPLv2+
Url:		http://sofia-sip.sourceforge.net/
Group:		Networking/Instant messaging
Source0:        https://github.com/freeswitch/%{name}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  libtool

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


%prep
%autosetup -p1

%build
#export CC=gcc
#export CXX=g++
sh autogen.sh
%configure --disable-rpath --disable-static --without-doxygen --disable-stun
%make_build     

%install
%make_install

%files -n %{name}
%{_bindir}/addrinfo
%{_bindir}/localinfo
%{_bindir}/sip-date
%{_bindir}/sip-dig
%{_bindir}/sip-options
#{_bindir}/stunc
#{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libsofia-sip-ua.so.0
%{_libdir}/libsofia-sip-ua.so.0.6.0
%{_libdir}/libsofia-sip-ua-glib.so.3
%{_libdir}/libsofia-sip-ua-glib.so.3.0.0

%files -n %{develname}
%{_datadir}/sofia-sip/msg_parser.awk
%{_datadir}/sofia-sip/tag_dll.awk
%{_includedir}/sofia-sip-1.13
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc
%{_libdir}/pkgconfig/sofia-sip-ua.pc

