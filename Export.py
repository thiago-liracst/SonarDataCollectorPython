from sonarqube import SonarEnterpriseClient

from sonarqube.community.project_badges import SonarQubeProjectBadges

import os
from datetime import datetime
import csv

class Export:

    def export_branches_pdf(self, projects, directory):

        sonar = SonarEnterpriseClient(sonarqube_url="http://localhost:9000", token='You Token')
        
        with open(directory + 'relatorio.csv', 'a+',) as csvfile:
            fields = ['Ord','Project', 'Blocker','Critical','Major','Issues']
            writer = csv.DictWriter(csvfile, fieldnames=fields, dialect='excel')
            writer.writeheader()
            ordem = 0
            blockers = 0
            criticals = 0
            majors = 0
            issuess = 0

            for project in projects:
                try:
                    print('Gerando relatório do pacote '+str(project))

                    blocker = list(sonar.issues.search_issues(componentKeys=project, severities="BLOCKER")).__len__()
                    critical = list(sonar.issues.search_issues(componentKeys=project, severities="CRITICAL")).__len__()
                    major = list(sonar.issues.search_issues(componentKeys=project, severities="MAJOR")).__len__()
                    issues = list(sonar.issues.search_issues(componentKeys=project)).__len__()
                    
                    writer.writerow({'Ord': ordem, 'Project': project, 'Blocker': blocker, 'Critical': critical,'Major': major, 'Issues': issues})

                    ordem = ordem + 1
                    blockers = blockers + blocker
                    criticals = criticals + critical
                    majors = majors + major
                    issuess = issuess + issues
                    
                except:
                    print("Erro ao gerar relatorio do projeto "+str(project))
            
            writer.writerow({'Ord': "", 'Project': "Resume", 'Blocker': blockers, 'Critical': criticals,'Major': majors, 'Issues': issuess})
        print("Relatório finalizado.")

        return "Sucess!"
