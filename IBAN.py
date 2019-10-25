#! /usr/bin/env python3

# IBAN
# https://programmingpraxis.com/2019/10/25/iban/

IBAN_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

class IBAN(object):
    """International Bank Account Number"""

    def __init__(self, iban):
        self.iban = self.normalise(iban)
        self.country_code = self.iban[:2]
        self.hash_code = self.iban[2:4]
        self.account_details = self.iban[4:]

    def __repr__(self):
        return f"IBAN.IBAN('{self.iban}')"

    def __str__(self):
        chunks = [self.iban[i:i+4] for i in range(0, len(self.iban), 4)]
        return ' '.join(chunks)

    def __eq__(self, other):
        return self.iban == other.iban

    def is_valid(self):
        istr = self.iban[4:] + self.iban[:4]
        istr = self.alpha_to_num(istr)
        chk = int(istr) % 97
        return chk == 1

    @classmethod
    def from_details(cls, country_code, details):
        iban = cls.normalise(details + country_code) + '00'
        istr = cls.alpha_to_num(iban)
        chk = 98 - (int(istr) % 97)
        iban = iban[-4:-2] + str(chk) + iban[:-4]
        return cls(iban)

    @staticmethod
    def normalise(iban):
        return ''.join(i for c in iban if (i := c.upper()) in IBAN_CHARS)

    @staticmethod
    def alpha_to_num(iban):
        return ''.join(c if c.isdigit() else str(ord(c)-55) for c in iban)
