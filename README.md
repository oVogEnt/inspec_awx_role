# My InSpec Role

This Ansible role executes InSpec tests on remote Linux hosts to check compliance with the CIS Distribution Independent Linux Benchmark. This guide describes how to configure and use the role in an AWX project.

## Requirements

- Ansible 2.9 or higher
- AWX or Ansible Tower
- Access to remote hosts via SSH

## Configuration and Usage Steps

### 1. **Generate an SSH key:**
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Follow the prompts and save the key, for example in ~/.ssh/id_rsa.

Add the public key to the remote hosts:
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@remote_host
```

### 2. Set Variables for the SSH Key in the AWX Template
Go to the AWX Interface:

Navigate to the Templates section and create or edit a job template.
Add the following variables to the job template:

```yaml
---
ssh_private_key: |
  -----BEGIN RSA PRIVATE KEY-----
  ...
  -----END RSA PRIVATE KEY-----
ssh_public_key: |
  ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...
ansible_user: "your_remote_user"
```

### 3. Set Variables in the Job Template
Add variables for InSpec attribute values if needed:
```yaml
---
inspec_vars_list:
  - name: 'cis_level'
    value: '1'
```

### 4. Use a Custom Execution Environment for AWX

Use the custom execution environment quay.io/owen_vogelaar/inspec_ee

Configure the execution environment in AWX:

Go to Administration > Execution Environments and add the new image.

### 5. Configure and Run the Job Template in AWX
Go to the AWX Interface and edit the job template:

Select the appropriate Inventory and Project.
Select the custom Execution Environment you created.
Ensure the correct playbook is selected.
Add the required variables to the job template as described earlier.

Run the job template:

Click Launch to execute the InSpec tests on the remote hosts.

### 6. View Results
The results of the InSpec tests will be visible in the job output. Any failures or deviations from the CIS standards will be reported.

## Role Structure
The role has the following structure:

```plaintext
my_inspec_role/
├── defaults/
│   └── main.yml
├── tasks/
│   └── main.yml
├── inspec-profile/
│   ├── controls/
│   └── inspec.yml
└── meta/
    └── main.yml
```

## Important Files and Directories
- defaults/main.yml: Contains default variables for the role.
- tasks/main.yml: Main tasks file for the role.
- inspec-profile/: Directory containing the InSpec profile.
- meta/main.yml: Metadata for the role.

## License
This role is licensed under the Apache License, Version 2.0.

```csharp
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0
Follow these steps to configure and use the my_inspec_role within your AWX environment to execute InSpec tests on Linux hosts.
```