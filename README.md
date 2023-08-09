# Login-Logout-API
Knox authentication is token based and is very similar to the TokenAuthentication that built in to the DRF. However, it overcomes some problems present in the default implementation.

As with the default TokenAuthentication that comes with DRF, tokens are unencrypted in the database . If somehow our database gets compromise or by any chance the attackers steal all the database data including tokens, they would be able to log in with the stolen credentials (tokens).

DRF tokens track their creation time, but have no inbuilt mechanism for tokens expiring. Knox tokens can have an expiry configured in the app settings (default is 10 hours.)

*Installing Knox
Knox should be installed with pip
pip install django-rest-knox

*Setup knox
Add rest_framework and knox to your INSTALLED_APPS, remove rest_framework.authtoken if you were using it.
Make knox’s TokenAuthentication as our default authentication class for django-rest-framework: 
INSTALLED_APPS = [
  ...
  'rest_framework',
  'knox',
  ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':'knox.auth.TokenAuthentication',),
    ...
}

*Summary: Django-rest-knox library provides models and views to handle token-based authentication in a more secure and extensible way than the built-in TokenAuthentication scheme — with Single Page Applications and Mobile clients in mind.

It provides per-client tokens, and views to generate them when provided some other authentication (usually basic authentication), to delete the token (providing a server enforced logout) and to delete all tokens (logs out all clients that a user is logged into).
