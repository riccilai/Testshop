from . import methods

class standard(methods.Base):
    code = 'standard'
    name = 'Standard shipping (free)'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('10.00'), incl_tax=D('12.00'))


