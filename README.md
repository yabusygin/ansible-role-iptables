Ansible Role for `iptables` Managed Firewall
============================================

An Ansible role that configures `iptables` managed firewall. Firewall rules are
persistent.

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
- name: example playbook
  hosts: server
  tasks:
    - name: configure firewall
      ansible.builtin.import_role:
        name: iptables
```

License
-------

MIT

Author Information
------------------

Alexey Busygin \<yaabusygin@gmail.com\>
