#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Differences
Summary:	Test::Differences - Test strings and data structures and show differences if not ok
Summary(pl):	Test::Differences - kontrola ³añcuchów i struktur danych z pokazywaniem ró¿nic
Name:		perl-Test-Differences
Version:	0.46
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Text-Diff
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When the code you're testing returns multiple lines or records and
they're just plain wrong, sometimes an equivalent to the Unix diff
utility is just what's needed.

%description -l pl
Je¶li testowany kod zwraca wiele linii lub rekordów, które s±
niepoprawne, czasem przydatny jest odpowiednik uniksowego narzêdzia
diff. 

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
