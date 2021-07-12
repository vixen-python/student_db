import os


def upload_to_student_dir(instance, filename):
    """
    Generate relative path from "MEDIA_ROOT" to uploaded file for students.

    Example:

        :param instance: MediaData object
        :param filename: file name of uploaded file
        :return: file system path
    """
    #{MEDIA_ROOT}/student/{student_id}/{filename}
    return os.path.join(
        'students',
        str(instance.student_id),
        filename
    )