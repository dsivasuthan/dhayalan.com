---
date: 2020-11-10
title: Setting Up Pop! OS on Thinkpad X1 Carbon Gen 5
draft: false
---

Recently, I upgraded to an older X1 Carbon from my trusty T440s. In the transition, I decided to switch to Pop! OS running GNOME from Manjaro running KDE. I will miss the AUR and bleeding edge rolling releases. The main reason for the switch is KDE and the out of the box experience with Pop! OS, nothing against KDE; in fact, I loved the ability to customize the heck out of everything.

System76 has done an amazing job tweaking Pop! OS; it has become a very stable and fun-to-use OS; thanks to GNOME's simplicity and focus user-experience. Since my new used ThinkPad has enough RAM, I don't even need to worry about GNOME's performance.

The following is a list of software and tweaks I added to make it viable for me.
	
* Touchpad gestures
		
	Install [`libinput-gestures`](https://github.com/bulletmark/libinput-gestures) for touchpad gesture.

	GNOME doesn't have good gesture support out of the box, at least for laptop. So I had to use this FOSS to get some gestures working.

	```
	sudo gpasswd -a $USER input // and restart PC

	sudo apt-get install wmctrl xdotool
	sudo apt-get install libinput-tools

	git clone https://github.com/bulletmark/libinput-gestures.git
	cd libinput-gestures/
	sudo make install
	libinput-gestures-setup start
  ```

* Install TLP

	Keep in mind the following set of will install and caliberate battery, so your screen will go blank for a few mins. It is best to run the following on a freshly started machine.

	```
	sudo add-apt-repository ppa:linrunner/tlp
	sudo apt update
	sudo apt install tlp tlp-rdw --no-install-recommends
	sudo apt install acpi-call-dkms
	sudo tlp-stat

	sudo apt install powertop
	sudo powertop -c
  ```
	
* Install software not found in Pop!_Shop

	```
	sudo apt install -y nautilus-dropbox
	sudo apt install -y code
	sudo apt install -y vlc
	sudo apt install neofetch // everybody needs to show off their unix
  ```

* Install and tweak touchpad drivers

	The default values for touchpad sensitivity is very janky. You will have to install and tweak as shown below. [Find more details here.](https://forums.linuxmint.com/viewtopic.php?p=765618#p765618)

	```
	sudo apt install xserver-xorg-input-synaptics // and reboot pc
	xinput // to find the touchpad device id
	xinput list-props X // replace X with touchpad device id
	xinput --set-prop X 316 14 17 128 // replace X, and tweak the numbers as necessary. These nums worked for me. FingerLow, FingerHigh, and FingerPress.
