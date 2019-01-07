from voluptuous import Schema, Required

CREATE_SCHEMA = Schema({
    Required("name"): str,
    Required("user_id"): str
})
EDIT_SCHEMA = Schema({
    Required("name"): str,
    Required("user_id"): str
})