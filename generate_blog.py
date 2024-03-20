from datetime import datetime
date_string = datetime.today().strftime('%Y-%m-%d')

print ("Enter permalink")
permalink = input(">")

f = open('_posts/%s-%s.md'%(date_string, permalink), 'w')
f.write("""---
title: 
layout: post
date: %s %s +0530
tags: 
permalink: %s
---
"""%(date_string, datetime.now().strftime("%H:%M"), permalink))
f.close()