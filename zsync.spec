Summary:	Program for efficient remote updates of files
Summary(es.UTF-8):   Programa para actualizar archivos remotos de forma eficiente
Summary(ko.UTF-8):   네트워크를 통한 파일동기화를 위한 프로그램
Summary(pl.UTF-8):   Program do wydajnego zdalnego uaktualniania plików
Summary(pt_BR.UTF-8):   Programa para atualizar arquivos remotos de forma eficiente
Summary(ru.UTF-8):   Программа для эффективного удаленного обновления файлов
Summary(uk.UTF-8):   Програма для ефективного віддаленого оновлення файлів
Summary(zh_CN.UTF-8):   [通讯]传输工具
Summary(zh_TW.UTF-8):   [喙啪]$(B6G?i火(c(B
Name:		zsync
Version:	0.5
Release:	2
License:	GPL
Group:		Daemons
Source0:	http://zsync.moria.org.uk/download/%{name}-%{version}.tar.bz2
# Source0-md5:	08beaf3fa95f16d8a2db2f7f3ea21196
URL:		http://zsync.moria.org.uk/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.318
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/zsyncd

%description
zsync is a file transfer program. It allows you to download a file
from a remote web server, where you have a copy of an older version of
the file on your computer already. zsync downloads only the new parts
of the file. It uses the same algorithm as rsync.

%description -l es.UTF-8
zsync es un substituto más rápido y flexible para rcp que permite la
sincronización de archivos o directorios, vía red, de forma rápida y
eficiente, entre diferentes máquinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las máquinas tengan una copia de lo que está en la
otra. Está disponible en este paquete, una relación técnica
describiendo el algoritmo usado por el zsync.

%description -l ko.UTF-8
Zsync는 원격 호스트 파일을 매우 빨리 동기화하는데 신뢰할만한
알고리즘을 사용한다. Zsync는 파일의 전체를 보내는 것 대신에 네트웍을
통해 파일의 다른 부분만을 전송하기 때문에 빠르다. Zsync는 강력한 미러
프로세스 혹은 rcp 커멘드를 통한 더 우수한 대체용으로써 사용된다. zsync
알고리즘을 묘사하는 기술적인 내용은 이 꾸러미에 포함되어 있다.

%description -l pl.UTF-8
Zsync jest zamiennikiem programu rcp z bardziej rozbudowaną składnią
poleceń. Program ten używa efektywnego algorytmu "zsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu została również dołączona do pakietu.

%description -l pt_BR.UTF-8
O zsync é um substituto mais rápido e flexível para o rcp permitindo
sincronização de arquivos ou diretórios via rede de forma rápida e
eficiente entre diferentes máquinas transferindo somente as diferenças
entre estes diretórios de forma compactada. Ele não precisa que
nenhuma das máquinas tenha uma cópia do que está na outra.

Um relatório técnico descrevendo o algoritmo usado pelo zsync está
disponível neste pacote.

%description -l ru.UTF-8
zsync - это более быстрая и гибкая альтернатива rcp, позволяющая
быструю и эффективную по отношению к ресурсам сети синхронизацию
файлов или каталогов на различных машинах путем передачи только
различий между ними в компрессированном виде. При этом совершенно не
обязательно, чтобы одна машина имела у себя копию того, что есть на
другой машине.

%description -l uk.UTF-8
zsync - це швидша та гнучкіша альтернатива rcp, яка забезпечує швидку
та ефективну по відношенню до ресурсів мережі синхронізацію файлів чи
каталогів на різних машинах шляхом передачі лише відмінностей між ними
в компресованому виді. При цьому зовсім не обов'язково, щоб одна
машина мала в себе копію того, що є на іншій машині.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	%{?with_rsh:--with-rsh=rsh} \
	--enable-ipv6 \
	--disable-debug \
	--with-zsyncd-conf=%{_sysconfdir}/zsyncd.conf

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/env.d,/var/log}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

:> $RPM_BUILD_ROOT/var/log/zsyncd.log
:> $RPM_BUILD_ROOT%{_sysconfdir}/zsyncd.secrets

cat << 'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/zsyncd.conf
log file = /var/log/zsyncd.log
EOF

cat << 'EOF' > $RPM_BUILD_ROOT/etc/env.d/CVSIGNORE
#CVSIGNORE=
EOF
cat << 'EOF' > $RPM_BUILD_ROOT/etc/env.d/ZSYNC_RSH
#ZSYNC_RSH=
EOF
cat << 'EOF' > $RPM_BUILD_ROOT/etc/env.d/ZSYNC_PROXY
#ZSYNC_PROXY=
EOF
cat << 'EOF' > $RPM_BUILD_ROOT/etc/env.d/ZSYNC_PASSWORD
#ZSYNC_PASSWORD=
EOF

rm -rf $RPM_BUILD_ROOT%{_docdir}/zsync

%clean
rm -rf $RPM_BUILD_ROOT

%post
%env_update

%postun
%env_update

%files
%defattr(644,root,root,755)
%doc NEWS README
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/*
%dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zsyncd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zsyncd.secrets
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %ghost /var/log/zsyncd.log
%{_mandir}/man1/*
