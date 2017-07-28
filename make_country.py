
import ConfigParser
from bs4 import BeautifulSoup
import urllib2


class CountryCode(object):



    def make_country_name(self):

        url = ('https://countrycode.org/')

        page = urllib2.urlopen(url).read()

        soup = BeautifulSoup(page)

        table = soup.find('table')

        x = (len(table.findAll('tr')) - 1)

        self.parser = ConfigParser.RawConfigParser()
        self.parser.add_section('COUNTRYCODE')

        for row in table.findAll('tr')[1:x]:
            col = row.findAll('td')
            self.parser.set('COUNTRYCODE', '%s' % col[0].getText(), '%s' % col[2].getText()[0:2])

        with open('country.ini', 'wb') as f:
            self.parser.write(f)

if __name__ == "__main__":

    country = CountryCode()
    country.make_country_name()



