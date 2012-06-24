Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	��Ʈ��ũ�� ���� ���ϵ���ȭ�� ���� ���α׷�
Summary(pl):	Program do wydajnego zdalnego uaktualniania plik�w
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	��������� ��� ������������ ���������� ���������� ������
Summary(uk):	�������� ��� ����������� צ��������� ��������� ���̦�
Summary(zh_CN):	[ͨѶ]���乤��
Summary(zh_TW):	[���]$(B6G?i��(c(B
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
zsync es un substituto m�s r�pido y flexible para rcp que permite la
sincronizaci�n de archivos o directorios, v�a red, de forma r�pida y
eficiente, entre diferentes m�quinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las m�quinas tengan una copia de lo que est� en la
otra. Est� disponible en este paquete, una relaci�n t�cnica
describiendo el algoritmo usado por el zsync.

%description -l ko
Zsync�� ���� ȣ��Ʈ ������ �ſ� ���� ����ȭ�ϴµ� �ŷ��Ҹ���
�˰����� ����Ѵ�. Zsync�� ������ ��ü�� ������ �� ��ſ� ��Ʈ����
���� ������ �ٸ� �κи��� �����ϱ� ������ ������. Zsync�� ������ �̷�
���μ��� Ȥ�� rcp Ŀ��带 ���� �� ����� ��ü�����ν� ���ȴ�. zsync
�˰����� �����ϴ� ������� ������ �� �ٷ��̿� ���ԵǾ� �ִ�.

%description -l pl
Zsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk�adni�
polece�. Program ten u�ywa efektywnego algorytmu "zsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta�a r�wnie� do��czona do pakietu.

%description -l pt_BR
O zsync � um substituto mais r�pido e flex�vel para o rcp permitindo
sincroniza��o de arquivos ou diret�rios via rede de forma r�pida e
eficiente entre diferentes m�quinas transferindo somente as diferen�as
entre estes diret�rios de forma compactada. Ele n�o precisa que
nenhuma das m�quinas tenha uma c�pia do que est� na outra.

Um relat�rio t�cnico descrevendo o algoritmo usado pelo zsync est�
dispon�vel neste pacote.

%description -l ru
zsync - ��� ����� ������� � ������ ������������ rcp, �����������
������� � ����������� �� ��������� � �������� ���� �������������
������ ��� ��������� �� ��������� ������� ����� �������� ������
�������� ����� ���� � ����������������� ����. ��� ���� ���������� ��
�����������, ����� ���� ������ ����� � ���� ����� ����, ��� ���� ��
������ ������.

%description -l uk
zsync - �� ������ �� ����˦�� ������������ rcp, ��� ��������դ ������
�� ��������� �� צ�������� �� �����Ӧ� ����֦ ������Φ��æ� ���̦� ��
������Ǧ� �� Ҧ���� ������� ������ ������ަ ���� צ�ͦ������� ͦ� ����
� �������������� ��Ħ. ��� ����� ���Ӧ� �� ����'������, ��� ����
������ ���� � ���� ��Ц� ����, �� � �� ��ۦ� ����Φ.

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
