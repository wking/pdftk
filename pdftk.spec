Summary: 	The PDF Tool Kit
Name: 		pdftk
Version: 	1.41
Release: 	4%{?dist}
License:	GPL
URL: 		http://www.pdfhacks.com/pdftk/
Source0: 	http://www.pdfhacks.com/pdftk/%{name}-%{version}.tar.bz2
Source1:        gpl.txt
Patch0:	        pdftk-1.41-rpmopt.patch
Patch1:	        pdftk-1.41-system-libgcj.patch
Patch2:	        pdftk-1.41-gcjh.patch
Group: 		Applications/Publishing
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires:	gcc-java
BuildRequires:	libgcj-devel

%description
If PDF is electronic paper, then pdftk is an electronic staple-remover,
hole-punch, binder, secret-decoder-ring, and X-Ray-glasses. Pdftk is a simple
tool for doing everyday things with PDF documents. Keep one in the top drawer
of your desktop and use it to:

    * Merge PDF Documents
    * Split PDF Pages into a New Document
    * Decrypt Input as Necessary (Password Required)
    * Encrypt Output as Desired
    * Burst a PDF Document into Single Pages
    * Report on PDF Metrics, including Metadata and Bookmarks
    * Uncompress and Re-Compress Page Streams
    * Repair Corrupted PDF (Where Possible)

Pdftk is also an example of how to use a library of Java classes in a
stand-alone C++ program. Specifically, it demonstrates how GCJ and CNI allow
C++ code to use iText's (itext-paulo) Java classes.

%prep
%setup -q
%patch0 -p1 -b .rpmopt
%patch1 -p0 -b .system-libgcj
%patch2 -p0 -b .gcjh
rm -rf java_libs/gnu_local java_libs/java_local java_libs/gnu

%build
unset CLASSPATH && cd pdftk && make -f Makefile.RedHat && cd -

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 0755 pdftk/pdftk $RPM_BUILD_ROOT/%{_bindir}/pdftk
install -m 0644 debian/pdftk.1 $RPM_BUILD_ROOT/%{_mandir}/man1/pdftk.1
cp %{SOURCE1} COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc pdftk.1.html pdftk.1.txt COPYRIGHT
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Apr 11 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.41-4
- Build against system libgcj.
- Patch build for new gcjh.
- Resolves: rhbz#233682 rhbz#233489 rhbz#233514

* Wed Feb 28 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.41-4
- Rebuild to solve broken deps

* Mon Feb 26 2007 Jochen Schmitt <s4504kr@zeus.herr-schmitt.de> 1.41-3
- Use $$RPM_OPT_FLAGS (#228945)

* Wed Nov 29 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.41-2
- New upstream release

* Sun Sep  3 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.12-8
- Rebuild for FC-6

* Mon Jul 31 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.12-7
- Rebuild

* Sun Feb 12 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.12-6
- Rebuild for FC5

* Thu Dec 15 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.12-5
- Rebuild
- Remove strange '//SID' comment.

* Sun Jul 31 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.12-3
- Add literal GPL text as Source1

* Wed Jul 27 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.12-2
- Don't compress man page
- Remove pdftk.1.notes
- Add COPYRIGHT from debian/copyright

* Tue Jul 26 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.12-1
- Initial RPM release
