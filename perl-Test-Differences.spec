#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Test
%define		pnam	Differences
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Differences - test strings and data structures and show differences if not ok
Summary(pl.UTF-8):	Test::Differences - kontrola łańcuchów i struktur danych z pokazywaniem różnic
Name:		perl-Test-Differences
Version:	0.64
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ecfda620fe133e36a6e392d94ab8424d
URL:		http://search.cpan.org/dist/Test-Differences/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::Dumper) >= 2.126
BuildRequires:	perl-Capture-Tiny >= 0.24
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Text-Diff >= 1.43
%endif
Requires:	perl-Text-Diff >= 1.43
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
%doc Changes
%{perl_vendorlib}/Test/Differences.pm
%{_mandir}/man3/Test::Differences.3pm*
