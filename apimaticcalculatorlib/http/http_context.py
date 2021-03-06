# -*- coding: utf-8 -*-

"""
    apimaticcalculatorlib.http.http_context

    This file was automatically generated by APIMATIC BETA v2.0 on 09/28/2016
"""

from .http_request import HttpRequest
from .http_response import HttpResponse

class HttpContext(object):

    """An HTTP Context that contains both the original HttpRequest
    object that intitiated the call and the HttpResponse object that
    is the result of the call.

    Attributes:
        request (HttpRequest): The original request object.
        response (HttpResponse): The returned response object after
            executing the request. Note that this may be None
            depending on if and when an error occurred.
    
    """

    def __init__(self,
                 request,
                 response):
        """Constructor for the HttpContext class
        
        Args:
            request (HttpRequest): The HTTP Request.
            response (HttpResponse): The HTTP Response.
        
        """
        self.request = request
        self.response = response
