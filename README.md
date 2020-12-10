# git-deploy-example
Example project demonstrating git-deploy configuration

## Getting started

### Install [git-deploy](https://github.com/NUKnightLab/git-deploy)

```
 $ pip install git+https://github.com/NUKnightLab/git-deploy.git@1.0.6
```

### Create /etc/ansible/hosts

See the [ansible docs](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)
for details. The section labels in your hosts file should match the deployment
environments you intend to use with git-deploy (e.g., we use stg and prd to
indicate staging and production deployment environments respectively)

### Create /etc/ansible/roles

Copy roles from the [git-deploy repo](https://github.com/NUKnightLab/git-deploy/tree/1.0.6/etc/ansible/roles) into /etc/ansible/roles


### Clone this repository

```
 $ git clone https://github.com/NUKnightLab/git-deploy-example
```

Set the missing variables in the config: deploy/config.common.yml

### Deploy the project

```
 $ git deploy stg main
```
