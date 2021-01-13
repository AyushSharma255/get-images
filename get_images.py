import sys
import shutil

import requests

if len(sys.argv) != 3:
	raise TypeError("Wrong amount of arguements, should be 2 command line arguements (excluding source code file).")

url_args = sys.argv[1]
url = f"https://picsum.photos/{url_args}"

num_of_times = int(sys.argv[2])


for i in range(num_of_times):
	r = requests.get(url, stream=True)
	
	with open(f"img/img_{i}.png", "wb") as img:
		shutil.copyfileobj(r.raw, img)