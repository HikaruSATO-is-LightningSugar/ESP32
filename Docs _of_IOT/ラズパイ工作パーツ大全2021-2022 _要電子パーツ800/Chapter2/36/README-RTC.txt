● リアルタイムクロックの設定
　AdafruitのDS1307を使って、リアルタイムクロックから現在時刻を取得するには、ラズパイの設定をする必要があります。
　端末アプリを起動し、以下のように実行して設定ファイル「/boot/config.txt」を編集します。

-----
$ sudo leafpad /boot/config.txt
-----

　テキストエディタが起動したら、ファイルの末尾に以下の1行を追加し、ファイルを保存します。

-----
dtoverlay=i2c-rtc,ds1307
-----

　設定したらラズパイを再起動します。
　Raspberry Pi OSには、ラズパイを終了する際に時刻情報をファイルに保管しておく「fake-hwclock」が動作しています。しかし、RTCを使う場合fale-hwclockが原因で時刻がくるってしまう事があります。そこで、fale-hwclockを動作しないように設定します。端末アプリで以下のように実行します。

-----
$ sudo apt -y remove fake-hwclock
$ sudo update-rc.d -f fake-hwclock remove
$ sudo systemctl disable fake-hwclock
$ sudo leafpad /lib/udev/hwclock-set
-----

　テキストエディタで設定ファイルが開いたら、以下に示した各行の先頭に「#」を付加します。

・7～9行目
if [ -e /run/systemd/system ] ; then
    exit 0
fi

・29行目
/sbin/hwclock --rtc=$dev --systz --badyear

・32行目
/sbin/hwclock --rtc=$dev --systz

　設定したらファイル保存します。これで設定完了です。




