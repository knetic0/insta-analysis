from program import posts, verified, followers, following, bio, followers_nameList, follow_nameList, private, business, business_type
import time


datass = f'''

Number of Posts = {posts}
Number of Followers = {followers}
Number of Following = {following}
Biography Content = {bio}
Profile is Private ? = {private}
Is Business Account ? = {business}
What is Category of Business Account ? = {business_type}
Is Profile Verified ? = {verified}

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
    file2.write("*"*20 + "\n")
    for fname in follow_nameList:
        file2.write(fname + "\n")
    file2.close()
