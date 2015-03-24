from zope.annotation import IAnnotations

ANNOTATIONS_KEY = 'collective.customlogin.success'


def update_challenge_status(request, status):
    IAnnotations(request)[ANNOTATIONS_KEY] = status


def get_challenge_status(request):
    return IAnnotations(request).get(ANNOTATIONS_KEY)
