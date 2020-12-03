from dateutil import parser

def parse_str(value):
    return (value if value != '' else None)

def parse_date(value):
    return (parser.parse(value) if value != '' else None)

def parse_int(value):
    return (int(value) if value != '' else None)

def parse_bool(value):
    return True if value == "true" else (False if value == "false" else None)

def parse_str_array(value):
    return value.split(',') if value != '' else []