import Export

class Main():  

    projects = ["My Çist Projects"]

    status = 's'
    while(status == 's'):
        print('O que você deseja fazer?\n')
        print('1- Gerar relatório de Array pré definido?\n')
        print('2- Gerar relatório de um projeto específico?\n')
        value = int(input())
        directory = "/home/thiago/Documents/Sonar/"
        if value == 1:
            print('Usar diretório padrão (/home/thiago/Documents/Sonar/)? (y)\n')
            p = str(input().lower())
            if p.__eq__('y'):
                expo = Export.Export()
                expo.export_branches_pdf(projects, directory)
            else:
                print('Informe o diretório que deseja: \n')
                d = str(input())
                directory = d
                try:
                    expo = Export.Export()
                    expo.export_branches_pdf(projects, directory)
                except:
                    print("Erro no diretório informado")       
            
        if value == 2:
            print('Informe o projeto que deseja gerar o relatório:\n')
            prj = str(input())
            array = list([prj])
            print(array)
            print('Usar diretório padrão (/home/thiago/Documents/Sonar/)? (y)\n')
            p = str(input().lower())
            directory = "/home/thiago/Documents/Sonar/"
            if p=='y':
                expo = Export.Export()
                expo.export_branches_pdf(array, directory)
            else:
                print('Informe o diretório que deseja: \n')
                d = str(input())
                directory = d
                try:
                    expo = Export.Export()
                    expo.export_branches_pdf(array, directory)
                except:
                    print("Erro no diretório informado") 

        print('Deseja continuar? Digite s/n')
        status = input().lower()
    
    print('Script finalizado com sucesso\n')
