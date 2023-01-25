Ansible Role for `iptables` Managed Firewall
============================================

An Ansible role that configures `iptables` managed firewall. Firewall rules are
persistent.

Requirements
------------

None.

Role Variables
--------------

`iptables_rules_ipv4` and `iptables_rules_ipv6` variables specify path to custom
rule dumps (IPv4 and IPv6 respectively). Rule dump format corresponds to
`iptables-save` (`ip6tables-save`) output.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
- name: Example playbook
  hosts: server
  tasks:
    - name: Configure firewall
      ansible.builtin.import_role:
        name: yabusygin.iptables
      vars:
        iptables_rules_ipv4: config/iptables.ipv4.rules
        iptables_rules_ipv6: config/iptables.ipv6.rules
```

License
-------

MIT

Author Information
------------------

Alexey Busygin \<yaabusygin@gmail.com\>
