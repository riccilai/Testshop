from decimal import Decimal as D

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

from oscar.core.loading import get_classes

(Free, NoShippingRequired,
 TaxExclusiveOfferDiscount, TaxInclusiveOfferDiscount) \
    = get_classes('shipping.methods', ['standard', 'NoShippingRequired',
                                       'TaxExclusiveOfferDiscount', 'TaxInclusiveOfferDiscount'])

# from oscar.apps.shipping import repository
from oscar.core.loading import get_class

Repository = get_class('shipping.repository', 'Repository')

from . import methods

class Repository(repository.Repository):
    methods = (methods.Standard(), methods.Express())

