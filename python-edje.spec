Summary:	Python bindings for Edje library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Edje
Name:		python-edje
Version:	1.7.0
Release:	10
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	1e0d7a4a4504298caaad0cee476e4edb
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	edje-devel >= 1.7.0
BuildRequires:	eina-devel >= 1.7.0
BuildRequires:	epydoc
BuildRequires:	evas-devel >= 1.7.0
BuildRequires:	python-Cython >= 0.15.1
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-evas >= 1.7.0
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	edje-libs >= 1.7.0
Requires:	eina >= 1.7.0
Requires:	evas >= 1.7.0
Requires:	python-evas >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Edje library.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki Edje.

%package devel
Summary:	Python bindings for Edje library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Edje - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	edje-devel >= 1.7.0
Requires:	eina-devel >= 1.7.0
Requires:	evas-devel >= 1.7.0
Requires:	python-evas-devel >= 1.7.0

%description devel
Python bindings for Edje library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki Edje - pliki programistyczne.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/edje/c_edje.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/edje/edit/c_edit.la

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitedir}/edje
%attr(755,root,root) %{py_sitedir}/edje/c_edje.so
%dir %{py_sitedir}/edje/edit
%attr(755,root,root) %{py_sitedir}/edje/edit/c_edit.so
%{py_sitedir}/edje/*.py[co]
%{py_sitedir}/edje/edit/__init__.py[co]
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_includedir}/python-edje
%{_pkgconfigdir}/python-edje.pc
