#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Fuzzy
Summary:	AI::Fuzzy - Perl extension for Fuzzy Logic
Summary(pl):	AI::Fuzzy - rozszerzenie Perla do logiki rozmytej
Name:		perl-AI-Fuzzy
Version:	0.05
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::Fuzzy really consists of two modules - AI::Fuzzy::Label and
AI::Fuzzy::Set.

A fuzzy set is simply a mathematical set to which members can partially
belong.  For example, a particular shade of gray may partially belong
to the set of dark colors, whereas black would have full membership,
and lemon yellow would have almost no membership.

A fuzzy labeler classifies a particular crisp value by examining the
degree to which it belongs to several sets, and selecting the most
appropriate.  For example, it can decide whether to call water at 60
degrees Fahrenheit "cold", "cool", or "warm".  A fuzzy label might be
one of these labels, or a fuzzy set describing to what degree each of
the labels describes the particular value in question.

%description -l pl
Pakiet AI::Fuzzy sk�ada si� z dw�ch modu��w: AI::Fuzzy::Label i
AI::Fuzzy::Set.

Zbi�r rozmyty to prosty matematyczny zbi�r, do ktorego elementy mog�
nale�e� cz�ciowo. Na przyk�ad, konkretny odcie� szaro�ci mo�e
cz�ciowo nale�e� do zbioru kolor�w ciemnych, natomiast czarny b�dzie
nale�a� do niego ca�kowicie, a cytrynowo-��ty nie b�dzie nale�a�
prawie wcale.

Rozmyta funkcja etykietuj�ca klasyfikuje now� konkretn� warto��
sprawdzaj�c stopie�, w jakim nale�y do r�nych zbior�w i wybieraj�c
najbardziej odpowiedni. Na przyk�ad, aby zdecydowa�, jak nazywa� wod�
o temperaturze 60 stopni Fahrenheita "zimn�", "ch�odn�" czy "ciep��".
Rozmyt� etykiet� mo�e by� jedna z nich, lub rozmyty zbi�r opisuj�cy w
jakim stopniu ka�da z tych etykiet opisuje dan� warto��.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
