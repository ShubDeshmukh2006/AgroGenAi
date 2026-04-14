"""
Middleware for the authentication app.
"""

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.http import HttpResponse


class LanguageMiddleware(MiddlewareMixin):
    """
    Middleware to handle language preferences for users.
    """
    
    def process_request(self, request):
        """
        Process incoming request to set language preference.
        """
        # Get language from session, cookie, or accept-language header
        language = request.session.get('language')
        
        if not language:
            # Try to get from cookie
            language = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
        
        if not language:
            # Fall back to default language
            language = settings.LANGUAGE_CODE
        
        # Set the language on the request
        request.language = language
        
        return None
