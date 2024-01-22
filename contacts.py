def getInputInfos():
    text = """
    Digite o %s do Contato: """

    name  = input(text % ("nome"))
    phone = input(text % ("phone"))
    email = input(text % ("email"))
    return {
        "name": name,
        "phone": phone,
        "email": email,
        "fav": False
    }

def getContactIndex(contacts):
    visualizar(contacts)

    text = """
    Escolha um usuário: """

    return int(input(text)) - 1

def adicionar(contacts, contato):
    contacts.append(contato)
    print("""\n\nContato adicionado com sucesso!\n\n""")
    return

def visualizar(contacts, onlyFavs = False):
    message = ""
    for i, c in enumerate(contacts, start=1):
        isFav = c["fav"]
        fav = "[❤ ]" if isFav else "[  ]"
        if onlyFavs:
            if isFav:
                message += f"{fav} {i}: name: {c["name"]} - phone: {c["phone"]} - email: {c["email"]} \n" 
        else:
            message += f"{fav} {i}: name: {c["name"]} - phone: {c["phone"]} - email: {c["email"]} \n"

    print(message)
    return

def editar(contacts):
    index = getContactIndex(contacts)
    
    c_old = contacts[index]
    c_new = getInputInfos()
    
    c_old["name"] = c_new["name"]
    c_old["phone"] = c_new["phone"]
    c_old["email"] = c_new["email"]

    return

def favorito(contacts):
    index = getContactIndex(contacts)
    contact = contacts[index]
    fav = contact["fav"]
    contact["fav"] = not fav
    if fav:
        print("Contado desmarcado dos favoritos")
    else:
        print("Contato marcado dos favoritos")
    return

def listarFavoritos(contacts):
    visualizar(contacts, True)
    return

def apagar(contacts):
    index = getContactIndex(contacts)
    contact = contacts[index]
    contacts.remove(contact)
    return

contacts = []
while True:
    try:
        menu = """
        ###   GERENCIAMENTO DE CONTATOS   ### 

            1. Adicionar
            2. Listar
            3. Editar
            4. (Des)marcar  favorito
            5. Listar       favorito(s)
            6. Apagar
            7. Sair

        Escolha uma opção: """
        opt = int(input(menu))

        if opt == 1:
            adicionar(contacts, getInputInfos())
        elif opt == 2:
            visualizar(contacts)
        elif opt == 3:
            editar(contacts)
        elif opt == 4:
            favorito(contacts)
        elif opt == 5:
            listarFavoritos(contacts)
        elif opt == 6:
            apagar(contacts)
        elif opt == 7:
            break
        else:
            raise NotImplementedError(opt)
    except NotImplementedError as e:
        print("Opção não implementada: ", e)
    except ValueError as e:
        print("Opção desconhecida, verifique o que foi digitado: ", opt)
    except Exception as e:
        print(e)
    else:
        print("Operação realizada")
    finally:
        print("############")
print("Programa finalizado!")