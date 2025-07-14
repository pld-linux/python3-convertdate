#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-convertdate.spec)

Summary:	Converts between Gregorian dates and other calendar systems
Summary(pl.UTF-8):	Konwersja między datami gregoriańskimi a innymi systemami kalendarza
Name:		python-convertdate
# keep 2.2.x here for python2 support
Version:	2.2.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/convertdate/
Source0:	https://files.pythonhosted.org/packages/source/c/convertdate/convertdate-%{version}.tar.gz
# Source0-md5:	ac845ba4edec63754594bfbd63447e0e
URL:		https://pypi.org/project/convertdate/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic,
ISO, Julian, Mayan and Persian.

%description -l pl.UTF-8
Konwersja między datami gregoriańskimi a innymi systemami kalendarzy -
w tym: baha'i, francuski republikański, hebrajski, indyjski narodowy,
islamski, ISO, juliański, Majów i perski.

%package -n python3-convertdate
Summary:	Converts between Gregorian dates and other calendar systems
Summary(pl.UTF-8):	Konwersja między datami gregoriańskimi a innymi systemami kalendarza
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-convertdate
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic,
ISO, Julian, Mayan and Persian.

%description -n python3-convertdate -l pl.UTF-8
Konwersja między datami gregoriańskimi a innymi systemami kalendarzy -
w tym: baha'i, francuski republikański, hebrajski, indyjski narodowy,
islamski, ISO, juliański, Majów i perski.

%prep
%setup -q -n convertdate-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.md
%{py_sitescriptdir}/convertdate
%{py_sitescriptdir}/convertdate-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-convertdate
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.md
%{py3_sitescriptdir}/convertdate
%{py3_sitescriptdir}/convertdate-%{version}-py*.egg-info
%endif
