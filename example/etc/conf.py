# -*- coding: utf-8 -*-

from saml2 import BINDING_PAOS
from saml2 import BINDING_HTTP_ARTIFACT
from saml2 import BINDING_HTTP_POST
from saml2 import BINDING_HTTP_REDIRECT
from saml2.sigver import get_xmlsec_binary

try:
    XMLSEC_BINARY = get_xmlsec_binary(["/opt/local/bin"])
except Exception:
    XMLSEC_BINARY = "/usr/bin/xmlsec1"

PORT = 8087

# Base URL for the service
BASE = "http://localhost:{port}".format(port=PORT)

# Base directory for needed files

CONFIG = {
    "entityid": "%s/sp.xml" % BASE,
    "name": "SAML2 test tool",
    "description": "Simplest possible",
    "service": {
        "sp": {
            "allow_unsolicited": True,
            "authn_requests_signed": "true",
            "endpoints": {
                "assertion_consumer_service": [
                    ("%s/acs/post" % BASE, BINDING_HTTP_POST),
                    ("%s/acs/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/acs/artifact" % BASE, BINDING_HTTP_ARTIFACT),
                    ("%s/ecp" % BASE, BINDING_PAOS),
                    (BASE, BINDING_HTTP_POST),  # Fake
                ],
            }
        }
    },
    "key_file": "./keys/mykey.pem",
    "cert_file": "./keys/mycert.pem",
    "xmlsec_binary": XMLSEC_BINARY,
    "accepted_time_diff": 60,
    "metadata": {"local": ["./idp.xml"]},
    "secret": "0123456789",
    "only_use_keys_in_metadata": False,
    "logger": {
        "rotating": {
            "filename": "/opt/idp_monitor/etc/idp_monitor.log",
            "maxBytes": 500000,
            "backupCount": 5,
        },
        "loglevel": "debug",
    }
}

# The base URL for the IdP
IDPBASE = "http://my.idp.com:8089"
MYSELF = "http://localhost:{port}/acs/post".format(port=PORT)

# This part describes when the 'user'/browser should do things.
INTERACTION = [
    # The login page and which fields that should be filled in
    {
        "matches": {
            "url": "%s/sso/redirect" % IDPBASE,
            "title": 'IDP test login'
        },
        "page-type": "login",
        "control": {
            "type": "form",
            "set": {"login": "testuser", "password": "qwerty"}
        }
    },
    # The form response from the IdP that should be automagically posted
    {
        "matches": {
            "url": "%s/sso/redirect" % IDPBASE,
            #"title": "SAML 2.0 POST"
        },
        "page-type": "other",
        "control": {
            "index": 0,
            "type": "form",
        }
    },
    {
        "matches": {
            "url": MYSELF,
            "title": "SAML 2.0 POST"
        },
        "page-type": "other",
        "control": {
            "index": 0,
            "type": "form",
        }
    },]