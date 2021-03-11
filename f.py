# students=["jyoti","navya","pranjali","veda"]
# with open("navgurukul.html","w") as f:
#     f.write("<html>\n")
#     f.write("<head>\n")
#     f.write("<title> this is html page </title>")
#     f.write("</head>\n")
#     f.write("<body>\n")
#     f.write("<ul>\n")
#     i=0
#     while i<len(students):
#         f.write("<li>"+students[i]+"</li>\n")
#         i=i+1
#     f.write("</ul>")
#     f.write("</body>")
#     f.write("</html>")

import json
with open("Top_Rated_Movies.json","r") as f:
    movies=json.load(f)

with open("movies.html","w") as f:
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<title>This is movies list </title>")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<table>\n")
    f.write("<tr>\n")
    f.write("<th>"+" movies name"+"</th>")
    f.write("<th>"+"movies position"+"</th>")
    f.write("<th>"+"movies url"+"</th>")
    f.write("<th>"+"movies year"+"</th>")
    f.write("<th>"+"movies rating"+"</th>")
    f.write("</tr>")
    i=0
    while i<len(movies):
        f.write("<tr>\n")
        f.write("<td>"+movies[i]['name']+"</td>")
        f.write("<td>"+str(movies[i]['year'])+"</td>")
        f.write("<td>"+str(movies[i]['position'])+"</td>")
        f.write("<td>"+str(movies[i]['Rating'])+"</td>")
        f.write("<td>"+movies[i]['url']+"</td>")
        f.write("</tr>")
        i=i+1

    f.write("</body>")
    f.write("</html>")




