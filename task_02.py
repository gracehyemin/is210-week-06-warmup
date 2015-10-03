#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module interacts with first module."""

import data


BALLETS = data.BALLETS
del BALLETS[11]
BALLETS[1] = 'Swan Lake'
BALLETS.append('Herman Schmerman')
BALLETS.extend(['Don Quixote', 'Sylvia'])
