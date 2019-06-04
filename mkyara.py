# Run mkyara on the current selection and generate rule
#@author Maelle Roubeau <maelle.roubeau@epita.fr> & Simon Regourd <simon.regourd@epita.fr>

import subprocess
import tempfile
import os

from ghidra.program.model.address.Address import *
from ghidra.program.model.listing.CodeUnit import *
from ghidra.program.model.listing.Listing import *

minAddress = currentSelection.getMinAddress()
maxAddress = currentSelection.getMaxAddress()

file_location = currentProgram.getDomainFile().getMetadata()["Executable Location"]
_, result_file = tempfile.mkstemp()

subprocess.call(["mkyara", "-f", file_location, "-o", str(minAddress.getOffset()), "-s", str(maxAddress.getOffset() - minAddress.getOffset()), "-r", result_file])

with open(result_file) as file:
    print(str(file.read()))
