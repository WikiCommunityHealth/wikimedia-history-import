from .parse_page import parse_page_obj
from .parse_revision import parse_revision_obj
from .parse_user import parse_user_obj

def parse_raw_obj(raw_obj):
    if raw_obj['event_entity'] == 'revision':
        return('revision', parse_revision_obj(raw_obj))
    elif raw_obj['event_entity'] == 'page':
        return('page', parse_page_obj(raw_obj))
    elif raw_obj['event_entity'] == 'user':
        return('user', parse_user_obj(raw_obj))
