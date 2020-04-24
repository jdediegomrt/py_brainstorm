import logging

logger = logging.getLogger(__name__)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def verify_request_contains_required_parameters(request, *parameters):
    missing_parameters = list()
    for parameter in parameters:
        if request.GET.get(parameter) is None:
            missing_parameters.append(parameter)
    if len(missing_parameters) > 0:

        raise Exception('Missing required parameters: {}'.format(', '.join(missing_parameters)))

    return missing_parameters
