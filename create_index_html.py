import os

base_url = 'http://ansible.threatfax.com/graphs/'

with open('html/index.html', 'w') as index_file:
    for filename in os.listdir('html'):
        symbol = filename.split(".")[0]
        clean_name = str.rstrip(filename)
        index_file.write("<a href=" + base_url + clean_name + ">" + symbol + "</a> \n")
        index_file.write("<br>")
