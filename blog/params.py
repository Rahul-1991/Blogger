# used to perform param validation for proper format of form submission

blog_params_v1 = {
    'type': 'object',
    'properties': {
        'content': {
            'type': 'string'
        }
    },
    'additionalProperties': False
}
