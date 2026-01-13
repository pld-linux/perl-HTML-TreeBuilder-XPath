#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	HTML
%define	pnam	TreeBuilder-XPath
Summary:	Typical XPath methods for HTML::TreeBuilder
Summary(pl.UTF-8):	Typowe metody XPath dla klasy HTML::TreeBuilder
Name:		perl-HTML-TreeBuilder-XPath
Version:	0.14
Release:	2
# same as perl5 5.8.4+
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a3fa3b73ff51dd6ec63be394dcd2a3b5
URL:		http://search.cpan.org/dist/HTML-TreeBuilder-XPath/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-XML-XPathEngine >= 0.12
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds typical XPath methods to HTML::TreeBuilder, to make
it easy to query a document.

%description -l pl.UTF-8
Ten moduł dodaje typowe metody XPath do klasy HTML::TreeBuilder aby
ułatwić odpytywanie dokumentu.

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
%{perl_vendorlib}/HTML/TreeBuilder/*.pm
%{_mandir}/man3/*
