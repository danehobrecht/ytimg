#!/venv/bin/python3

def main(url):
	if "https://youtu.be/" in url or "https://www.youtube.com/watch?v=" in url:
		l = len(url)
		uuid = url[l - 11:]
		maxresdefault = "https://img.youtube.com/vi/" + uuid + "/maxresdefault.jpg"
		print("Video UUID:\t" + uuid + "\nThumbnail URL:\t" + maxresdefault)
		return maxresdefault
	else:
		return "http://127.0.0.1:5000/"
