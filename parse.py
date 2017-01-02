import csv
import xml.etree.ElementTree as ET
ns = {'disqus': 'http://disqus.com',
'internal': "http://disqus.com/disqus-internals"}

def createTable(root):
	idDictionary = {}
	for thread in root.findall('disqus:thread',ns):
		if not thread.attrib[thread.attrib.keys()[0]] in idDictionary:
			idDictionary[thread.attrib[thread.attrib.keys()[0]]] = []
	return idDictionary

def printCSV(table):
	row = 0
	col = 0
	filename = "output.csv"
	with open(filename, 'wb') as f:
		cWriter = csv.writer(f)
		row = ["Thread ID","Post ID","Parent ID","Email","Username","IP Address","Date","Content"]
		cWriter.writerow([unicode(s).encode("utf-8") for s in row])
		for key in table:
			keyList = table[key]
			for item in keyList:
				row = [item.threadID , item.post,  item.parentID, item.authEmail, item.authUser, item.authIP, item.date, item.content ]
				cWriter.writerow([unicode(s).encode("utf-8") for s in row])



def buildDictionary(root, table):
	for post in root.findall('disqus:post', ns):
		postID = post.attrib[post.attrib.keys()[0]]
		threadID = post.find('disqus:thread',ns).attrib[post.find('disqus:thread',ns).attrib.keys()[0]]
		parent = post.find('disqus:parent',ns)
		date = post.find('disqus:createdAt',ns).text
		author = post.find('disqus:author', ns)
		ip = post.find('disqus:ipAddress', ns).text
		content = post.find('disqus:message', ns).text
		if author is not None:
			email = author.find('disqus:email', ns).text
			user = author.find('disqus:username', ns)
			if user is not None:
				username = user.text
		parentID = 0
		if parent is not None:
			parentID = parent.attrib[parent.attrib.keys()[0]]
		#print("Post:" , postID , " thread ID : " , threadID , " Parent ID: " , parentID , " Email: " , email , " user : " , username ," IP: " , ip , " date: " , date) 
		newPost = Post(postID, threadID, parentID, email, username, ip, date, content)
		if threadID in table:
			table[threadID].append(newPost)

class Post:
	'Post Object which will work because I told it to'
	postNum = 0

	def __init__(self, post, threadID, parentID, authEmail, authUser, authIP, date, content):
		self.post = post
		self.threadID = threadID
		self.parentID = parentID
		self.authEmail = authEmail
		self.authUser = authUser
		self.authIP = authIP
		self.date = date
		self.content = content
		Post.postNum += 1



def main():
	tree = ET.parse('dump.xml')
	root = tree.getroot()
	table = createTable(root)
	buildDictionary(root, table)
	printCSV(table)

if __name__ == "__main__":
   	main()



