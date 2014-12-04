#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from pages.base import Base


class WhatsNextPage(Base):

    @property
    def _page_title(self):
        return "What's next? | Mozilla One and Done"
