#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libnumbertext
Version  : 1.0.5
Release  : 4
URL      : https://github.com/Numbertext/libnumbertext/releases/download/1.0.5/libnumbertext-1.0.5.tar.xz
Source0  : https://github.com/Numbertext/libnumbertext/releases/download/1.0.5/libnumbertext-1.0.5.tar.xz
Summary  : Library implementing Soros based Number to Number Name conversion
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libnumbertext-bin = %{version}-%{release}
Requires: libnumbertext-data = %{version}-%{release}
Requires: libnumbertext-lib = %{version}-%{release}
Requires: libnumbertext-license = %{version}-%{release}

%description
# Soros interpreters for C++11, Java, JavaScript and Python
[![Build Status](https://travis-ci.org/Numbertext/libnumbertext.png?branch=master)](https://travis-ci.org/Numbertext/libnumbertext)

%package bin
Summary: bin components for the libnumbertext package.
Group: Binaries
Requires: libnumbertext-data = %{version}-%{release}
Requires: libnumbertext-license = %{version}-%{release}

%description bin
bin components for the libnumbertext package.


%package data
Summary: data components for the libnumbertext package.
Group: Data

%description data
data components for the libnumbertext package.


%package dev
Summary: dev components for the libnumbertext package.
Group: Development
Requires: libnumbertext-lib = %{version}-%{release}
Requires: libnumbertext-bin = %{version}-%{release}
Requires: libnumbertext-data = %{version}-%{release}
Provides: libnumbertext-devel = %{version}-%{release}
Requires: libnumbertext = %{version}-%{release}

%description dev
dev components for the libnumbertext package.


%package lib
Summary: lib components for the libnumbertext package.
Group: Libraries
Requires: libnumbertext-data = %{version}-%{release}
Requires: libnumbertext-license = %{version}-%{release}

%description lib
lib components for the libnumbertext package.


%package license
Summary: license components for the libnumbertext package.
Group: Default

%description license
license components for the libnumbertext package.


%prep
%setup -q -n libnumbertext-1.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570212695
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1570212695
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libnumbertext
cp COPYING %{buildroot}/usr/share/package-licenses/libnumbertext/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/spellout

%files data
%defattr(-,root,root,-)
/usr/share/libnumbertext/Hung.sor
/usr/share/libnumbertext/Roman.sor
/usr/share/libnumbertext/Suzhou.sor
/usr/share/libnumbertext/af.sor
/usr/share/libnumbertext/bg.sor
/usr/share/libnumbertext/ca.sor
/usr/share/libnumbertext/cs.sor
/usr/share/libnumbertext/da.sor
/usr/share/libnumbertext/de.sor
/usr/share/libnumbertext/el.sor
/usr/share/libnumbertext/en.sor
/usr/share/libnumbertext/eo.sor
/usr/share/libnumbertext/es.sor
/usr/share/libnumbertext/et.sor
/usr/share/libnumbertext/fi.sor
/usr/share/libnumbertext/fr.sor
/usr/share/libnumbertext/gl.sor
/usr/share/libnumbertext/he.sor
/usr/share/libnumbertext/hr.sor
/usr/share/libnumbertext/hu.sor
/usr/share/libnumbertext/id.sor
/usr/share/libnumbertext/is.sor
/usr/share/libnumbertext/it.sor
/usr/share/libnumbertext/ja.sor
/usr/share/libnumbertext/ko.sor
/usr/share/libnumbertext/lb.sor
/usr/share/libnumbertext/lt.sor
/usr/share/libnumbertext/lv.sor
/usr/share/libnumbertext/ms.sor
/usr/share/libnumbertext/nl.sor
/usr/share/libnumbertext/no.sor
/usr/share/libnumbertext/pl.sor
/usr/share/libnumbertext/pt.sor
/usr/share/libnumbertext/ro.sor
/usr/share/libnumbertext/ru.sor
/usr/share/libnumbertext/sh.sor
/usr/share/libnumbertext/sl.sor
/usr/share/libnumbertext/sq.sor
/usr/share/libnumbertext/sr.sor
/usr/share/libnumbertext/sv.sor
/usr/share/libnumbertext/th.sor
/usr/share/libnumbertext/tr.sor
/usr/share/libnumbertext/uk.sor
/usr/share/libnumbertext/vi.sor
/usr/share/libnumbertext/zh.sor

%files dev
%defattr(-,root,root,-)
/usr/include/libnumbertext/Numbertext.hxx
/usr/include/libnumbertext/Soros.hxx
/usr/include/libnumbertext/numbertext-version.h
/usr/lib64/libnumbertext-1.0.so
/usr/lib64/pkgconfig/libnumbertext.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnumbertext-1.0.so.0
/usr/lib64/libnumbertext-1.0.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnumbertext/COPYING
