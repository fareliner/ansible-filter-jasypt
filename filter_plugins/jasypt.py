from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# https://github.com/fareliner/jasypt4py/issues/3#issuecomment-1058722911
# Resolve time.clock problem
import time
time.clock = time.time


from ansible.errors import AnsibleError

try:
    from jasypt4py import StandardPBEStringEncryptor
    HAS_LIB = True
except ImportError:
    HAS_LIB = False

def jasypt_encrypt(value, algorithm, password, iterations):
    crypter = StandardPBEStringEncryptor(algorithm)
    return crypter.encrypt(password, value, iterations)

def jasypt_decrypt(value, algorithm, password, iterations):
    crypter = StandardPBEStringEncryptor(algorithm)
    return crypter.decrypt(password, value, iterations)

class FilterModule(object):
    ''' Jasypt en/decryption filters '''

    def filters(self):
        if not HAS_LIB:
            raise AnsibleError(
                'You need to install "jasypt4py" prior to running '
                'jasypt filter'
            )

        return {
            'jasypt_encrypt': jasypt_encrypt,
            'jasypt_decrypt': jasypt_decrypt
        }
