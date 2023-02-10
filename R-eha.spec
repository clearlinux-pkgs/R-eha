#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-eha
Version  : 2.10.3
Release  : 46
URL      : https://cran.r-project.org/src/contrib/eha_2.10.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/eha_2.10.3.tar.gz
Summary  : Event History Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-eha-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
right censoring for common families of distributions, piecewise constant 
        hazards, and discrete models. Parametric accelerated failure time models
        for left truncated and right censored data. Proportional hazards
        models for tabular and register data. Sampling of risk sets in Cox 
        regression, selections in the Lexis diagram, bootstrapping.

%package lib
Summary: lib components for the R-eha package.
Group: Libraries

%description lib
lib components for the R-eha package.


%prep
%setup -q -n eha
cd %{_builddir}/eha

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676048184

%install
export SOURCE_DATE_EPOCH=1676048184
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/eha/CITATION
/usr/lib64/R/library/eha/DESCRIPTION
/usr/lib64/R/library/eha/INDEX
/usr/lib64/R/library/eha/Meta/Rd.rds
/usr/lib64/R/library/eha/Meta/data.rds
/usr/lib64/R/library/eha/Meta/features.rds
/usr/lib64/R/library/eha/Meta/hsearch.rds
/usr/lib64/R/library/eha/Meta/links.rds
/usr/lib64/R/library/eha/Meta/nsInfo.rds
/usr/lib64/R/library/eha/Meta/package.rds
/usr/lib64/R/library/eha/Meta/vignette.rds
/usr/lib64/R/library/eha/NAMESPACE
/usr/lib64/R/library/eha/NEWS.md
/usr/lib64/R/library/eha/R/eha
/usr/lib64/R/library/eha/R/eha.rdb
/usr/lib64/R/library/eha/R/eha.rdx
/usr/lib64/R/library/eha/data/Rdata.rdb
/usr/lib64/R/library/eha/data/Rdata.rds
/usr/lib64/R/library/eha/data/Rdata.rdx
/usr/lib64/R/library/eha/doc/eha.R
/usr/lib64/R/library/eha/doc/eha.Rmd
/usr/lib64/R/library/eha/doc/eha.html
/usr/lib64/R/library/eha/doc/gompertz.R
/usr/lib64/R/library/eha/doc/gompertz.Rmd
/usr/lib64/R/library/eha/doc/gompertz.html
/usr/lib64/R/library/eha/doc/index.html
/usr/lib64/R/library/eha/doc/parametric.R
/usr/lib64/R/library/eha/doc/parametric.Rmd
/usr/lib64/R/library/eha/doc/parametric.html
/usr/lib64/R/library/eha/doc/parametric1.Rnw
/usr/lib64/R/library/eha/doc/parametric1.pdf
/usr/lib64/R/library/eha/doc/tpchreg.R
/usr/lib64/R/library/eha/doc/tpchreg.Rmd
/usr/lib64/R/library/eha/doc/tpchreg.html
/usr/lib64/R/library/eha/help/AnIndex
/usr/lib64/R/library/eha/help/aliases.rds
/usr/lib64/R/library/eha/help/eha.rdb
/usr/lib64/R/library/eha/help/eha.rdx
/usr/lib64/R/library/eha/help/paths.rds
/usr/lib64/R/library/eha/html/00Index.html
/usr/lib64/R/library/eha/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/eha/libs/eha.so
/usr/lib64/R/library/eha/libs/eha.so.avx2
/usr/lib64/R/library/eha/libs/eha.so.avx512
