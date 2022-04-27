import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
'''

# https://py4e-data.dr-chuck.net/comments_42.xml

# Parse XML document from string constant
tree = ET.fromstring(data)
print('type(tree) ->', type(tree))  # <class 'xml.etree.ElementTree.Element'>

# Return the first matching element, or None if no element was found.
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
