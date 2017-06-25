import urllib

epnum = raw_input('Episode Number? ')
baseurl = ('https://media.grc.com/sn/sn-' + epnum + '.mp3')
downloading = 'Downloading please wait...'
filename = r'D:\amd8320\Music\Security Now\sn' + epnum + '.mp3'

print downloading
urllib.urlretrieve(baseurl, filename)
