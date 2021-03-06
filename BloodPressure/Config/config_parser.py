import configparser


class MyConfigParser:
    def __init__(self):
        self._parser = configparser.ConfigParser()

    @staticmethod
    def change_config(database_name):
        cfgfile = open("/home/londra/Downloads/ComputerArchitecture-master/BloodPressure/Config/config.ini", 'w')
        config = configparser.ConfigParser()
        # add the settings to the structure of the file, and lets write it out
        if not config.has_section('database'):
            config.add_section('database')
        config.set('database', 'name', database_name)
        config.write(cfgfile)
        cfgfile.close()
        print("Config has changed successfully!!")


    def read_config(self):
        try:
            self._parser.read('/home/londra/Downloads/ComputerArchitecture-master/BloodPressure/Config/config.ini')
            return self._parser.get('database', 'name')
        except configparser.ParsingError:
            print('Could not parse:')
