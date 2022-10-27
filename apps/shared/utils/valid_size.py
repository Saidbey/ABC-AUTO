from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value


def validate_img_size(value):
    filesize = value.size

    if filesize > 2621440:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value
