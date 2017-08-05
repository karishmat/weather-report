__author__ = 'karishma'
from model_utils import Choices


MONTHS = Choices(('JAN', 'JAN'),
                 ('FEB', 'FEB'),
                 ('MAR', 'MAR'),
                 ('APR', 'APR'),
                 ('MAY', 'MAY'),
                 ('JUN', 'JUN'),
                 ('JUL', 'JUL'),
                 ('AUG', 'AUG'),
                 ('SEP', 'SEP'),
                 ('OCT', 'OCT'),
                 ('NOV', 'NOV'),
                 ('DEC', 'DEC'),
                 )

SEASONS = Choices(('WIN', 'WIN'),
                 ('SPR', 'SPR'),
                 ('SUM', 'SUM'),
                 ('AUT', 'AUT'),
                 ('ANN', 'ANN'))