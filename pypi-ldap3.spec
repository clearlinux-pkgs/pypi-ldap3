#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ldap3
Version  : 2.9.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/43/ac/96bd5464e3edbc61595d0d69989f5d9969ae411866427b2500a8e5b812c0/ldap3-2.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/ac/96bd5464e3edbc61595d0d69989f5d9969ae411866427b2500a8e5b812c0/ldap3-2.9.1.tar.gz
Summary  : A strictly RFC 4510 conforming LDAP V3 pure Python client library
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: pypi-ldap3-license = %{version}-%{release}
Requires: pypi-ldap3-python = %{version}-%{release}
Requires: pypi-ldap3-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyasn1)

%description
=====

%package license
Summary: license components for the pypi-ldap3 package.
Group: Default

%description license
license components for the pypi-ldap3 package.


%package python
Summary: python components for the pypi-ldap3 package.
Group: Default
Requires: pypi-ldap3-python3 = %{version}-%{release}

%description python
python components for the pypi-ldap3 package.


%package python3
Summary: python3 components for the pypi-ldap3 package.
Group: Default
Requires: python3-core
Provides: pypi(ldap3)
Requires: pypi(pyasn1)

%description python3
python3 components for the pypi-ldap3 package.


%prep
%setup -q -n ldap3-2.9.1
cd %{_builddir}/ldap3-2.9.1
pushd ..
cp -a ldap3-2.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656395666
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ldap3
cp %{_builddir}/ldap3-2.9.1/COPYING.LESSER.txt %{buildroot}/usr/share/package-licenses/pypi-ldap3/93a34ec120cdc2f9216d2217ffb32908fd9e3d4b
cp %{_builddir}/ldap3-2.9.1/COPYING.txt %{buildroot}/usr/share/package-licenses/pypi-ldap3/52be821be7d06dde87d7805331066d1af6f3f9f8
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ldap3/52be821be7d06dde87d7805331066d1af6f3f9f8
/usr/share/package-licenses/pypi-ldap3/93a34ec120cdc2f9216d2217ffb32908fd9e3d4b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
