from functools32 import wraps
from blog.params import blog_params_v1
from jsonschema import validate, FormatChecker


# decorator to remove extra params of the form and perform form value modification if required
def process_params(*args, **kwargs):

    def deco(f):

        def extract_params(request):
            if request.method == 'POST':
                return dict(request.POST)
            else:
                return request.args

        # convert list to string if it has 1 element and remove csrf token
        def correct_params(params):
            for key, value in params.iteritems():
                if isinstance(value, list) and len(value) == 1:
                    params.update({key: value[0]})
            params.pop('csrfmiddlewaretoken')
            return params

        @wraps(f)
        def decorated_function(cls, request, *args, **kwargs):
            params = extract_params(request)
            corrected_params = correct_params(params)

            # perform validation on corrected params by comparing with predefined format
            validate(corrected_params, blog_params_v1, format_checker=FormatChecker())

            kwargs['params'] = corrected_params
            return f(cls, request, *args, **kwargs)

        return decorated_function

    return deco
