Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	네트워크를 통한 파일동기화를 위한 프로그램
Summary(pl):	Program do wydajnego zdalnego uaktualniania plik�w
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	眺逑怒袴� 켈� 步팍客�肋逑� 臘죈턱卦하 苟卦隆턱�� 팁奸窘
Summary(uk):	眺逑怒皐 켈� 탬탸燉肋逑� 屢컴죈턱逑� 鷗窘謙鑛� 팁奸┹
Summary(zh_CN):	[繫祇]눈渴묏야
Summary(zh_TW):	[놉게]$(B6G?iㆅ(c(B
Name:		zsync
Version:	0.5
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://zsync.moria.org.uk/download/%{name}-%{version}.tar.bz2
# Source0-md5:	08beaf3fa95f16d8a2db2f7f3ea21196
URL:		http://zsync.moria.org.uk/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.316
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/zsyncd

%description
zsync is a file transfer program. It allows you to download a file
from a remote web server, where you have a copy of an older version of
the file on your computer already. zsync downloads only the new parts
of the file. It uses the same algorithm as rsync.

%description -l es
zsync es un substituto m�s r�pido y flexible para rcp que permite la
sincronizaci�n de archivos o directorios, v�a red, de forma r�pida y
eficiente, entre diferentes m�quinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las m�quinas tengan una copia de lo que est� en la
otra. Est� disponible en este paquete, una relaci�n t�cnica
describiendo el algoritmo usado por el zsync.

%description -l ko
Zsync는 원격 호스트 파일을 매우 빨리 동기화하는데 신뢰할만한
알고리즘을 사용한다. Zsync는 파일의 전체를 보내는 것 대신에 네트웍을
통해 파일의 다른 부분만을 전송하기 때문에 빠르다. Zsync는 강력한 미러
프로세스 혹은 rcp 커멘드를 통한 더 우수한 대체용으로써 사용된다. zsync
알고리즘을 묘사하는 기술적인 내용은 이 꾸러미에 포함되어 있다.

%description -l pl
Zsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk쿪dni�
polece�. Program ten u퓓wa efektywnego algorytmu "zsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta쿪 r�wnie� do낢czona do pakietu.

%description -l pt_BR
O zsync � um substituto mais r�pido e flex�vel para o rcp permitindo
sincroniza豫o de arquivos ou diret�rios via rede de forma r�pida e
eficiente entre diferentes m�quinas transferindo somente as diferen�as
entre estes diret�rios de forma compactada. Ele n�o precisa que
nenhuma das m�quinas tenha uma c�pia do que est� na outra.

Um relat�rio t�cnico descrevendo o algoritmo usado pelo zsync est�
dispon�vel neste pacote.

%description -l ru
zsync - 卜� 쫏謙� 쬔戇怒� � 핀쫀죙 죈茫텀适燉陸 rcp, 饉璞驅記北�
쬔戇論� � 步팍客�肋藍 饉 鞫卦北炚� � 瑙撞錄죌 膽燉 譚洸碌炚憫촁�
팁奸窘 �俓 個讀卿하� 适 怒蜜�奢謨 皐排适� 檎旽� 斤瑙컨司 冬景蓋
怒蜜�司� 考靈� 炚苽 � 蓋辜瑙幢�碌陸鑛鳩 慄컵. 眺� 卜鳩 遝淪膿턱卦 壙
苟拿죤턍忘�, 師苟� 謳适 皐排适 �考訣 � 膽쫓 蓋筋� 冬하, 師� 텁潼 适
켠朗銶 皐排壙.

%description -l uk
zsync - 쳔 伯�콕� 讀 핑良閘防 죈茫텀适燉陸 rcp, 麒� 憫쩨拍텡邏 伯�켄�
讀 탬탸燉肋� 饉 屢켑郡턱括 켓 瑙撞錄┹ 考瑙輦 譚洸碌過憫챈� 팁奸┹ 司
個讀卿푠� 适 娘剝�� 皐排适� 焙騎鳩 斤瑙컨誹 俓北 屢켐┧卦戇탱 稽� 炚苽
� 蓋辜瑙遝陸卦鼓 慄칡. 眺� 쵤鳩� 博綾┦ 壙 苟窘'拿蓋凜, 粉� 謳适
皐排适 皐訣 � 膽쩨 蓋揆� 冬하, 粉 � 适 ┧魃� 皐排過.

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
