import Export

projects = ["You Lits Projects"]
directory = "/home/thiago/Documents/Sonar/"

expo = Export.Export()
expo.export_branches_pdf(projects, directory)
