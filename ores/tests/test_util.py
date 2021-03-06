import time
import re

from nose.tools import raises

from ..errors import TimeoutError
from ..util import timeout


def test_timeout():
    timeout(int, 5, seconds=0.5)


@raises(TimeoutError)
def test_timeout_error():
    timeout(time.sleep, 2, seconds=1)


@raises(TimeoutError)
def test_timeout_error_badfunc():
    # This regex causes a near-infinite loop, should timeout
    # See https://wikitech.wikimedia.org/wiki/Incident_documentation/20170623-ORES
    bad_re = re.compile('(j+[aeiou]*)*(\\b)', re.I)
    edit = "JAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJputoAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJgayAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJcasamelaAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJJAJAJJAJAJAJAJAJAJlentos, y se hacen visibles con el paso de los años. El medio físico condiciona desigualmente los grupos humanos." # noqa : E501

    timeout(bad_re.match, edit, seconds=2)
