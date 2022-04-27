import xml.etree.ElementTree as ET

input_str = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>
'''

stuff = ET.fromstring(input_str)

# Returns list containing all matching elements in document order.
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('\tId:', item.find('id').text)
    print('\tAttribute:', item.get('x'))
