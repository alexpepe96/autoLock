<h2>Configurazione ambiente unix</h2>
<p>Per verificare se <b>python</b> è già installato digitare da riga di comando<code>python3 -V</code>. Se non presente o per aggiornarlo eseguire il comando <code>sudo apt install python3</code></p>
<p>Installare <b>esptool</b> eseguendo il comando <code>sudo pip3 install esptool</code></p>
<p>Installare <b>ampy</b> eseguendo il comando <code>sudo pip3 install adafruit-ampy</code></p>
<p>Installare <b>picocom</b> eseguendo il comando <code>sudo apt install picocom</code></p>

<h2>Upload del firmware</h2>
<p>Creare una cartella progetto: in questo caso la chiamiamo <b>esp32</b></p>
<p>Scaricare il firmware all'indirizzo https://micropython.org/resources/firmware/esp32-idf3-20191220-v1.12.bin e spostarlo nella cartella <b>esp32</b></p>
<p>Da riga di comando spostarsi con il comando <code>cd (percorso cartella esp32)</code> nella cartella progetto</p>
<p>Eseguire il comando <code>esptool.py --port /dev/ttyUSB0 erase_flash</code> e tenere premuto il pulsante di boot fino a termine operazione</p>
<p>Eseguire il comando <code>esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash esp32-idf3-20191220-v1.12.bin</code></p>
<h4>Modifica dei file boot.py e main.py</h4>
<p>Scaricare i file <b>main.py</b> e <b>boot.py</b> dal repository github eseguendo il comando <code>git clone https://github.com/alexpepe96/autoLock.git</code> ed effettuare le opportune modifiche</p>
<p>Da riga di comando spostarsi con il comando <code>cd autoLock</code> nella cartella <b>autoLock</b></p>
<p>Eseguire il comando <code>ampy --port /dev/ttyUSB0 put 'main.py'</code> oppure <code>ampy --port /dev/ttyUSB0 put 'boot.py'</code> in base ai file modificati</p>
<p>Per verificare il corretto funzionamento eseguire il comando <code>sudo picocom -b 115200 /dev/ttyUSB0</code></p>

<h2>Rest Api</h2>
<p>Per sbloccare la serratura effettuare una chiamata POST all'indirizzo <code>ipCliente:8081/tennisify/api/v1.0/lock</code></p>
<p>Per leggere lo stato delle racchette effettuare una chiamata POST all'indirizzo <code>ipCliente:8081/tennisify/api/v1.0/rack</code></p>
