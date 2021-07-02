contacts = []

def create_new_contact():
    contact = dict()
    contact['name'] = input('Name: ')
    contact['email'] = input('Email: ')
    contact['Age'] = int(input('Age: '))
    contact['Favorite Color'] = input('Favorite color: ')
    contact['birthday'] = input('Birthday: ')

    contacts.append(contact)


def list_contacts():
    for contact in contacts:
        print(contact)
    
    input('Press a key to continue')


def search_contact():

    name = input('Insert name of contact: ')
    
    for contact in contacts:
        if name in contact['name']:
            return contact

    print('Contact not found')
    return {}

def delete_contact():
    contact = search_contact()

    if contact != {}:
        d  = input(f'Delete contact "{contact["name"]}?(y/N): "')

        if(d == 'y'):
            contacts.remove(contact)


def menu():
    print('Bem vindo a agenda')
    print('1. Cadastrar novo contato')
    print('2. Listar contatos')
    print('3. Pesquisar um contato')
    print('4. Apagar um contato')
    print('5. Sair')

    d = input('')

    print(chr(27) + "[2J")
    if(d == '1'):
        create_new_contact()
    elif(d == '2'):
        list_contacts()
    elif(d == '3'):
        contact = search_contact()
        print(contact)
        input('Press a key to continue')
    elif(d == '4'):
        delete_contact()
    elif(d == '5'):
        exit()


if __name__ == '__main__':
    while True:
        menu()