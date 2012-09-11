Introduction
============

This is an add-on adapter for `RedTurtle Video`__ product for Plone. For additional documentation see
the main product's page.

Add this to your Plone installation for beeing able to use `YouTube`__ video link as valid
URLs for "Video link" content type.

__ http://plone.org/products/redturtle.video
__ http://www.youtube.com/

Valid URL formats
=================

Classic URL is supported::

    http://www.youtube.com/watch?v=f7OLg1AZvr4&...otherparams

Also the shortened version can be used::

    http://youtu.be/f7OLg1AZvr4

Autoplay
--------

You can enabled the YoutTube video autoplay in two ways:

* Use the YouTube ``autoplay=1`` parameter in the remote YouTube video
  you are saving in Plone.
  
  This is a permanent autoplay (the editor choose to autoplay the video)
* Call the RedTurtle video content with the ``autoplay=1`` parameter.
  
  This is a user choice autoplay (who links the Plone content choose to auto
  start it)
