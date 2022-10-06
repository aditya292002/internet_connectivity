

# python script to check internet connectivity and speed


import urllib.request
import speedtest



def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False


# test
def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)





print( "connected" if connect() else "no internet!" )
speed_test = speedtest.Speedtest()

# speedtest's download and upload function returns in bytes, so need to convert them to MB
download_speed = bytes_to_mb(speed_test.download())
upload_speed = bytes_to_mb(speed_test.upload())


print("Your Download speed is", download_speed, "MB") 
print("Your Download speed is", upload_speed, "MB") 


