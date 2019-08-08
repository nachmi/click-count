#!/usr/bin/env python

import os
import requests
from requests.auth import HTTPBasicAuth

NEXUS_BASE_URL = 'http://localhost:8081'
NEXUS_URL_SUFFIX = '/service/rest/v1/search/assets/download'
NEXUS_URL_ARGUMENTS = '?sort=version\
&repository=maven-snapshots\
&group=fr.xebia\
&maven.artifactId=clickCount\
&maven.baseVersion=1.0-SNAPSHOT\
&maven.extension=war'


NEXUS_URL = NEXUS_BASE_URL + NEXUS_URL_SUFFIX + NEXUS_URL_ARGUMENTS


resp = requests.get(
    NEXUS_URL,
    auth=HTTPBasicAuth(os.environ['NEXUS_USER'], os.environ['NEXUS_PASSWORD'])
)

if resp.status_code == 200:
    with open('clickCount.war', 'w') as output:
        output.write(resp.content)
else:
    print('ERROR : No file to download.')
