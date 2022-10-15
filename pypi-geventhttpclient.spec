#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-geventhttpclient
Version  : 2.0.8
Release  : 14
URL      : https://files.pythonhosted.org/packages/bf/05/93c4e1e525c15890a6222833a31a1abb5df987d6d16e0dadb395796a19b5/geventhttpclient-2.0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/05/93c4e1e525c15890a6222833a31a1abb5df987d6d16e0dadb395796a19b5/geventhttpclient-2.0.8.tar.gz
Summary  : http client library for gevent
Group    : Development/Tools
License  : MIT
Requires: pypi-geventhttpclient-filemap = %{version}-%{release}
Requires: pypi-geventhttpclient-lib = %{version}-%{release}
Requires: pypi-geventhttpclient-license = %{version}-%{release}
Requires: pypi-geventhttpclient-python = %{version}-%{release}
Requires: pypi-geventhttpclient-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(brotli)
BuildRequires : pypi(certifi)
BuildRequires : pypi(gevent)
BuildRequires : pypi(six)
BuildRequires : python3-dev

%description
# geventhttpclient
[![Build Status](https://travis-ci.org/gwik/geventhttpclient.svg?branch=master)](https://travis-ci.org/gwik/geventhttpclient)

%package filemap
Summary: filemap components for the pypi-geventhttpclient package.
Group: Default

%description filemap
filemap components for the pypi-geventhttpclient package.


%package lib
Summary: lib components for the pypi-geventhttpclient package.
Group: Libraries
Requires: pypi-geventhttpclient-license = %{version}-%{release}
Requires: pypi-geventhttpclient-filemap = %{version}-%{release}

%description lib
lib components for the pypi-geventhttpclient package.


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
Requires: pypi-geventhttpclient-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(geventhttpclient)
Requires: pypi(brotli)
Requires: pypi(certifi)
Requires: pypi(gevent)
Requires: pypi(six)

%description python3
python3 components for the pypi-geventhttpclient package.


%prep
%setup -q -n geventhttpclient-2.0.8
cd %{_builddir}/geventhttpclient-2.0.8
pushd ..
cp -a geventhttpclient-2.0.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665850094
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-geventhttpclient
cp %{_builddir}/geventhttpclient-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-geventhttpclient/5413311e63bb2579dda428f8b1137cdce381cf27 || :
cp %{_builddir}/geventhttpclient-%{version}/llhttp/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-geventhttpclient/f7eb77642fea2d18bc5b53d361802ca0fb698b3e || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-geventhttpclient

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-geventhttpclient/5413311e63bb2579dda428f8b1137cdce381cf27
/usr/share/package-licenses/pypi-geventhttpclient/f7eb77642fea2d18bc5b53d361802ca0fb698b3e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
