# ec2_tags_inventory
## A Simple AWS EC2 Dynamic Inventory for Ansible 

Read more about the [Ansible Dynamic Inventory](http://docs.ansible.com/ansible/intro_dynamic_inventory.html). 

### How to use this script?
Tag all your instances with whatever roles they play with key "ansible_role" in a comma separated fashion. So ansible_role: webserver,emailserver is a valid tag. The inventory script will look for tag with key "ansible_role" and splits the value by comma. 

Make the ec2_tags_inventory.py executable
```
$ chmod 755 ec2_tags_inventory.py
```
Copy the ec2.ini.sample to ec2.ini and put the AWS access key and secret and use it in place of Ansible inventory file.

### To Do
- implement pagination.
- make the key "ansible_role" customizable.
- make the delimiter customizable. 
