Angel:
En los files dentro de sub directorios como:
"/model/tests/unittest_classname.py"
se le debe add este pedaso de codigo al principio
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

ejemplo de llamado
"from model.User import User"

este pedaso de codigo permite llamar modulos en el directorio padre,
es importante notar que todo llamado debe estar despues de este pedaso de codigo.
