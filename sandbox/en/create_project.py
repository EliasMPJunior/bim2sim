from pathlib import Path
from bim2sim import Project
from bim2sim.utilities.types import IFCDomain

project_path = '/projects/en'
# ifc_path = '/projects/en/ifc'
ifc_path = {IFCDomain.arch: Path('/projects/en/ifc/AC20-FZK-Haus.ifc')}

if Project.is_project_folder(project_path):
    # load project if existing
    project = Project(project_path)
else:
    # else create a new one
    project = Project.create(project_path, ifc_path, 'energyplus')