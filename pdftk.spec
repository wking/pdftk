%define itextvers 2.1.5

Summary:        The PDF Tool Kit
Name:           pdftk
Version:        1.41
Release:        13%{?dist}
License:        GPLv2+
URL:            http://www.pdfhacks.com/pdftk/
# Remove java-lib/com because it's contains licensing issue
Source0:        http://www.pdfhacks.com/pdftk/%{name}-%{version}-noitext.tar.bz2
Patch0:         pdftk-use-internal-itext.patch
Patch1:         pdftk-1.41-make.patch
Patch2:         pdftk-1.41-gcc44.patch
Group:          Applications/Publishing
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc-java
BuildRequires:  libgcj-devel
BuildRequires:  java-devel >= 1:1.6.0

# Requires itext-2.1.4-3
BuildRequires:  itext >= %{itextvers}

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -rf java_libs

%build
# Requires as a workaround for gcc BZ #39380
export CFLAGS="${RPM_OPT_FLAGS} -O0"
jar tf %{_javadir}/itext-%{itextvers}.jar | grep '\.class$' | sed 's/\.class//' | sed 's|/|\.|g' > classes
    gjavah -d java_libs -cni -classpath=%{_javadir}/itext-%{itextvers}.jar \
       `cat classes`
    cd pdftk
    make -f Makefile.RedHat LIBDIR=%{_libdir} %{?_smp_mflags} ITEXTVERS="%{itextvers}" 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 0755 pdftk/pdftk $RPM_BUILD_ROOT/%{_bindir}/pdftk
install -m 0644 debian/pdftk.1 $RPM_BUILD_ROOT/%{_mandir}/man1/pdftk.1
# Fix the weird dependency, e.g.
# /usr/lib64/gcj/itext/itext-x.y.z.jar.so()(64bit)  to
# /usr/lib64/gcj/itext/itext-x.y.z.jar.so
%define _use_internal_dependency_generator 0
cat << \EOF > %{name}.req
#!%{_buildshell}
grep -v %{_docdir} - | %{__find_requires} $* \
     | sed 's@\(itext-[0-9.]*\.jar\.so\)\(()(64bit)\)\?@\1@'
EOF

%define __find_requires %{_builddir}/%{name}-%{version}/%{name}.req
chmod +x %{__find_requires}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc pdftk.1.html pdftk.1.txt
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Mar 10 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.41-13
- Move to iText-2.1.5

* Thu Mar  5 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.41-12
- Make sure, the -O0 will be used by the Makefile

* Thu Mar  5 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.41-11
- substitute %%{_datadir}/java into %%{_javadir} in build stanza

* Thu Mar  5 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.41-10
- Use -O0 as a workaround for a gcc bug

* Sun Mar  1 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.41-9
- Remove license text
- Fix Dependencies
- fix Tab/Space

* Thu Feb 19 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.41-8
- Add BR and Req. to itext-2.1.4-3

* Sun Feb 15 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.41-7
- Build pdftk agains system iText library

* Sun Jan 25 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.41-6
- Fix license tag

* Wed Apr 11 2007 Thomas Fitzsimmons <fitzsim@redhat.com> 1.41-5
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
