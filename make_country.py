
import ConfigParser
import afrinic_treatment


class CountryCode(object):

    def make_country_name(self):
        self.parser = ConfigParser.RawConfigParser()
        self.parser.read('config.ini')
        self.itens = self.parser.items('DIR_LOC')
        return self.itens

        """
        afrinic = afrinic_treatment.AfrinicTreatment()
        afrinic.
        """

    def make_afrinic_file_config(self, name, date):
        f = open("%s_%s.txt" % (name, date[-8:]), 'r')
        countrycode = []
        try:
            for i in f.readlines():
                k = i.split('|')
                if k[1] not in countrycode:
                    countrycode.append(k[1])
        except Exception as e:
            print e




if __name__ == "__main__":

    countryname = CountryCode()
    countrylist = countryname.make_country_name()
    for i in countrylist:
        print i[0]
        print i[1]
        makefile = countryname.make_afrinic_file_config(i[0],i[1])
        break