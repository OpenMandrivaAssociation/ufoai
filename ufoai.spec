Name:		ufoai
Version:	2.3
Release:	%mkrel 1
URL:		http://ufoai.sourceforge.net/
Source0:	%{name}-%{version}-source.tar.bz2
Source1:	%{name}.desktop
Patch0:		ufoai-2.3-almost-fhs-compliance.patch
License:	GPLv2+
Group:		Games/Strategy
Summary:	UFO: Alien Invasion
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%rename ufo

Requires:	%{name}-data = %{version}

BuildRequires:	curl-devel
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	SDL_image-devel >= 1.2.7
BuildRequires:	SDL_mixer-devel >= 1.2.7
BuildRequires:	SDL_ttf-devel >= 2.0.7
BuildRequires:	openal-devel
BuildRequires:	gtksourceview-devel
BuildRequires:	gtkglext-devel
BuildRequires:	gtk+-devel
BuildRequires:	xvid-devel
BuildRequires:	libtheora-devel

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
%patch0 -p1 -b .fhs~
autoreconf

%build
%configure	--bindir=%{_gamesbindir} \
		--datarootdir=%{_gamesdatadir} \
		--datadir=%{_gamesdatadir} \
		--localedir=%{_datadir}/locale \
		--enable-release 
%make

%install
rm -rf %{buildroot}
make install_exec DESTDIR=%{buildroot}

%find_lang ufoai
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -m644 src/ports/linux/ufo.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%files -f ufoai.lang
%defattr(-,root,root)
%doc INSTALL README
%{_gamesbindir}/ufo*
%dir %{_gamesdatadir}/ufoai
%dir %{_gamesdatadir}/ufoai/base
%{_gamesdatadir}/ufoai/base/game.so
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

