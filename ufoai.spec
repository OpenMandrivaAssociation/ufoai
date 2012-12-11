Name:		ufoai
Version:	2.4
Release:	1
URL:		http://ufoai.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-source.tar.bz2
Source1:	%{name}.desktop
Patch0:		ufoai-2.4-destdir-support.patch
Patch1:		ufoai-2.4-dont-strip-binaries.patch
Patch2:		ufoai-2.4-missing-shebang.patch

License:	GPLv2+
Group:		Games/Strategy
Summary:	UFO: Alien Invasion

%rename ufo

Requires:	%{name}-data = %{version}

BuildRequires:	pkgconfig(libcurl)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(sdl) >= 1.2.10
BuildRequires:	pkgconfig(SDL_image)  >= 1.2.7
BuildRequires:	pkgconfig(SDL_mixer) >= 1.2.7
BuildRequires:	pkgconfig(SDL_ttf) >= 2.0.7
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(gdkglext-x11-1.0)
BuildRequires:	pkgconfig(gtk+)
# xvid is in plf, but we can build without support, adding dlopen() support and
# a suggests on it could be done though..
#BuildRequires:	xvid-devel
BuildRequires:	pkgconfig(theoradec)
BuildRequires:	zip

%description
UFO: ALIEN INVASION is a strategy game featuring tactical combat against
hostile alien forces which are about to infiltrate earth at this very
moment. You are in command of a small special unit which has been
founded to face the alien strike force. To be successful on the long
run, you will also have to have a research team study the aliens and
their technologies in order to learn as much as possible about their
technology, their goals and the aliens themselves. 'UFO: Alien Invasion'
is heavily inspired by the 'X-COM' series by Mythos and Microprose.


%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1 -b .destdir~
%patch1 -p1 -b .nostrip~
%patch2 -p1 -b .shebang~

%build
./configure	--prefix=%{_prefix} \
		--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}/ufoai \
		--localedir=%{_localedir} \
		--enable-release \
%ifarch x86_64
		--enable-sse \
%endif
		--enable-cgame-campaign \
		--enable-cgame-multiplayer \
		--enable-cgame-skirmish \
		--enable-cgame-staticcampaign \
		--enable-game \
		--enable-memory \
		--enable-testall \
		--enable-ufo2map \
		--enable-ufoded \
		--enable-ufo \
		--enable-ufomodel \
		--enable-uforadiant \
		--enable-ufoslicer
%make

%install
%makeinstall_std
# Remove empty data files to avoid file conflict with data package
rm -f %{buildroot}/%{_gamesdatadir}/%{name}/base/*pk3

%find_lang ufoai
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -m644 src/ports/linux/ufo.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files -f ufoai.lang
%doc LICENSES
%{_gamesbindir}/ufo*
%dir %{_gamesdatadir}/ufoai
%{_gamesdatadir}/ufoai/memory
%{_gamesdatadir}/ufoai/ufo*
%dir %{_gamesdatadir}/ufoai/base
%{_gamesdatadir}/ufoai/base/game.so
%dir %{_gamesdatadir}/ufoai/radiant
%{_gamesdatadir}/ufoai/radiant/uforadiant/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed May 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.4-1
+ Revision: 797633
- add 'zip' as buildrequires in order for pk3 archives to be made
- leave stripping of binaries to helper scripts so that we can get -debuginfo
  packages (P1)
- use pkgconfig() dependencies for buildrequires
- enable all modules
- enable SSE on x86_64
- help Solbu updating to latest version and regenerate destdir patch (P0)

  + Johnny A. Solbu <solbu@mandriva.org>
    - Fix patch
    - Remove empty data files, to avoid file conflict with data package

* Sun Jan 22 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3.1-2
+ Revision: 764872
- be sure to link against pthread
- fix build with libpng 1.5

* Mon Jul 11 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3.1-1
+ Revision: 689578
- fix buildrequires
- don't ship useless INSTALL file
- drop deprecated spec stuff

  + Johnny A. Solbu <solbu@mandriva.org>
    - New version
    - Bugfix. The folder base/ needs to exist to compile.
    - Define locale dir in ufoai.desktop, the game assumes ./base/i18n/

* Fri Sep 24 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3-1mdv2011.0
+ Revision: 580811
- disable xvid support as it requires plf package...
- import ufoai


* Thu Sep 23 2010 Per Øyvind Karlsen <peroyvind@mandria.org> 2.3-1
- use &%%{_gamesdatadir} & %%{_gamesbindir}
- make paths comply mostly with FHS (P0)
- package from Johnny A. Solbu <johnny@solbu.net>

* Tue Jul 5 2010 Johnny A. Solbu <johnny@solbu.net> 2.2.1-1mdv
- Bugfix. the shellscripts (/usr/bin/{ufo,ufoded}) tried to launch the game from RPM_BUILD_ROOT.

* Thu Apr 2 2010 Johnny A. Solbu <johnny@solbu.net> 2.2.1-1mdv
- Added menu entry.

* Tue Mar 31 2010 Johnny A. Solbu <johnny@solbu.net> 2.2.1-1mdv
- More spec cleanup, after tip from Per Øyvind Karlsen.

* Tue Mar 30 2010 Johnny A. Solbu <johnny@solbu.net> 2.2.1-1mdv
- Upgraded the package.
- spec cleanup.

* Fri Jan 27 2006 Guillaume Rousse <guillomovitch@zarb.org> 0.10-4plf
- %%mkrel 
- spec cleanup

* Sun Nov 28 2004 Guillaume Rousse <guillomovitch@zarb.org> 0.10-3plf
- fix macros 
- PLF reason

* Tue Sep 28 2004 Guillaume Rousse <guillomovitch@zarb.org> 0.10-2plf
- moved to plf, as it is useless without its data

* Tue Mar 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.10-2mdk
- buildrequires

* Fri Feb 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.10-1mdk
- initial mdk release
