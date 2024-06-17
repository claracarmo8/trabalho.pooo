medicos=[
    {"NOME":"clara",
    "CPF":"100.456.987-67",
    "RG":"AL654321",
    "CRM":"6758",
    "TELEFONE":"(82)9979-8674",
    "ENDEREÇO":"São Vicente",
    "SEXO":"feminino",
    "SENHA":"9741",
    },
    {"NOME":"Luís",
    "CPF":"887.635.900-65",
    "RG":"BA169812",
    "CRM":"9634",
    "TELEFONE":"(71)9954-8307",
    "ENDEREÇO":"Sitio Chico",
    "SEXO":"masculino",
    "SENHA":"8854",
    },
    {"NOME":"Mathias",
    "CPF":"567.665.870-65",
    "RG":"BA344328",
    "CRM":"6782",
    "TELEFONE":"(71)9904-9077",
    "ENDEREÇO":"vacarias",
    "SEXO":"masculino",
    "SENHA":"6743",
    }
]

Pacientes= [
{
    "NOME":"italo",
    "CPF":"234.567.890-90",
    "RG":"CE345127",
    "TELEFONE":"(88)97898-6534",
    "ENDEREÇO":"Riacho Seco",
    "SEXO":"Masculino",
    "CONVENIO":"SulAmerica",
},
{
    "NOME":"robecio",
    "CPF":"216.577.170-54",
    "RG":"CE268451",
    "TELEFONE":"(88)96053834",
    "ENDEREÇO":"Fortuna",
    "SEXO":"Masculino",
    "CONVENIO":"SaudeUniversal",
},
    {
    "NOME":"maria",
    "CPF":"789.657.856-97",
    "RG":"CE345721",
    "TELEFONE":"(88)97898-",
    "ENDEREÇO":"Boa Vista",
    "SEXO":"Masculino",
    "CONVENIO":"VidaClin",
}
]

Convenio = [
    {
    "NOME":"SulAmerica",
    "CNPJ":"12.458.523/0001-00",
    "TELEFONE":"(88)99456-8954",
    "ENDEREÇO":"RIACHINHO,141",
    "PLANO": "A,B e C"
},
{
    "NOME":"saudeuniversal",
    "CNPJ":"65.898.098/0001-00",
    "TELEFONE":"(88)99789-7858",
    "ENDEREÇO":"BETANIA,78",
    "PLANO": "A e B"
},
{
    "NOME":"vidaclin",
    "CNPJ":"21.988.145/0001-00",
    "TELEFONE":"(88)99845-6745",
    "ENDEREÇO":"JUREMAL,210",
    "PLANO": "A,B e x(premium)"
},
]

consulta = [ 
{
    "Médico": "Matias",
    "Paciente": "Robecio",
    "Data": "08/07/2024",
    "Hora": "14:00",
},
{
    "Médico": "Clara",
    "Paciente": "italo",
    "Data": "12/06/2024",
    "Hora": "15:00",
},
{
    "Médico": "Luís",
    "Paciente": "Maria",
    "Data": "08/01/2025",
    "Hora": "10:30",
}
]

Compromissos=[
{
    "data":"06/04/2025",
    "hora inicial":"07;35",
    "hora final":"10;00",
    "descricao":"casamento",
},
{
    "data":"09/03/2024",
    "hora inicial":"14::00",
    "hora final":"15;31",
    "descricao":"fazer compras",
}]

def cadastrarMedicos():
        
        print("Nome Completo:")
        nome=input("")
        print("CPF:")
        cpf= input("")
        print("RG:")
        rg= input("")
        print("Numero do conselho regional de medicina(CRM):")
        crm= input("")
        print("Telefone:")
        telefone= input("")
        print("Endereço")
        endereço= input("")
        print("Senha")
        senha= input("")
        print("Sexo")
        sexo=input("")
        print("Salvar as informaçoes? (confirmar/cancelar) ")
        a=input("")
        if a=="confirmar":
            print("informaçoes salvas")
            
            medicos.append({
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "crm": crm,
            "telefone": telefone,
            "endereco": endereço,
            "sexo": sexo,
            "senha": senha
            })
            print(medicos)
        else:
            print("Programa cancelado!")
      
    
def cadastrarPacientes():
    
       print("Cadastrar paciente:)")
       print("Nome completo:")
       nome2= input("")
       print("Endereço:")
       endereço2= input("")
       print("Telefone:")
       telefone2= input("")
       print("CPF:")
       cpf2= input("")
       print("RG")
       rg2= input("")
       print("Sexo:")
       sexo2= input("")
       print("A qual convenio esta associado?")
       convenio = input("")
       print("Salvar as informaçoes? (confirmar/cancelar)")
       b=input()
       if b=="confirmar":
            print("informaçoes salvas com sucesso!")

            Pacientes.append({
    
                "nome": nome2,
                "endereco": endereço2,
                "telefone": telefone2,
                "cpf": cpf2,
                "rg": rg2,
                "sexo": sexo2,
                "convenio": convenio
        })
            print(Pacientes)
       else:
          print("Programa cancelado!")
          breakpoint
       
def cadastrarConvenios():
    
    print("Forneça o nome do convênio")
    nome3= input("")
    print("O seu telefone para contato")
    telefone3= input("")
    print("O seu endereço")
    endereço3= input("")
    print("O CPF do convênio")
    cpf3= input("")
    planos = input("")
    print("Deseja salvar as informaçoes? (confirmar/cancelar)")
    c=input("")
    if c=="confirmar":
        print("infornaçoes salvas")

        Convenio.append({
    
                "nome": nome3,
                "endereco": endereço3,
                "telefone": telefone3,
                "palnos": planos
        })
        print(Convenio)
    else:
        print("Programa cancelado!")
        breakpoint

def buscarMedicos():
   
       print("Informe o nome ou CRM do médico:")
       busm = input("")
       resultados = [medico for medico in medicos if busm in medico or busm in medico['CRM']]
       if resultados:
           for resultado in resultados:
               print(f"Nome: {resultado['NOME']}, Telefone: {resultado['TELEFONE']}, CRM: {resultado['CRM']}")
       else:
           print("Não foi possivel encontrar um médico com este nome ou crm.")

def buscarPacientes():
   
       print("Informe o nome ou CPF do paciente:")
       busp = input("")
       resuls = [paciente for paciente in Pacientes if busp in paciente['NOME'] or busp in paciente['CPF']]
       if resuls:
           for resultado in resuls:
               print(f"Nome: {resultado['NOME']}, Telefone: {resultado['TELEFONE']}, CPF: {resultado['CPF']}")
       else:
           print("Não foi possivel encontrar um paciente com este nome ou cpf.")


def buscarConvenios():
     
       print("Informe o nome ou CNPJ do convênio")
       busc = input("")
       resultados = [convenio for convenio in Convenio if busc in convenio['NOME'] or busc in convenio['CNPJ']]
       if resultados:
           for resultado in resultados:
               print(f"Nome: {resultado['NOME']}, Telefone: {resultado['TELEFONE']}, CNPJ: {resultado['CNPJ']}")
       else:
           print("Não foi possivel encontrar um covenio com este nome ou cnpj.")

   
def alterarMedicos():
     
     print("Informe o CRM: ")
     crm = input("")
     medico = next((medico for medico in medicos if medico['CRM'] == crm), None)
     if medico:
           print(f"Dados atuais: {medico}")
           print("Informe os novos dados :")
           nome = input(f"Nome ({medico['NOME']}): ") or medico['NOME']
           cpf = input(f"CPF ({medico['CPF']}): ") or medico['CPF']
           rg = input(f"RG ({medico['RG']}): ") or medico['RG']
           telefone = input(f"Telefone ({medico['TELEFONE']}): ") or medico['TELEFONE']
           endereco = input(f"Endereço ({medico['ENDEREÇO']}): ") or medico['ENDEREÇO']
           sexo = input(f"Sexo ({medico['SEXO']}): ") or medico['SEXO']
           senha = input(f"Senha ({medico['SENHA']}): ") or medico['SENHA']
           medico.update({
               "nome": nome,
               "cpf": cpf,
               "rg": rg,
               "telefone": telefone,
               "endereco": endereco,
               "sexo": sexo,
               "senha": senha
           })
           print("Dados atualizados com sucesso!.")
           print(medicos)
     else:
           print("Médico não encontrado.")

def alterarPacientes():
   
       print("Informe o CPF do paciente:")
       cpf = input("")
       paciente = next((paciente for paciente in Pacientes if paciente['CPF'] == cpf), None)
       if paciente:
           print(f"Estes são os dados atuais: {paciente}")
           print("Forneça os novos dados :")
           nome = input(f"Nome ({paciente['NOME']}): ") or paciente['NOME']
           rg = input(f"RG ({paciente['RG']}): ") or paciente['RG']
           telefone = input(f"Telefone ({paciente['TELEFONE']}): ") or paciente['TELEFONE']
           endereco = input(f"Endereço ({paciente['ENDEREÇO']}): ") or paciente['ENDEREÇO']
           sexo = input(f"Sexo ({paciente['SEXO']}): ") or paciente['SEXO']
           convenio = input(f"Convênio ({paciente['CONVENIO']}): ") or paciente['CONVENIO']
           paciente.update({
               "nome": nome,
               "rg": rg,
               "telefone": telefone,
               "endereco": endereco,
               "sexo": sexo,
               "convenio": convenio
           })
           print("Dados atualizados com sucesso!.")
       else:
           print("Paciente não encontrado.")

def marcarCompromisso():
    print("Marcar um compromisso: ")
    print("Informe a data que você deseja :")
    data = input("").strip()
    print("Informe o horário do compromisso :")
    horario = input("").strip()
    print("Descreva o compromisso:")
    descricao = input("").strip()
    print("Você deseja salvar essas informações? (confirmar/cancelar)")
    salvar = input("").strip().lower()
    if salvar == "confirmar":
            print("Compromisso registrado")

            consulta.append({
                "data": data,
                "horario": horario,
                "descricao": descricao
            })
    else:
            print("As informações não foram salvas.")

def marcarConsulta():
    print("Agendar consulta: ")
    print("Data desejada:")
    data_consulta = input("").strip()
    print("Horário desejado:")
    horario = input("").strip()
    print("Motivo da consulta:")
    descricao = input("").strip()
    print("Deseja confirmar o agendamento? (confirmar/cancelar)")
    confirmacao = input("").strip().lower()
    if confirmacao == "confirmar":
            print(f"Agendamento realizado com sucesso! Detalhes: Data: {data_consulta}, Horário: {horario}, Descrição: {descricao}")
    else:
            print("Agendamento cancelado.")

def emitirRelatorio():
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas realizadas em um intervalo de data")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"Nome: {medico['NOME']}, CPF: {medico['CPF']}, CRM: {medico['CRM']}, Telefone: {medico['TELEFONE']}")
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in Pacientes:
            print(f"Nome: {paciente['NOME']}, CPF: {paciente['CPF']}, Telefone: {paciente['TELEFONE']}")
    elif escolha == "3":
        print("Convênios:")
        for convenio in Convenio:
            print(f"Nome: {convenio['NOME']}, CNPJ: {convenio['CNPJ']}, Telefone: {convenio['TELEFONE']}")
    elif escolha == "4":
        data_inicio = input("Informe a data de início : ")
        if not (data_inicio):
            print("Data inválida,programa encerrado.")
            return
        
        data_fim = input("Informe a data de fim : ")
        if not (data_fim):
            print("Data inválida, programa encerrado.")
            return
        
        print(f"Consultas de {data_inicio} a {data_fim}:")
        for consulta in consulta:
            data_consulta = consulta.get("data", "")
            if data_inicio <= data_consulta <= data_fim:
                print(f"Data: {consulta['data']}, Horário: {consulta['horario']}, Médico: {consulta['medico']}, Paciente: {consulta['paciente']}, Descrição: {consulta['descrição']}")

a = True
while a:
    lang = input("1 - Cadastrar Médico\n"
                 "2 - Cadastrar Paciente\n"
                 "3 - Cadastrar Convênio\n"
                 "4 - Buscar Médicos\n"
                 "5 - Buscar Pacientes\n"
                 "6 - Buscar Convênios\n"
                 "7 - Alterar Medicos\n"
                 "8 - Alterar Pacientes\n"
                 "9 - Marcar Compromisso\n"
                 "10 - Marcar Consulta\n"
                 "11 - Emitir Relatório\n"
                 "12 - Encerrar Programa\n"
                 "O que você deseja fazer?")
    match lang:
        case "1":
            cadastrarMedicos()
        case "2":
            cadastrarPacientes()
        case "3":
            cadastrarConvenios()
        case "4":
            buscarMedicos()
        case "5":
            buscarPacientes()
        case "6":
            buscarConvenios()
        case "7":
            alterarMedicos()
        case "8":
            alterarPacientes()
        case "9":
            marcarCompromisso()
        case "10":
            marcarConsulta()
        case "11":
            emitirRelatorio()
        case "12":
            print("Programa Encerrado!")
        case _:
            print("Escolha uma opção válida")

