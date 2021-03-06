from tenable.io import TenableIO

tio_client = TenableIO(
    access_key='',
    secret_key='',
    proxies={}
)

session_details = tio_client.session.details()
if session_details['permissions'] != 64:
    print('This script must run as a user with Administrator permissions. Exiting.')
    quit()

default_can_use_acl = [
    {
        "name": "Default",
        "permissions": 32,
        "type": "default"
    }
]
for tg in tio_client.target_groups.list():
    try:
        if tg['type'] == 'system' and tg['name'] != 'Default':
            print('Updating System Target Group ' + tg['name'] + ' Default permission to \'Can Use\'')
            default_can_use_acl[0]['permissions'] = 32
            tio_client.target_groups.edit(tg['id'], acls=default_can_use_acl)
        elif tg['type'] == 'user':
            print('Updating User Target Group ' + tg['name'] + ' Default permission to \'Can Use\'')
            # 16 is the permission to set a User Target Group to "Can Use". 32 will set the permission to "Can Change"
            default_can_use_acl[0]['permissions'] = 16
            tio_client.target_groups.edit(tg['id'], acls=default_can_use_acl)
        elif (tg['type'] == 'system' and tg['name'] == 'Default') or tg['type'] == 'group':
            pass
        else:
            print('WARNING: Unrecognized Target Group type.')
            print(tg['type'])
    # Generic pass for any unforeseen errors
    except:
        pass
