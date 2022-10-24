import shutil
import os
from templateframework.metadata import Metadata


def run(metadata: Metadata = None):
    inputs = metadata.all_inputs()
    inputs_local = metadata.inputs
    inputs_global = metadata.global_inputs
    inputs_computed_global = metadata.global_computed_inputs
    target_path = metadata.target_path
    component_path = metadata.component_path
    stack_path = metadata.stack_path
    print("Hello from script.py!")