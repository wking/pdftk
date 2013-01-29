Notes on the different branches:

* robin: [Robin Houston's patches][RH] against v1.45.
* debian: [Debian patches][debian] against v1.44 as of Debian's 1.44-7
* gentoo: [Gentoo patches][gentoo] against v1.44 as of Gentoo's app-text/pdftk-1.44
* fedora: [Fedora patches][fedora] against v1.44 as of Fedora's 1.44-r11

My `.git/config` looks something like:

    [remote "origin"]
      url = git://github.com/wking/pdftk.git
      pushurl = git@github.com:wking/pdftk.git
      fetch = +refs/heads/*:refs/remotes/origin/*
    [remote "robin"]
      url = git://github.com/robinhouston/pdftk.git
      fetch = +refs/heads/*:refs/remotes/robin/*
    [remote "debian"]
      url = git://anonscm.debian.org/collab-maint/pdftk.git
      fetch = +refs/heads/*:refs/remotes/debian/*
    [remote "fedora"]
      url = git://pkgs.fedoraproject.org/pdftk.git
      fetch = +refs/heads/master:refs/remotes/fedora/master
      tagopt = --no-tags

There's no Git repository for Gentoo's Portage tree yet (they're
getting there :p), but you can [browse the CVS by hand][gentoo].

The patches by Robin, Debian, and Gentoo are all fairly lightweight,
but Fedora has ported pdftk to use an external [iText][] version 2.1.7
instead of the bundled `lowagie` precursor currently used in pdftk.

[RH]: https://github.com/robinhouston/pdftk/
[debian]: http://packages.debian.org/source/sid/pdftk
[gentoo]: http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/app-text/pdftk/
[fedora]: https://admin.fedoraproject.org/pkgdb/acls/name/pdftk
[iText]: http://sourceforge.net/projects/itext/
