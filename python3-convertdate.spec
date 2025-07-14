Summary:	Converts between Gregorian dates and other calendar systems
Summary(pl.UTF-8):	Konwersja między datami gregoriańskimi a innymi systemami kalendarza
Name:		python3-convertdate
Version:	2.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/convertdate/
Source0:	https://files.pythonhosted.org/packages/source/c/convertdate/convertdate-%{version}.tar.gz
# Source0-md5:	320965d9ae24060c385110606c61d040
URL:		https://pypi.org/project/convertdate/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:60.5.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
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

%prep
%setup -q -n convertdate-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

# python code (censusgeocode.__main__) not present
%{__rm} $RPM_BUILD_ROOT%{_bindir}/censusgeocode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/convertdate
%{py3_sitescriptdir}/convertdate-%{version}-py*.egg-info
