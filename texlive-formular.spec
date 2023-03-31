Name:		texlive-formular
Version:	15878
Release:	2
Summary:	Create forms containing field for manual entry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/formular
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formular.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formular.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formular.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
When typesetting forms there often arises the need for defining
fields which consist of one or more lines where the customer
can write something down manually. This package offers some
commands for defining such fields in a distinctive way.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/formular/formular.sty
%doc %{_texmfdistdir}/doc/latex/formular/README
%doc %{_texmfdistdir}/doc/latex/formular/formular.pdf
#- source
%doc %{_texmfdistdir}/source/latex/formular/formular.dtx
%doc %{_texmfdistdir}/source/latex/formular/formular.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
