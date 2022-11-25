all: compile install

compile:
	pyinstaller -F src/munin_rs500.py

install:
	sudo mkdir -p /usr/local/share/munin/plugins;
	sudo cp dist/munin_rs500 /usr/local/share/munin/plugins/
    sudo cp munin_plugin.conf /etc/munin/plugin-conf.d/apartment_temps
