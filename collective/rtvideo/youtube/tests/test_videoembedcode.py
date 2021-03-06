# -*- coding: utf-8 -*-

import unittest
from zope.testing import doctest
import collective.rtvideo.youtube.browser.videoembedcode

import zope.component
import redturtle.video.interfaces

import zope.interface
from zope.traversing.adapters import DefaultTraversable
from zope.traversing.interfaces import ITraversable


def setUp(test):

    zope.component.provideAdapter(
            DefaultTraversable,
            (zope.interface.Interface,),
            provides=ITraversable
        )
    
    zope.component.provideAdapter(
            collective.rtvideo.youtube.browser.videoembedcode.ClassicYoutubeEmbedCode,
            (redturtle.video.interfaces.IRTRemoteVideo,
             zope.publisher.interfaces.browser.IHTTPRequest),
            provides=redturtle.video.interfaces.IVideoEmbedCode,
            name='youtube.com'
        )

    zope.component.provideAdapter(
            collective.rtvideo.youtube.browser.videoembedcode.ShortYoutubeEmbedCode,
            (redturtle.video.interfaces.IRTRemoteVideo,
             zope.publisher.interfaces.browser.IHTTPRequest),
            provides=redturtle.video.interfaces.IVideoEmbedCode,
            name='youtu.be'
        )


def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite(collective.rtvideo.youtube.browser.videoembedcode,
                     setUp=setUp,
                     optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,),
        ))
