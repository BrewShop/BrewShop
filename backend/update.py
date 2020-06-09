import json
import sys
if sys.version_info < (3, 0):
	import urllib2 as urllib 
else:
	import urllib.request as urllib

# Convert to lowercase + numbers only for titleid field
def simplify(s): return "".join(c for c in s.lower() if (ord(c) >= ord("a") and ord(c) <= ord("z")) or (ord(c) >= ord("0") and ord(c) <= ord("9")))

list0 = json.loads("[]")

# Read apps.json
with open("apps.json", "r") as file:
	obj = json.load(file)

i = 0
for project in obj:
	i += 1
	out = []

	if project["location"] == "GitHub":
		print(project["name"] + " by " + project["author"])
		info = json.loads(urllib.urlopen("https://api.github.com/repos/" + project["author"] + "/" + project["name"]).read())
		releases = json.loads(urllib.urlopen("https://api.github.com/repos/" + project["author"] + "/" + project["name"] + "/releases/latest").read())

		files = []
		for asset in releases["assets"]:
			files.append({"name": asset["name"], "size": asset["size"], "url": asset["browser_download_url"]})
		out = {
			"id": i,
			"titleid": simplify(info["name"]),
			"name": info["name"],
			"description": info["description"] if not info["description"] == None else project["description"],
			"author": info["owner"]["login"],
			"files": files,
			"create_time": info["created_at"][:10],
			"update_time": releases["created_at"][:10],
			"version": releases["tag_name"],
			"categories": project["categories"],
			"url": info["html_url"]
		}
	elif project["location"] == "other":
		print(project["name"] + " by " + project["author"])
		out = project
		out["id"] = i
		out["titleid"] = simplify(project["name"])

	list0.append(out)

with open("./list0.json", "w") as file:
	json.dump(list0, file)