import os
import json


def config_gen(working_dir: str, save_path: str) -> dict:
    config = {}

    # 1
    proteins_path = input(
        ">> Please confirm the protein examples location (Insert the full path). \n"
        ">> An empty answer will set the protein location to the default '../tests' folder:\n"
        ">> Path: ")
    if proteins_path:
        # check if a valid directory was given;
        if os.path.isdir(proteins_path):
            config["proteins_path"] = proteins_path
            pass
        else:
            print(f">> Given directory not found: {proteins_path}")
            # set the default directory;
            proteins_path = working_dir + "\\tests"
            config["proteins_path"] = proteins_path
            print(f">> Directory set as default: {proteins_path}")
    else:
        # set the default directory;
        proteins_path = working_dir + "\\tests"
        config["proteins_path"] = proteins_path

    # 2
    is_convex_relax = bool(input(
        ">> Please confirm if the existing proteins will pass the SDP relaxed phase: (Boolean)\n"
        ">> An empty answer will set the configuration to 'False'."))
    config["is_convex_relax"] = is_convex_relax

    # 3
    multi_start_phase = bool(input(
        ">> Please confirm if the Multi-start will be executed: (Boolean)\n"
        ">> An empty answer will set the configuration to 'False'."))
    config["multi_start_phase"] = multi_start_phase

    # 4
    mdjeep_source = bool(input(
        ">> Will be MDjeep protein data be loaded ? (Boolean)\n"
        ">> An empty answer will set the configuration to 'False'."))
    config["MDjeep_source"] = mdjeep_source

    # 5
    protein_black_list = list(input(
        ">> Is there any protein that will not be tested? (List) Please answer using space as a separator:"
        ">> If answered *, the single mode will be activated. Just one specific protein will be loaded"
        ">> Press Enter for an empty answer. This will set the configuration to test all the available proteins."))
    if not protein_black_list:
        # An empty list was given!
        pass
    elif protein_black_list == ['*']:
        # Single mode activated
        pass
    else:
        # Removing spaces:
        protein_black_list = list(filter(lambda x: x != ' ', protein_black_list))
    config["protein_black_list"] = protein_black_list

    # 6
    # Global Debug configuration;
    debug_value = bool(input(
        ">> Will the Debug option be enable during the process? (Boolean)"
        ">> An empty answer will set the configuration to 'False'."))
    config["debug_value"] = debug_value

    with open(save_path, 'w') as file:
        json.dump(dict, file)
    return config
