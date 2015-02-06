Summary:	UFO: Alien Invasion
Name:		ufoai
Version:	2.4
Release:	3
License:	GPLv2+
Group:		Games/Strategy
Url:		http://ufoai.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-source.tar.bz2
Source1:	%{name}.desktop
Patch0:		ufoai-2.4-destdir-support.patch
Patch1:		ufoai-2.4-dont-strip-binaries.patch
Patch2:		ufoai-2.4-missing-shebang.patch
Patch3:		ufoai-2.4-CameraDrawMode-anonymous-namespace-fix.patch
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gdkglext-x11-1.0)
BuildRequires:	pkgconfig(gtk+)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sdl) >= 1.2.10
BuildRequires:	pkgconfig(SDL_image)  >= 1.2.7
BuildRequires:	pkgconfig(SDL_mixer) >= 1.2.7
BuildRequires:	pkgconfig(SDL_ttf) >= 2.0.7
BuildRequires:	pkgconfig(theoradec)
# xvid is in plf, but we can build without support, adding dlopen() support and
# a suggests on it could be done though..
#BuildRequires:	xvid-devel
BuildRequires:	zip
Requires:	%{name}-data = %{version}
%rename ufo

%description
UFO: ALIEN INVASION is a strategy game featuring tactical combat against
hostile alien forces which are about to infiltrate earth at this very
moment. You are in command of a small special unit which has been
founded to face the alien strike force. To be successful on the long
run, you will also have to have a research team study the aliens and
their technologies in order to learn as much as possible about their
technology, their goals and the aliens themselves. 'UFO: Alien Invasion'
is heavily inspired by the 'X-COM' series by Mythos and Microprose.

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

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1 -b .destdir~
%patch1 -p1 -b .nostrip~
%patch2 -p1 -b .shebang~
%patch3 -p1 -b .camera

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

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -m644 src/ports/linux/ufo.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png

%find_lang ufoai

