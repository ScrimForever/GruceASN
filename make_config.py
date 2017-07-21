import ConfigParser

parser = ConfigParser.RawConfigParser()

parser.add_section('CONFIG')
parser.set('CONFIG', 'FTP', 'ftp.lacnic.net')
parser.add_section('CONTINENTS')
parser.set("CONTINENTS", 'AFRINIC','0')
parser.set("CONTINENTS", 'APINIC','0')
parser.set("CONTINENTS", 'ARIN','0')
parser.set("CONTINENTS", 'LACNIC','1')
parser.set("CONTINENTS", 'RIPENCC','0')
parser.add_section('')

with open('config.ini', 'wb') as cf:
    parser.write(cf)


