import urllib.request

# file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# https://py4e-data.dr-chuck.net/regex_sum_42.txt
# https://py4e-data.dr-chuck.net/comments_42.html

file_handler = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in file_handler:
    print(line.decode().strip())
# try:
#
# except urllib.error as err:
#     print(err)
