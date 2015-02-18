import urllib.request, urllib.parse, urllib.error
import json
from django.utils.html import strip_tags


def AlchemyKeywordGeneration(object, content, API_KEY, defaults=False):
    '''
    Function for saving and storing meta keywords for a model.
    Call function before super save on save operation.

    object - The object being saved. Passed in as self
    content - String. Body copy field that keywords will be extracted from.
    API_KEY - String. API key for AlchemyApi.com
    defaults - Array. Contains any additional keywords that should be stored, regardless of object content.

    Example (SEO keywords stored in field seo_keywords and content from field copy):
    def save(self, *args, **kwargs):
        from conf.settings import API_KEY
        self.seo_keywords = AlchemyKeywordGeneration(self, self.body, API_KEY, ('keyword 1', 'keyword 2', 'keyword 3'))
        super(MyModel, self).save(*args, **kwargs)

    '''

    def content_clean(content):
        # Strips HTML tags from the content
        return strip_tags(content).encode('utf-8')

    # If the object is not new (and hence has a primary key), return.
    # Operation only runs on initial save
    if object.pk:
        return

    # Sanitize the content
    clean_content = content_clean(content)

    POSTDATA = urllib.parse.urlencode({
        "apikey": API_KEY,
        "text": clean_content,
        "outputMode": "json"
    })

    response = urllib.request.urlopen("http://access.alchemyapi.com/calls/text/TextGetRankedKeywords", POSTDATA)
    keywords = json.loads(response.read())['keywords']

    meta_keywords_to_save = []

    if defaults:
        meta_keywords_to_save.extend(defaults)

    for keyword in keywords:
        if float(keyword['relevance']) > 0.6:
            meta_keywords_to_save.append(keyword['text'])

    return ', '.join(meta_keywords_to_save)
