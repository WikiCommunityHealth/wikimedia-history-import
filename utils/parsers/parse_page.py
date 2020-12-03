def parse_page_obj(raw_obj):
    return {
        "wiki_db": raw_obj['wiki_db'],
        "event_entity": raw_obj['event_entity'],
        "event_type": raw_obj['event_type'],
        "event_timestamp": raw_obj['event_timestamp'],
        "event_comment": raw_obj['event_comment'],

        "event_user": {
            "id": raw_obj['event_user_id'],
            "text_historical": raw_obj['event_user_text_historical'],
            "text": raw_obj['event_user_text'],
            "blocks_historical": raw_obj['event_user_blocks_historical'],
            "blocks": raw_obj['event_user_blocks'],
            "groups_historical": raw_obj['event_user_groups_historical'],
            "groups": raw_obj['event_user_groups'],
            "is_bot_by_historical": raw_obj['event_user_is_bot_by_historical'],
            "is_bot_by": raw_obj['event_user_is_bot_by'],
            "is_created_by_self": raw_obj['event_user_is_created_by_self'],
            "is_created_by_system": raw_obj['event_user_is_created_by_system'],
            "is_created_by_peer": raw_obj['event_user_is_created_by_peer'],
            "is_anonymous": raw_obj['event_user_is_anonymous'],
            "registration_timestamp": raw_obj['event_user_registration_timestamp'],
            "creation_timestamp": raw_obj['event_user_creation_timestamp'],
            "first_edit_timestamp": raw_obj['event_user_first_edit_timestamp'],
            "revision_count": raw_obj['event_user_revision_count'],
            "seconds_since_previous_revision": raw_obj['event_user_seconds_since_previous_revision'],
        },

        "page": {
            "id": raw_obj['page_id'],
            "title_historical": raw_obj['page_title_historical'],
            "title": raw_obj['page_title'],
            "namespace_historical": raw_obj['page_namespace_historical'],
            "namespace_is_content_historical": raw_obj['page_namespace_is_content_historical'],
            "namespace": raw_obj['page_namespace'],
            "namespace_is_content": raw_obj['page_namespace_is_content'],
            "is_redirect": raw_obj['page_is_redirect'],
            "is_deleted": raw_obj['page_is_deleted'],
            "creation_timestamp": raw_obj['page_creation_timestamp'],
            "first_edit_timestamp": raw_obj['page_first_edit_timestamp'],
            "revision_count": raw_obj['page_revision_count'],
            "seconds_since_previous_revision": raw_obj['page_seconds_since_previous_revision'],
        }
    }

