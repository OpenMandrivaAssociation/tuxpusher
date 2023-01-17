%define oname TuxPusher

Name:       tuxpusher
Version:    1.0.4
Release:    1
Summary:    A Tux themed 3D coin pusher game.
Group:      Games
License:    GPL2.0
URL:        https://tuxpusher.com/
Source0:    https://github.com/mrbid/TuxPusher/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(glfw3)

%description
A Tux themed 3D coin pusher game.
Mechanics / Rules
Getting a gold coin in a silver slot rewards you 2x silver coins.
Getting a gold coin in a gold slot rewards you 2x gold coins.
Getting a tux in a slot when you already have the tux gives you 6x gold coins and 6x silver coins.
Controls
Just move around your mouse and click to release a coin.

Left Click = Release coin.
Right Click = Show/Hide cursor.
C = Orthographic/Perspective.
F = FPS to console.


%prep
%autosetup -n %{oname}-%{version} -p1

%build
%make_build

%install
%make_install

%files
