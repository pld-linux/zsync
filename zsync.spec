Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	³×Æ®¿öÅ©¸¦ ÅëÇÑ ÆÄÀÏµ¿±âÈ­¸¦ À§ÇÑ ÇÁ·Î±×·¥
Summary(pl):	Program do wydajnego zdalnego uaktualniania plików
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	ðÒÏÇÒÁÍÍÁ ÄÌÑ ÜÆÆÅËÔÉ×ÎÏÇÏ ÕÄÁÌÅÎÎÏÇÏ ÏÂÎÏ×ÌÅÎÉÑ ÆÁÊÌÏ×
Summary(uk):	ðÒÏÇÒÁÍÁ ÄÌÑ ÅÆÅËÔÉ×ÎÏÇÏ ×¦ÄÄÁÌÅÎÏÇÏ ÏÎÏ×ÌÅÎÎÑ ÆÁÊÌ¦×
Summary(zh_CN):	[Í¨Ñ¶]´«Êä¹¤¾ß
Summary(zh_TW):	[³ñ°Ô]$(B6G?i¤õ(c(B
Name:		zsync
Version:	0.4.0
Release:	0.1
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/zsync/%{name}-%{version}.tar.gz
# Source0-md5:	8840d1b6c7b1b7dc2ec4895eac613beb
URL:		http://zsync.moria.org.uk/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/zsyncd

%description
zsync is a file transfer program. It allows you to download a file
from a remote web server, where you have a copy of an older version of
the file on your computer already. zsync downloads only the new parts
of the file. It uses the same algorithm as rsync.

%description -l es
zsync es un substituto más rápido y flexible para rcp que permite la
sincronización de archivos o directorios, vía red, de forma rápida y
eficiente, entre diferentes máquinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las máquinas tengan una copia de lo que está en la
otra. Está disponible en este paquete, una relación técnica
describiendo el algoritmo usado por el zsync.

%description -l ko
Zsync´Â ¿ø°Ý È£½ºÆ® ÆÄÀÏÀ» ¸Å¿ì »¡¸® µ¿±âÈ­ÇÏ´Âµ¥ ½Å·ÚÇÒ¸¸ÇÑ
¾Ë°í¸®ÁòÀ» »ç¿ëÇÑ´Ù. Zsync´Â ÆÄÀÏÀÇ ÀüÃ¼¸¦ º¸³»´Â °Í ´ë½Å¿¡ ³×Æ®¿÷À»
ÅëÇØ ÆÄÀÏÀÇ ´Ù¸¥ ºÎºÐ¸¸À» Àü¼ÛÇÏ±â ¶§¹®¿¡ ºü¸£´Ù. Zsync´Â °­·ÂÇÑ ¹Ì·¯
ÇÁ·Î¼¼½º È¤Àº rcp Ä¿¸àµå¸¦ ÅëÇÑ ´õ ¿ì¼öÇÑ ´ëÃ¼¿ëÀ¸·Î½á »ç¿ëµÈ´Ù. zsync
¾Ë°í¸®ÁòÀ» ¹¦»çÇÏ´Â ±â¼úÀûÀÎ ³»¿ëÀº ÀÌ ²Ù·¯¹Ì¿¡ Æ÷ÇÔµÇ¾î ÀÖ´Ù.

%description -l pl
Zsync jest zamiennikiem programu rcp z bardziej rozbudowan± sk³adni±
poleceñ. Program ten u¿ywa efektywnego algorytmu "zsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta³a równie¿ do³±czona do pakietu.

%description -l pt_BR
O zsync é um substituto mais rápido e flexível para o rcp permitindo
sincronização de arquivos ou diretórios via rede de forma rápida e
eficiente entre diferentes máquinas transferindo somente as diferenças
entre estes diretórios de forma compactada. Ele não precisa que
nenhuma das máquinas tenha uma cópia do que está na outra.

Um relatório técnico descrevendo o algoritmo usado pelo zsync está
disponível neste pacote.

%description -l ru
zsync - ÜÔÏ ÂÏÌÅÅ ÂÙÓÔÒÁÑ É ÇÉÂËÁÑ ÁÌØÔÅÒÎÁÔÉ×Á rcp, ÐÏÚ×ÏÌÑÀÝÁÑ
ÂÙÓÔÒÕÀ É ÜÆÆÅËÔÉ×ÎÕÀ ÐÏ ÏÔÎÏÛÅÎÉÀ Ë ÒÅÓÕÒÓÁÍ ÓÅÔÉ ÓÉÎÈÒÏÎÉÚÁÃÉÀ
ÆÁÊÌÏ× ÉÌÉ ËÁÔÁÌÏÇÏ× ÎÁ ÒÁÚÌÉÞÎÙÈ ÍÁÛÉÎÁÈ ÐÕÔÅÍ ÐÅÒÅÄÁÞÉ ÔÏÌØËÏ
ÒÁÚÌÉÞÉÊ ÍÅÖÄÕ ÎÉÍÉ × ËÏÍÐÒÅÓÓÉÒÏ×ÁÎÎÏÍ ×ÉÄÅ. ðÒÉ ÜÔÏÍ ÓÏ×ÅÒÛÅÎÎÏ ÎÅ
ÏÂÑÚÁÔÅÌØÎÏ, ÞÔÏÂÙ ÏÄÎÁ ÍÁÛÉÎÁ ÉÍÅÌÁ Õ ÓÅÂÑ ËÏÐÉÀ ÔÏÇÏ, ÞÔÏ ÅÓÔØ ÎÁ
ÄÒÕÇÏÊ ÍÁÛÉÎÅ.

%description -l uk
zsync - ÃÅ Û×ÉÄÛÁ ÔÁ ÇÎÕÞË¦ÛÁ ÁÌØÔÅÒÎÁÔÉ×Á rcp, ÑËÁ ÚÁÂÅÚÐÅÞÕ¤ Û×ÉÄËÕ
ÔÁ ÅÆÅËÔÉ×ÎÕ ÐÏ ×¦ÄÎÏÛÅÎÎÀ ÄÏ ÒÅÓÕÒÓ¦× ÍÅÒÅÖ¦ ÓÉÎÈÒÏÎ¦ÚÁÃ¦À ÆÁÊÌ¦× ÞÉ
ËÁÔÁÌÏÇ¦× ÎÁ Ò¦ÚÎÉÈ ÍÁÛÉÎÁÈ ÛÌÑÈÏÍ ÐÅÒÅÄÁÞ¦ ÌÉÛÅ ×¦ÄÍ¦ÎÎÏÓÔÅÊ Í¦Ö ÎÉÍÉ
× ËÏÍÐÒÅÓÏ×ÁÎÏÍÕ ×ÉÄ¦. ðÒÉ ÃØÏÍÕ ÚÏ×Ó¦Í ÎÅ ÏÂÏ×'ÑÚËÏ×Ï, ÝÏÂ ÏÄÎÁ
ÍÁÛÉÎÁ ÍÁÌÁ × ÓÅÂÅ ËÏÐ¦À ÔÏÇÏ, ÝÏ ¤ ÎÁ ¦ÎÛ¦Ê ÍÁÛÉÎ¦.

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
install -d $RPM_BUILD_ROOT/etc/env.d

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{sysconfig/rc-inetd,rc.d/init.d,logrotate.d},/var/log}

:> $RPM_BUILD_ROOT/var/log/zsyncd.log
:> $RPM_BUILD_ROOT%{_sysconfdir}/zsyncd.secrets

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/zsyncd.conf
log file = /var/log/zsyncd.log
EOF

cat << EOF > $RPM_BUILD_ROOT/etc/env.d/CVSIGNORE
#CVSIGNORE=
EOF
cat << EOF > $RPM_BUILD_ROOT/etc/env.d/ZSYNC_RSH
#ZSYNC_RSH=
EOF
cat << EOF > $RPM_BUILD_ROOT/etc/env.d/ZSYNC_PROXY
#ZSYNC_PROXY=
EOF
cat << EOF > $RPM_BUILD_ROOT/etc/env.d/ZSYNC_PASSWORD
#ZSYNC_PASSWORD=
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(644,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/*
%dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zsyncd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zsyncd.secrets
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %ghost /var/log/zsyncd.log
%{_mandir}/man1/*
