from .. import utils


NAME = "ogg"
MIME_TYPES = ["audio/ogg", "application/ogg", "video/ogg"]
'''Mime-types that are recognized as Ogg'''
EXTENSIONS = [".ogg"]
'''Valid Ogg file extensions.'''
OGG_V1 = "OGGv1"


def isVorbisFile(file_name):
    '''Does a mime-type check on ``file_name`` and returns ``True`` it the
    file is ogg, and ``False`` otherwise.'''
    return utils.guessMimetype(file_name) in MIME_TYPES


from .audio import *
