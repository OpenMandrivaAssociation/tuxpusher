%global oname TuxPusher

Summary:	A Tux themed 3D coin pusher game
Name:		tuxpusher
Version:	1.0.4
Release:	1
Group:		Games
License:	GPLv2
URL:		https://github.com/mrbid/tuxpusher
Source0:	https://github.com/mrbid/TuxPusher/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(glfw3)

%description
A Tux themed 3D coin pusher game.

%files
%doc LICENSE
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/openmandriva-%{name}.desktop


#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

# fix makedile
sed -i -e "s|gcc|\$(CC) %{optflags}|g" makefile

%build
%set_build_flags
%make_build
#$CC main.c glad_gl.c -I inc -Ofast %{optflags} -lglfw -lm -o %{name}

%install
#%%make_install
# binary
install -pm 0755 -d %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}

# .desktop file
install -dm 0755 %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/openmandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A fun coin pusher game featuring Tux!
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Application;Game;ArcadeGame;
X-Vendor=OpenMandriva
EOF

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
#	rsvg-convert -f png -h ${d} -w ${d} snap/gui/%{name}.png \
#			-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
	convert -background none -resize "${d}x${d}" snap/gui/%{name}.png \
			%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -resize 32x32 snap/gui/%{name}.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}.xpm

