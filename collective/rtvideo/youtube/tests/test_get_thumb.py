from zope.interface import implements
from redturtle.video.interfaces import IVideoEmbedCode
from zope.component import getMultiAdapter
from redturtle.video.tests.base import TestRequest
from collective.rtvideo.youtube.tests.base import (RemoteVideo,
                                                  TestCase,
                                                  ShortUrlRemoteVideo)
from redturtle.video.browser.videoembedcode import ThumbObject
import unittest

class TestGetThumb(TestCase):
    
    def test_get_thumb_for_classic_url(self):
        """
        Try the method with classic youtube.com url
        """
        remote_video = RemoteVideo()
        adapter = getMultiAdapter((remote_video, TestRequest()),
                                   IVideoEmbedCode,
                                   name = 'youtube.com')
        
        video_id = 's43WGi_QZEE'
        thumb_obj = adapter.getThumb()
        
        self.assertEqual('image/jpeg',
                         thumb_obj.content_type)
        
        self.assertEqual('%s-image.jpg'%video_id,
                         thumb_obj.filename)
        
        self.assertEqual('http://img.youtube.com/vi/%s/0.jpg'%video_id,
                         thumb_obj.url)

        self.assertTrue(isinstance(thumb_obj, ThumbObject))
        
    def test_get_thumb_for_short_url(self):
        """
        Try the method with the short youtu.be url
        """
        remote_video = ShortUrlRemoteVideo()
        adapter = getMultiAdapter((remote_video, TestRequest()),
                                   IVideoEmbedCode,
                                   name = 'youtu.be')
        
        video_id = 's43WGi_QZEE'
        thumb_obj = adapter.getThumb()
        
        self.assertEqual('image/jpeg',
                         thumb_obj.content_type)
        
        self.assertEqual('%s-image.jpg'%video_id,
                         thumb_obj.filename)
        
        self.assertEqual('http://img.youtube.com/vi/%s/0.jpg'%video_id,
                         thumb_obj.url)

        self.assertTrue(isinstance(thumb_obj, ThumbObject))
        
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGetThumb))
    return suite