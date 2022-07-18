from program import posts, followers, following
import time


datass = f'''

        Number of Posts = {posts}
        Number of Followers = {followers}
        Number of Following = {following}

'''


print("[+] Saving...")
time.sleep(2)

with open("datas.txt", "w") as file:
    file.write(datass)
    time.sleep(3)
    print("Save Successful!")

