from optparse import OptionParser
import sys
import program

# taking instagram username here. 
# using sys and optparse library's.

userDatas = OptionParser()

userDatas.add_option("-u", dest = "userName", help = "username", default = "admin123")
userDatas.add_option("-p", dest = "password", help = "password", default = "123456789")

userDatas.add_option("-t", dest = "targetName", help = "targetname", default = "test")

(datas, args) = userDatas.parse_args(sys.argv)


# firstly, we must login to Instagram.
# secondly, search for targetname on instagram. So if we want to search any target on instagram we must login.

userName = datas.userName
password = datas.password
targetName = datas.targetName


# python3 main.py -u {your USERNAME} -p {your PASSWORD} -t {target's USERNAME} this is using like that. 
