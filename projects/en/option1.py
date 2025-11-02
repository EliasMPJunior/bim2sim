from bim2sim import Project
from pathlib import Path
from bim2sim.utilities.types import IFCDomain

project_path = '/projects/en'

ifc_path = {IFCDomain.arch: Path('/projects/en/ifc/AC20-FZK-Haus.ifc')}

project = Project(project_path)

# Option 1: handle decisions manually
for bunch in project.run():
    for decision in bunch:
        print(decision.question)
        decision.value = 42  # your logic goes here
