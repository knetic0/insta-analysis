from program import posts, followers, following, bio, followers_nameList, follow_nameList
import time


datass = f'''

Number of Posts = {posts}
Number of Followers = {followers}
Number of Following = {following}
Biography Content = {bio}

'''

print(datass)

print("[+] Saving...")
time.sleep(2)

with open("datas.txt", "w") as file:
    file.write(datass)
    time.sleep(3)
    print("Save Successful!")
    file.close()

with open("followers.txt", "w") as file2:
    for names in followers_nameList:
        file2.write(names + "\n")
    file2.write("*"*20)
    for fname in follow_nameList:
        file2.write(fname + "\n")
    file2.close()
