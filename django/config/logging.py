import json_log_formatter
from django.http import HttpRequest
from logging import LogRecord
from time import localtime, strftime


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):

    def json_record(self, message: str, extra: dict, record: LogRecord) -> dict:
        request: HttpRequest = extra.get('request')
        extra.pop('request', None)
        if not request:
            return extra
        extra['url'] = request.get_full_path()
        extra['method'] = request.method
        extra['user_id'] = request.user.id
        extra['username'] = request.user.get_username()
        extra['REMOTE_ADDR'] = request.META.get('REMOTE_ADDR', None)

        local_time = localtime(record.created)
        extra['created'] = strftime('%x %X', local_time)
        extra['logger'] = record.name
        extra['message'] = message
        extra['levelname'] = record.levelname

        data = dict(request.data)
        data.pop('csrfmiddlewaretoken', None)
        data.pop('password', None)
        data.pop('password1', None)
        data.pop('password2', None)
        extra.update(data)

        return extra
        