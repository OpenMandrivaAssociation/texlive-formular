# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/formular
# catalog-date 2007-01-05 21:30:32 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-formular
Version:	1.0a
Release:	2
Summary:	Create forms containing field for manual entry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/formular
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formular.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formular.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formular.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-2
+ Revision: 752085
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 718495
- texlive-formular
- texlive-formular
- texlive-formular
- texlive-formular

