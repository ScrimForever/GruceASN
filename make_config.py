import ConfigParser

parser = ConfigParser.RawConfigParser()

parser.add_section('CONFIG')
parser.set('CONFIG', 'FTP', 'ftp.lacnic.net')
parser.add_section('CONTINENTS')
parser.set("CONTINENTS", 'AFRINIC','/pub/stats/afrinic')
parser.set("CONTINENTS", 'APINIC', '/pub/stats/apnic')
parser.set("CONTINENTS", 'ARIN','/pub/stats/arin')
parser.set("CONTINENTS", 'LACNIC','/pub/stats/lacnic')
parser.set("CONTINENTS", 'RIPENCC','/pub/stats/ripencc')
with open('config.ini', 'wb') as cf:
    parser.write(cf)



