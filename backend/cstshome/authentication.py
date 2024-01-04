from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    """
    Overrides 'Token' keyword for token header.
    """
    keyword = 'Bearer'
