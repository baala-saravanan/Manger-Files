import subprocess
import os
#import time

def run_command(command, input_str=None, check=True):
    try:
        result = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, input=input_str, check=check
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr.strip())
        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def is_hdmi_disconnected():
    output = run_command("xrandr")
    return "disconnected" in output

def decrypt_files(file_names, password, all_file_path, root_dir, keyfile_path=None):
    try:
        for file in file_names:
            bin_file = f"{all_file_path}encrypted_{file}.enc"
            org_file = f"{root_dir}{file}.py"
            bst_file = "/home/rock/Desktop/Hearsight/mycroft-precise/test/scripts/encrypted_best.enc"
            best_file = "/home/rock/Desktop/Hearsight/mycroft-precise/test/scripts/best.pt"
            if os.path.exists(org_file):
                os.remove(org_file)
            if os.path.exists(best_file):
                os.remove(best_file)
            
            if keyfile_path:
                run_command(f"openssl enc -d -aes-256-cbc -in {bin_file} -out {org_file} -pass file:{keyfile_path}")
                run_command(f"openssl enc -d -aes-256-cbc -in {bst_file} -out {best_file} -pass file:{keyfile_path}")
            else:
                run_command(f"openssl enc -d -aes-256-cbc -in {bin_file} -out {org_file} -k {password}", check=False)
                run_command(f"openssl enc -d -aes-256-cbc -in {bst_file} -out {best_file} -k {password}", check=False)

            print(f"Decrypted: {file}")
        return True
    except Exception as e:
        print("An error occurred during decryption:", str(e))
        return False

def main():
    file_dir = "/home/rock/Desktop/Hearsight/"
    
    file_names = [file.replace("encrypted_", "").replace(".enc", "") for file in os.listdir(file_dir) if "encrypted_" in file]

    root_dir = "/home/rock/Desktop/Hearsight/"
    all_file_path = "/home/rock/Desktop/Hearsight/"
    keyfile_path = "/home/rock/Desktop/Hearsight/mycroft-precise/test/scripts/file"
    hdmi_disconnected = is_hdmi_disconnected()
    decryption_successful = False
    if not hdmi_disconnected:
#        print("HDMI detected")
        password = input("Enter your password: ")
        password_2 = input("Enter your password: ")
        password_3 = input("Enter your password: ")

        if password_2 == f"{password}#" and password_3 == f"{password_2}%":
            decryption_successful = decrypt_files(file_names, password, all_file_path, root_dir)
        else:
#            print("Wrong passwords\n")
#            print("Shuting Down in 5 seconds: ")
#            for i in range(5,0,-1):
#                print(i)
#                time.sleep(1)
            os.system("python /home/rock/Desktop/Hearsight/English/off/off.py")

    if hdmi_disconnected:
        subprocess.Popen(["python3", "/home/rock/Desktop/Hearsight/mycroft-precise/test/scripts/detect.py"])
        if not os.path.exists(keyfile_path):
            print("Error: Keyfile not found.")
            return

        decryption_successful = decrypt_files(file_names, None, all_file_path, root_dir, keyfile_path)

if __name__ == "__main__":
    main()