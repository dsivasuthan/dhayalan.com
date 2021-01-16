---
date: 2019-05-08
title: Useful CLI commands
draft: false
---

These are just reminders/documentation for me because I don't want to remember them. It is not a guide for anything, it just has commands and tricks I use when reinstalling OS or fixing someone's computer.

* GNU/Linux
	* remap right alt key with context menu button (I miss the context button on my ThinkPad)

		```
		// add this to your startup script to make it permanent
		xmodmap -e "keycode  108 = Menu"
		```
	* awk

		```
		awk '/regex/'
		awk '!/regex/'

		awk 'BEGIN{a=5; b=2.5; print a+b}'
		awk '{sub(/:/, "-")} 1' // subtitution
		awk '{gsub(/:/, "-")} 1'
		```

	* Make VS Code remember Github credentials; Easier if you are working with multiple accounts for work and personal.

		`git config credential.helper store`

	* Print exit code of previous-run program

		`echo $?`

* Windows
	* PATH manipulation

		```
		env | grep PATH
		echo $PATH
		export PATH=<previous-paths>:<new-path>
		```

	* List network devices
	
		`arp -a`

* nodejs

	* Installing NPM

		```
		curl -L https://npmjs.org/install.sh | sudo sh
		```

	* Clear node modules cache and install dependencies

		```
		rm node_modules -r
		npm cache clean --force
		npm cache verify
		npm install
		```

*	CLI

	* youtube-dl - best audio

		```
		youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0
		```

	* termux - setting up, etc

		* settings file `~/.termux/termux.properties`
		* add extra touch keyboard buttons
			
			```
			extra-keys = [ \
				['ESC','|','/','HOME','UP','END','PGUP','DEL'], \
				['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP'] \
			]
			```
		
		* reload settings

			```
			termux-reload-settings
			```