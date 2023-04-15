● Pythonを使ってIAQを利用する方法

PythonでIAQを利用する場合には、本誌の手法でビルドした「bsec_bme680」を使います。bsec_bme680を実行し、その結果をMQTT（Message Queuing Telemetry Transport）というプロトコルを利用してPython3のプログラムで受信できるようにします。

MQTTでやりとりできるようにするため以下のように実行して必要なライブラリなどをインストールしておきます。

-----
$ sudo pip3 install paho-mqtt
-----

次にプログラムを格納しておくフォルダーを準備し、以下のファイルをコピーします。
・bsec_bme680_python/bsec_bme680
・bsec_bme680_python/bsec_iaq.config
・bsec_bme680_python/bsec_iaq.state
・読者限定サイトで配布する「iaq.py」

ファイルが準備できたら、以下のように実行することでIAQが表示されます。

-----
$ python3 iaq.py
-----




