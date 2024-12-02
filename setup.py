import os, platform
platform = platform.system()
import json

def user_data_read():
    with open('./Data/user_data.json', 'r') as f:
        return json.load(f)

def user_data_write(newdata):
    with open('./Data/user_data.json', 'w') as f:
        json.dump(newdata, f, ensure_ascii=False)

def start_setup():
    if platform == "Darwin":
        print('''
        Looks like you are on Mac OS X
        Are you on an ARM processor? (Apple M Series Chip)
        ''')
        if input("[y/n]") == "y":
            d = user_data_read()
            d["driver_name"] = "chromedriver_macos_arm"
            user_data_write(d)
        else:
            d = user_data_read()
            d["driver_name"] = "chromedriver_macos_x64"
            user_data_write(d)
        
    elif platform == "Linux":    
        print("Looks like you are on Linux")
        d = user_data_read()
        d["driver_name"] = "chromedriver_linux_64"
        user_data_write(d)

    elif platform == "Windows":
        print("Looks like you are on Windows")
        d = user_data_read()
        d["driver_name"] = "chromedriver_win64.exe"
        user_data_write(d)
    else:  
        print("Looks like you are on an unsupported platform")

    print('\n\n\n')
    username = input("Enter your srn: ")
    password = input("Enter your wifi password: ")
    d = user_data_read()
    d["username"] = username
    d["password"] = password
    user_data_write(d)
    print('\n\n\n')
    print("Setup complete!")

if __name__ == "__main__":
    start_setup()