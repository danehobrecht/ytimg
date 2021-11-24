#!/venv/bin/python3

def main(user_input):
	if "https://youtu.be/" in user_input or "https://www.youtube.com/watch?v=" in user_input:
		l = len(user_input)
		uuid = user_input[l - 11:]
		url = "https://img.youtube.com/vi/" + uuid + "/maxresdefault.jpg"
		print("Video UUID:\t" + uuid + "\nThumbnail URL:\t" + url)
		return url
	else:
		return "http://127.0.0.1:5000/"
