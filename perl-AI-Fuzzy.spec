#
# Conditional build:
%bcond_without	tests	# don't perform "make test"

%define		pdir	AI
%define		pnam	Fuzzy
%include	/usr/lib/rpm/macros.perl
Summary:	AI::Fuzzy - Perl extension for Fuzzy Logic
Summary(pl.UTF-8):	AI::Fuzzy - rozszerzenie Perla do logiki rozmytej
Name:		perl-AI-Fuzzy
Version:	0.05
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f9d8f20cff0ad81651f96800f15e6b3
URL:		http://search.cpan.org/dist/AI-Fuzzy/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::Fuzzy really consists of two modules - AI::Fuzzy::Label and
AI::Fuzzy::Set.

A fuzzy set is simply a mathematical set to which members can
partially belong. For example, a particular shade of gray may
partially belong to the set of dark colors, whereas black would have
full membership, and lemon yellow would have almost no membership.

A fuzzy labeler classifies a particular crisp value by examining the
degree to which it belongs to several sets, and selecting the most
appropriate. For example, it can decide whether to call water at 60
degrees Fahrenheit "cold", "cool", or "warm". A fuzzy label might be
one of these labels, or a fuzzy set describing to what degree each of
the labels describes the particular value in question.

%description -l pl.UTF-8
Pakiet AI::Fuzzy składa się z dwóch modułów: AI::Fuzzy::Label i
AI::Fuzzy::Set.

Zbiór rozmyty to prosty matematyczny zbiór, do którego elementy mogą
należeć częściowo. Na przykład, konkretny odcień szarości może
częściowo należeć do zbioru kolorów ciemnych, natomiast czarny będzie
należał do niego całkowicie, a cytrynowo-żółty nie będzie należał
prawie wcale.

Rozmyta funkcja etykietująca klasyfikuje nową konkretną wartość
sprawdzając stopień, w jakim należy do różnych zbiorów i wybierając
najbardziej odpowiedni. Na przykład, aby zdecydować, jak nazywać wodę
o temperaturze 60 stopni Fahrenheita "zimną", "chłodną" czy "ciepłą".
Rozmytą etykietą może być jedna z nich, lub rozmyty zbiór opisujący w
jakim stopniu każda z tych etykiet opisuje daną wartość.

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
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
