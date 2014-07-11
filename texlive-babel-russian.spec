# revision 30287
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/russian
# catalog-date 2013-05-03 12:18:01 +0200
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-babel-russian
Version:	1.3
Release:	7
Summary:	Russian language module for Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/russian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-russian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-russian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-russian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for use of Babel in documents
written in Russian. The package is adapted for use both under
'traditional' TeX engines, and under XeTeX and LuaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-russian/russianb.ldf
%doc %{_texmfdistdir}/doc/generic/babel-russian/README
%doc %{_texmfdistdir}/doc/generic/babel-russian/russianb.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-russian/russianb.dtx
%doc %{_texmfdistdir}/source/generic/babel-russian/russianb.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
