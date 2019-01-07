from voluptuous import Schema, Required

CREATE_SCHEMA = Schema({
    Required("username"): str,
    Required("password"): str,
    Required("name"): str
})

LOGIN_SCHEMA = Schema({
    Required("username"): str,
    Required("password"): str,
})

EDIT_SCHEMA = Schema({
    Required("password"): str,
    Required("name"): str
})
