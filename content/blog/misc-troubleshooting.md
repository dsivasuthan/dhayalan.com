---
date: 2018-11-08
title: Misc Troubleshooting
draft: false
---

# Virtual Box issue on Windows 10
If you are not able to get Vitual Box in Windows, try running the following (as admin)

```
dism.exe /Online /Disable-Feature:Microsoft-Hyper-V

bcdedit /set hypervisorlaunchtype off
```
Also make sure to remove the following from Windows Program and Features:
- Hyper-V
- Virtualizing Platform
- 