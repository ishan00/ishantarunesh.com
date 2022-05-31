html = """
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
			<div class="row"> 
				<div class="col-md-2">  
				</div>
				<div class="col-md-8">
					<div style="margin-top:30px">
						<h1 style="text-align: center;">Thoughts and Worries</h1>
						<hr class="hr-1">
						<br>
						<br>

						INDEX

						<br>
						<hr>

						CONTENT

					</div>
				</div>
				<div class="col-md-2">  
				</div>
			</div>
		</div>

		</div>
	</body>
</html>
"""

make_index = False

posts = [
	'hesitate-writing-goals',
	'humiliations-that-stick',
	'insidious-addictions'
]

index = ""
content = ""

for post in posts:
	file = open('posts/' + post + '.html')
	lines = file.read()
	content += lines
	content += '\n<hr>\n\n'

html = html.replace('INDEX', index).replace('CONTENT', content)

with open('blog.html', 'w') as f:
	f.write(html)