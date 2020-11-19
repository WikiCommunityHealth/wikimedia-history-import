from sys import argv
import json

INPUT = argv[1] + '.tsv'

OUTPUT_REVISIONS = "revisions.json"
OUTPUT_PAGES = "pages.json"
OUTPUT_USERS = "users.json"


def get_raw_obj(parts):
    (
        wiki_db,
        event_entity,
        event_type,
        event_timestamp,
        event_comment,

        event_user_id,
        event_user_text_historical,
        event_user_text,
        event_user_blocks_historical,
        event_user_blocks,
        event_user_groups_historical,
        event_user_groups,
        event_user_is_bot_by_historical,
        event_user_is_bot_by,
        event_user_is_created_by_self,
        event_user_is_created_by_system,
        event_user_is_created_by_peer,
        event_user_is_anonymous,
        event_user_registration_timestamp,
        event_user_creation_timestamp,
        event_user_first_edit_timestamp,
        event_user_revision_count,
        event_user_seconds_since_previous_revision,

        page_id,
        page_title_historical,
        page_title,
        page_namespace_historical,
        page_namespace_is_content_historical,
        page_namespace,
        page_namespace_is_content,
        page_is_redirect,
        page_is_deleted,
        page_creation_timestamp,
        page_first_edit_timestamp,
        page_revision_count,
        page_seconds_since_previous_revision,

        user_id,
        user_text_historical,
        user_text,
        user_blocks_historical,
        user_blocks,
        user_groups_historical,
        user_groups,
        user_is_bot_by_historical,
        user_is_bot_by,
        user_is_created_by_self,
        user_is_created_by_system,
        user_is_created_by_peer,
        user_is_anonymous,
        user_registration_timestamp,
        user_creation_timestamp,
        user_first_edit_timestamp,

        revision_id,
        revision_parent_id,
        revision_minor_edit,
        revision_deleted_parts,
        revision_deleted_parts_are_suppressed,
        revision_text_bytes,
        revision_text_bytes_diff,
        revision_text_sha1,
        revision_content_model,
        revision_content_format,
        revision_is_deleted_by_page_deletion,
        revision_deleted_by_page_deletion_timestamp,
        revision_is_identity_reverted,
        revision_first_identity_reverting_revision_id,
        revision_seconds_to_identity_revert,
        revision_is_identity_revert,
        revision_is_from_before_page_creation,
        revision_tags
    ) = parts

    return {
        "wiki_db": wiki_db,
        "event_entity": event_entity,
        "event_type": event_type,
        "event_timestamp": event_timestamp,
        "event_comment": event_comment,

        "event_user_id": event_user_id,
        "event_user_text_historical": event_user_text_historical,
        "event_user_text": event_user_text,
        "event_user_blocks_historical": event_user_blocks_historical,
        "event_user_blocks": event_user_blocks,
        "event_user_groups_historical": event_user_groups_historical,
        "event_user_groups": event_user_groups,
        "event_user_is_bot_by_historical": event_user_is_bot_by_historical,
        "event_user_is_bot_by": event_user_is_bot_by,
        "event_user_is_created_by_self": event_user_is_created_by_self,
        "event_user_is_created_by_system": event_user_is_created_by_system,
        "event_user_is_created_by_peer": event_user_is_created_by_peer,
        "event_user_is_anonymous": event_user_is_anonymous,
        "event_user_registration_timestamp": event_user_registration_timestamp,
        "event_user_creation_timestamp": event_user_creation_timestamp,
        "event_user_first_edit_timestamp": event_user_first_edit_timestamp,
        "event_user_revision_count": event_user_revision_count,
        "event_user_seconds_since_previous_revision": event_user_seconds_since_previous_revision,

        "page_id": page_id,
        "page_title_historical": page_title_historical,
        "page_title": page_title,
        "page_namespace_historical": page_namespace_historical,
        "page_namespace_is_content_historical": page_namespace_is_content_historical,
        "page_namespace": page_namespace,
        "page_namespace_is_content": page_namespace_is_content,
        "page_is_redirect": page_is_redirect,
        "page_is_deleted": page_is_deleted,
        "page_creation_timestamp": page_creation_timestamp,
        "page_first_edit_timestamp": page_first_edit_timestamp,
        "page_revision_count": page_revision_count,
        "page_seconds_since_previous_revision": page_seconds_since_previous_revision,

        "user_id": user_id,
        "user_text_historical": user_text_historical,
        "user_text": user_text,
        "user_blocks_historical": user_blocks_historical,
        "user_blocks": user_blocks,
        "user_groups_historical": user_groups_historical,
        "user_groups": user_groups,
        "user_is_bot_by_historical": user_is_bot_by_historical,
        "user_is_bot_by": user_is_bot_by,
        "user_is_created_by_self": user_is_created_by_self,
        "user_is_created_by_system": user_is_created_by_system,
        "user_is_created_by_peer": user_is_created_by_peer,
        "user_is_anonymous": user_is_anonymous,
        "user_registration_timestamp": user_registration_timestamp,
        "user_creation_timestamp": user_creation_timestamp,
        "user_first_edit_timestamp": user_first_edit_timestamp,

        "revision_id": revision_id,
        "revision_parent_id": revision_parent_id,
        "revision_minor_edit": revision_minor_edit,
        "revision_deleted_parts": revision_deleted_parts,
        "revision_deleted_parts_are_suppressed": revision_deleted_parts_are_suppressed,
        "revision_text_bytes": revision_text_bytes,
        "revision_text_bytes_diff": revision_text_bytes_diff,
        "revision_text_sha1": revision_text_sha1,
        "revision_content_model": revision_content_model,
        "revision_content_format": revision_content_format,
        "revision_is_deleted_by_page_deletion": revision_is_deleted_by_page_deletion,
        "revision_deleted_by_page_deletion_timestamp": revision_deleted_by_page_deletion_timestamp,
        "revision_is_identity_reverted": revision_is_identity_reverted,
        "revision_first_identity_reverting_revision_id": revision_first_identity_reverting_revision_id,
        "revision_seconds_to_identity_revert": revision_seconds_to_identity_revert,
        "revision_is_identity_revert": revision_is_identity_revert,
        "revision_is_from_before_page_creation": revision_is_from_before_page_creation,
        "revision_tags": revision_tags
    }


def parse_revision_obj(raw_obj):
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
        },

        "revision": {
            "id": raw_obj['revision_id'],
            "parent_id": raw_obj['revision_parent_id'],
            "minor_edit": raw_obj['revision_minor_edit'],
            "deleted_parts": raw_obj['revision_deleted_parts'],
            "deleted_parts_are_suppressed": raw_obj['revision_deleted_parts_are_suppressed'],
            "text_bytes": raw_obj['revision_text_bytes'],
            "text_bytes_diff": raw_obj['revision_text_bytes_diff'],
            "text_sha1": raw_obj['revision_text_sha1'],
            "content_model": raw_obj['revision_content_model'],
            "content_format": raw_obj['revision_content_format'],
            "is_deleted_by_page_deletion": raw_obj['revision_is_deleted_by_page_deletion'],
            "deleted_by_page_deletion_timestamp": raw_obj['revision_deleted_by_page_deletion_timestamp'],
            "is_identity_reverted": raw_obj['revision_is_identity_reverted'],
            "first_identity_reverting_revision_id": raw_obj['revision_first_identity_reverting_revision_id'],
            "seconds_to_identity_revert": raw_obj['revision_seconds_to_identity_revert'],
            "is_identity_revert": raw_obj['revision_is_identity_revert'],
            "is_from_before_page_creation": raw_obj['revision_is_from_before_page_creation'],
            "tags": raw_obj['revision_tags']
        }
    }


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


def parse_user_obj(raw_obj):
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

        "user": {
            "id": raw_obj['user_id'],
            "text_historical": raw_obj['user_text_historical'],
            "text": raw_obj['user_text'],
            "blocks_historical": raw_obj['user_blocks_historical'],
            "blocks": raw_obj['user_blocks'],
            "groups_historical": raw_obj['user_groups_historical'],
            "groups": raw_obj['user_groups'],
            "is_bot_by_historical": raw_obj['user_is_bot_by_historical'],
            "is_bot_by": raw_obj['user_is_bot_by'],
            "is_created_by_self": raw_obj['user_is_created_by_self'],
            "is_created_by_system": raw_obj['user_is_created_by_system'],
            "is_created_by_peer": raw_obj['user_is_created_by_peer'],
            "is_anonymous": raw_obj['user_is_anonymous'],
            "registration_timestamp": raw_obj['user_registration_timestamp'],
            "creation_timestamp": raw_obj['user_creation_timestamp'],
            "first_edit_timestam": raw_obj['user_first_edit_timestamp']
        }
    }


def parse_raw_obj(raw_obj):
    if raw_obj['event_entity'] == 'revision':
        return('revision', parse_revision_obj(raw_obj))
    elif raw_obj['event_entity'] == 'page':
        return('page', parse_page_obj(raw_obj))
    elif raw_obj['event_entity'] == 'user':
        return('user', parse_user_obj(raw_obj))


with open(INPUT, 'r') as file, open(OUTPUT_REVISIONS, 'w') as revisions, open(OUTPUT_PAGES, 'w') as pages, open(OUTPUT_USERS, 'w') as users:
    for line in file:
        remove_newline = line[0:(len(line) - 1)]
        parts = remove_newline.split('\t')
        raw_obj = get_raw_obj(parts)
        (type, result) = parse_raw_obj(raw_obj)
        if type == 'revision':
            revision = json.dumps(result)
            revisions.write(revision)
            revisions.write('\n')
        elif type == 'page':
            page = json.dumps(result)
            pages.write(page)
            pages.write('\n')
        elif type == 'user':
            user = json.dumps(result)
            users.write(user)
            users.write('\n')
