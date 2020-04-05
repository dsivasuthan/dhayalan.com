---
date: 2019-05-08
title: Useful CLI commands
draft: false
---

These are just documentation for me because I don't want to remember them. It is not a guide for anything.

* awk

	```
	awk '/regex/'
	awk '!/regex/'

	awk 'BEGIN{a=5; b=2.5; print a+b}'
	awk '{sub(/:/, "-")} 1' // subtitution
	awk '{gsub(/:/, "-")} 1'
	```

* List network devices

	```
	Win:
	arp -a
	```

* Make VS Code remember Github credentials; Easier if you are working with multiple accounts for work and personal.

		git config credential.helper store

* Install Node

* Install NPM

		curl -L https://npmjs.org/install.sh | sudo sh
