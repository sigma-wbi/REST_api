import json_log_formatter
from django.http import HttpRequest
from logging import LogRecord
from time import localtime, strftime
import hashlib


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):

    def json_record(self, message: str, extra: dict, record: LogRecord) -> dict:
        request: HttpRequest = extra.get('request')
        extra.pop('request', None)
        if not request:
            return extra
        extra['url'] = request.get_full_path()
        extra['method'] = request.method
        user_id = request.user.id
        extra['user_id'] = hashlib.sha256(f'{user_id}'.encode('ascii')).hexdigest()
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
        
    def to_json(self, record):
        """Converts record dict to a JSON string.

        It makes best effort to serialize a record (represents an object as a string)
        instead of raising TypeError if json library supports default argument.
        Note, ujson doesn't support it.
        ValueError and OverflowError are also caught to avoid crashing an app,
        e.g., due to circular reference.

        Override this method to change the way dict is converted to JSON.

        """
        try:
            return self.json_lib.dumps(record, default=json_log_formatter._json_serializable, ensure_ascii=False)
        # ujson doesn't support default argument and raises TypeError.
        # "ValueError: Circular reference detected" is raised
        # when there is a reference to object inside the object itself.
        except (TypeError, ValueError, OverflowError):
            try:
                return self.json_lib.dumps(record, ensure_ascii=False)
            except (TypeError, ValueError, OverflowError):
                return '{}'