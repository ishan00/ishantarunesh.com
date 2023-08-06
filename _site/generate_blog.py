import os

html_main = """
<!DOCTYPE html>
<html lang="en-US">
<head>
	<title>Thoughts and Worries</title>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel=stylesheet href=https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css integrity="sha256-+N4/V/SbAFiW1MPBCXnfnP9QSN3+Keu+NlB+0ev/YKQ=" crossorigin=anonymous>
	<link rel="stylesheet" href="bootstrap.min.css">
	<link href="style.css" rel="stylesheet" type="text/css" media="screen" />

	<style>

		.hr-1 {
			height: 10px;
			background: url(hr-1.jpg) no-repeat center;
			border: none;
		}
		.hr-2 {
			height: 15px;
			background: url(hr-2.jpg) no-repeat center;
			border: none;
		}

	</style>

</head>
<body style="background-color: #FEF2CC;">

	<div id="home" class="container-fluid">
		<div style="margin-top:30px">
			<h1 style="text-align: center;">Thoughts and Worries</h1>
			<hr class="hr-1">
			<br>
		</div>

		INDEX

		CONTENT

	</div>

</div>
</body>
</html>
"""

html_index = """
<div class="row">
	<div class="col-md-3">
	</div>
	<div class="col-md-6">
		<h4 style="text-align: center;">Contents</h3>
			<ul>
				LIST
			</ul>
		<br>

	</div>
</div>

"""

html_blog = """
<div class="row"> 
	<div class="col-md-2">  
	</div>
	<div class="col-md-8">
		POSTS
	</div>
	<div class="col-md-2">  
	</div>
</div>
"""

html_post = """
<hr>
<h4 id=ID>TITLE</h4>
<span class="date">DATE</span><br><br>

BODY
"""

def read_post(file):

	post = {}

	with open(file) as f:
		lines = f.readlines()
		post["title"] = lines[0][6:].strip()
		post["date"] = lines[1][5:].strip()
		post["body"] = '\n'.join(lines[3:])

	return post

list_of_posts = os.listdir('posts')
list_of_posts = sorted(list_of_posts, reverse = True)

print (list_of_posts)

index = ""
posts = ""

for i, post in enumerate(list_of_posts):
	parsed = read_post('posts/' + post)
	index += '<li><a href="#' + str(i) + '"' + ">" + parsed['title'] + '</a><span style="float:right">' + parsed['date'] + '</span></li>\n'
	posts += html_post.replace("TITLE", parsed['title']).replace("DATE", parsed['date']).replace("BODY", parsed['body']).replace("ID", str(i))

html_main = html_main.replace('INDEX', html_index.replace('LIST', index)).replace('CONTENT', html_blog.replace('POSTS',posts))

with open('blog.html', 'w') as f:
	f.write(html_main)