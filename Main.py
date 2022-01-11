import Export

projects = ["You List Projects"] 
directory = "/home/thiago/Documents/Sonar/"

expo = Export.Export()
expo.export_branches_pdf(projects, directory)
