Name:           libnl1
Summary:        Convenience library for kernel netlink sockets
Group:          Development/Libraries/Other
License:        LGPL-2.1
Version:        1.1
Release:        1
Url:            http://people.suug.ch/~tgr/libnl/
Source:         http://people.suug.ch/~tgr/libnl/files/libnl-%version.tar.bz2
Source99:       baselibs.conf
BuildRequires:  pkgconfig >= 0.23

%description
This package contains a convenience library to simplify using the Linux
kernels netlink sockets interface for network manipulation.


%package devel
License:        LGPL-2.1+
Summary:        Convenience library for kernel netlink sockets
Group:          Development/Libraries/Other
Requires:       %name = %version-%release
Provides:       libnl-devel = %release-%version

%description devel
This package contains a convenience library to simplify using the Linux
kernels netlink sockets interface for network manipulation.

%prep
%setup -q -n libnl-%version

%build
%configure \
    --prefix=%_prefix \
    --libdir=/%_lib \
    --includedir=%_includedir
make %{?_smp_mflags}

%install
%makeinstall
mkdir -p %buildroot/%_libdir/pkgconfig
mv %buildroot/%_lib/pkgconfig/* %buildroot/%_libdir/pkgconfig

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/%_lib/libnl*.so.*
%doc COPYING 

%files devel
%defattr(-,root,root,0755)
%_includedir/netlink/
/%_lib/libnl*.so
%_libdir/pkgconfig/*.pc

%changelog
