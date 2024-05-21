import os

file_dir = "/home/rock/Desktop/Hearsight/"
fle_dir = "/home/rock/Desktop/Hearsight/mycroft-precise/test/scripts/best.pt"
a = "best"
file_names = ["button","voice"]

for file in file_names:
    os.remove(f"{file_dir}{file}.py")
    print(f"{file} file removed")
os.remove(fle_dir)
print(f"{a} file removed")