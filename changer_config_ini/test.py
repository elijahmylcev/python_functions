import configparser

def update_ini_file(file_path, section, parameter, value):
    config = configparser.ConfigParser()
    config.read(file_path)
    config.set(section, parameter, value)
    config.set(section, 'key', 'value')
    with open(file_path, 'w') as config_file:
        config.write(config_file)
        

def update_config(config, updates_dict):
    for key in updates_dict:
        if key in config.sections():
            for k in updates_dict[key]:
                config[key][k] = updates_dict[key][k]
        else:
            config.add_section(key)
            for k in updates_dict[key]:
                config[key][k] = updates_dict[key][k]
    return config

config = configparser.ConfigParser()
config.read('./changer_config_ini/test.ini')

updates = {
    'first_sec': {
        'param1': 'test_for_param1',
        'param2': 'test_for_param2',
        'param3': 'test_for_param3'
    },
    'second_sec' : {
        'second_section_key': 'second_section_value',
        'second_section_key2': 'second_section_value2'
    },
    'section3': {
        'l': 'k'
    }

}

config = update_config(config, updates)

with open('./changer_config_ini/test.ini', 'w') as f:
    config.write(f)
    