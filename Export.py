from sonarqube import SonarEnterpriseClient
from sonarqube import SonarQubeClient

from sonarqube.community.project_badges import SonarQubeProjectBadges

import csv
from datetime import datetime

import json

class Export:

    def export_branches_pdf(self, projects, directory):

        jsonFinal = {}

        #sonar = SonarEnterpriseClient(sonarqube_url="http://localhost:9000", token='You Token Sonar')
        #Autenticação com usuário e senha
        sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='user', password='pass')
        
        today = datetime.today()

        date = '{}-{}-{}'.format(today.day, today.month, today.year)

        with open(directory + 'Relatorio-Sonar-'+ date +'.csv', 'a+',) as csvfile:
            fields = ['Ord', 'Project Name', 'Project', '-', 'Blocker','Critical', '--', '---', 'Major', '----','Issues', 'Coverage']
            writer = csv.DictWriter(csvfile, fieldnames=fields, dialect='excel')
            writer.writeheader()
            ordem = 1
            blockers = 0
            criticals = 0
            majors = 0
            issuess = 0

            for project in projects:
                try:
                    print('Gerando relatório do pacote '+str(project))

                    blocker = list(sonar.issues.search_issues(componentKeys=project, severities="BLOCKER", statuses="OPEN")).__len__()
                    blocker = blocker + list(sonar.issues.search_issues(componentKeys=project, severities="BLOCKER", statuses="REOPENED")).__len__()
                    
                    critical = list(sonar.issues.search_issues(componentKeys=project, severities="CRITICAL", statuses="OPEN")).__len__()
                    critical = critical + list(sonar.issues.search_issues(componentKeys=project, severities="CRITICAL", statuses="REOPENED")).__len__()
                    
                    major = list(sonar.issues.search_issues(componentKeys=project, severities="MAJOR", statuses="OPEN")).__len__()
                    major = major + list(sonar.issues.search_issues(componentKeys=project, severities="MAJOR", statuses="REOPENED")).__len__()
                    
                    issues = list(sonar.issues.search_issues(componentKeys=project, statuses="OPEN")).__len__()
                    issues = issues + list(sonar.issues.search_issues(componentKeys=project, statuses="REOPENED")).__len__()
        
                    result = list(sonar.measures.search_measures_history(component=project, metrics="coverage"))
                    coverage = str(result[0])
                    coverage = coverage[-10:-3]
                    
                    
                    ocorrencia = 0
                    valor = ""

                    for letra in coverage:
                        if ocorrencia==0:  
                            
                            if letra.__eq__("'"):
                                ocorrencia=1
                        else:
                            if letra.__eq__("'"):
                                ocorrencia = 0
                            else:
                                valor = valor + letra

                    coverage = valor                         

                    writer.writerow({'Ord': ordem, 'Project Name': project, 'Project': project, '-': date, 'Blocker': blocker, 'Critical': critical, '--': '', '---':'', 'Major': major, '----':'', 'Issues': issues, 'Coverage': coverage})

                    ordem = ordem + 1
                    blockers = blockers + blocker
                    criticals = criticals + critical
                    majors = majors + major
                    issuess = issuess + issues

                    pjt = {
                        "blockers": blockers,
                        "criticals": criticals,
                        "majors": majors,
                        "issues": issuess,
                        "coverage": coverage
                    }

                    jsonFinal[project] = pjt
                    
                except:
                    print("Erro ao gerar relatorio do projeto "+str(project))
            
            writer.writerow({'Ord': "", 'Project Name': "", 'Project': "Resume", '-': "", 'Blocker': blockers, 'Critical': criticals, '--': "", '---': "", 'Major': majors, '----': "", 'Issues': issuess})
        print("Relatório finalizado.")

        print("Exportando JSON")
        with open(directory + 'json_data.json', 'w') as outfile:
            json.dump(jsonFinal, outfile)

        return "Sucess!"
