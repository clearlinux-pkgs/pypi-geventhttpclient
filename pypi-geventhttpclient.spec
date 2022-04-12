#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-geventhttpclient
Version  : 1.5.3
Release  : 2
URL      : https://files.pythonhosted.org/packages/7e/52/f799b56882eb2730c09c281bcc7f71607963853302ce27f3c565aa736bc8/geventhttpclient-1.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/7e/52/f799b56882eb2730c09c281bcc7f71607963853302ce27f3c565aa736bc8/geventhttpclient-1.5.3.tar.gz
Summary  : http client library for gevent
Group    : Development/Tools
License  : MIT
Requires: pypi-geventhttpclient-license = %{version}-%{release}
Requires: pypi-geventhttpclient-python = %{version}-%{release}
Requires: pypi-geventhttpclient-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(brotli)
BuildRequires : pypi(certifi)
BuildRequires : pypi(gevent)
BuildRequires : pypi(six)

%description
# geventhttpclient
[![Build Status](https://travis-ci.org/gwik/geventhttpclient.svg?branch=master)](https://travis-ci.org/gwik/geventhttpclient)

%package license
Summary: license components for the pypi-geventhttpclient package.
Group: Default

%description license
license components for the pypi-geventhttpclient package.


%package python
Summary: python components for the pypi-geventhttpclient package.
Group: Default
Requires: pypi-geventhttpclient-python3 = %{version}-%{release}

%description python
python components for the pypi-geventhttpclient package.


%package python3
Summary: python3 components for the pypi-geventhttpclient package.
Group: Default
Requires: python3-core
Provides: pypi(geventhttpclient)
Requires: pypi(brotli)
Requires: pypi(certifi)
Requires: pypi(gevent)
Requires: pypi(six)

%description python3
python3 components for the pypi-geventhttpclient package.


%prep
%setup -q -n geventhttpclient-1.5.3
cd %{_builddir}/geventhttpclient-1.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649751112
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-geventhttpclient
cp %{_builddir}/geventhttpclient-1.5.3/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-geventhttpclient/a6751b809f6837cdb0240746a1ea2b328a385e8a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-geventhttpclient/a6751b809f6837cdb0240746a1ea2b328a385e8a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
