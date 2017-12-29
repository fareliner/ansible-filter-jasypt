# Ansible Filter: Jasypt

This module provides custom Ansible filter to de/encrypt string values.

## Requirements

None

## Filter Variables

`algorithm` - the encryption algorithm to be used

`password` - the encryption password

`iterations` - the number of iterations used for generating the key material


## Dependencies

The python library `jasypt4py` must be installed.

## Example Playbook

```yaml
- hosts: all
  connection: local
  gather_facts: no
  vars:
    algo: PBEWITHSHA256AND256BITAES-CBC
    iterations: 2000
    passcode: 'pssst password'
  roles:
  - ansible-filter-jasypt
  tasks:
  - set_fact:
      encrypted_secret: "{{ 'test' | jasypt_encrypt(algo, passcode, iterations) }}"
  - set_fact:
      decrypted_secret: "{{ encrypted_secret | jasypt_decrypt(algo, passcode, iterations) }}"
```
