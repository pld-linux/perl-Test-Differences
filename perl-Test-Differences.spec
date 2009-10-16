#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Differences
Summary:	Test::Differences - test strings and data structures and show differences if not ok
Summary(pl.UTF-8):	Test::Differences - kontrola łańcuchów i struktur danych z pokazywaniem różnic
Name:		perl-Test-Differences
Version:	0.4801
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2df59051b3c4276f9bb3f26fcf01ae67
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Text-Diff >= 0.34
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When the code you're testing returns multiple lines or records and
they're just plain wrong, sometimes an equivalent to the Unix diff
utility is just what's needed.

%description -l pl.UTF-8
Jeśli testowany kod zwraca wiele linii lub rekordów, które są
niepoprawne, czasem przydatny jest odpowiednik uniksowego narzędzia
diff.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
