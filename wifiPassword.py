import subprocess

# Retrieve Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Extract the profile names
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print("\n{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("-" * 40)

for i in profiles:
    # Retrieve the key for each profile
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')

    # Extract the password
    password = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        print("{:<30}| {:<}".format(i, password[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, "No password found"))
