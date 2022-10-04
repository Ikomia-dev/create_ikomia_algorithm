import os
import re
import logging
import argparse
from ikomia.core import config


logger = logging.getLogger(__name__)


def _to_pascal_case(string: str):
    return re.sub(r"(_|-)+", " ", string).title().replace(" ", "")


def _get_full_base_class(base_class: str):
    if base_class == "CWorkflowTask":
        return "core.CWorkflowTask"
    elif base_class == "CWorkflowTaskWidget":
        return "core.CWorkflowTaskWidget"
    else:
        return f"dataprocess.{base_class}"


def _get_qt_import(args):
    if args.qt == "pyqt":
        return "from PyQt5.QtWidgets import *"
    else:
        return "from PySide2 import QtCore, QtGui, QtWidgets"


def _get_qt_layout(args):
    if args.qt == "pyqt":
        template_path = os.path.join("templates", "pyqt_layout.pyt")
    else:
        template_path = os.path.join("templates", "pyside_layout.pyt")

    with open(template_path, "r") as template_file:
        content = template_file.read()
        return content


def _generate_entry_point(args, algo_dir: str):
    template_path = os.path.join("templates", "entry_point.pyt")
    with open(template_path, "r") as template_file:
        class_name = _to_pascal_case(args.name)
        content = template_file.read()
        content = content.replace("{{ PluginName }}", args.name)
        content = content.replace("{{ PluginClassName }}", class_name)

        with open(os.path.join(algo_dir, f"{args.name}.py"), "w") as f:
            f.write(content)


def _generate_process(args, algo_dir: str):
    template_path = os.path.join("templates", "process.pyt")
    with open(template_path, "r") as template_file:
        class_name = _to_pascal_case(args.name)
        content = template_file.read()
        content = content.replace("{{ PluginName }}", args.name)
        content = content.replace("{{ PluginClassName }}", class_name)
        content = content.replace("{{ ProcessBaseClass }}", _get_full_base_class(args.process_base))

        with open(os.path.join(algo_dir, f"{args.name}_process.py"), "w") as f:
            f.write(content)


def _generate_widget(args, algo_dir: str):
    template_path = os.path.join("templates", "widget.pyt")
    with open(template_path, "r") as template_file:
        class_name = _to_pascal_case(args.name)
        content = template_file.read()
        content = content.replace("{{ PluginName }}", args.name)
        content = content.replace("{{ PluginClassName }}", class_name)
        content = content.replace("{{ WidgetBaseClass }}", _get_full_base_class(args.widget_base))
        content = content.replace("{{ QtImport }}", _get_qt_import(args))
        content = content.replace("{{ QtLayout }}", _get_qt_layout(args))

        with open(os.path.join(algo_dir, f"{args.name}_widget.py"), "w") as f:
            f.write(content)


def _generate_test(args, algo_dir: str):
    template_path = os.path.join("templates", "test.pyt")
    with open(template_path, "r") as template_file:
        content = template_file.read()

        with open(os.path.join(algo_dir, f"{args.name}_test.py"), "w") as f:
            f.write(content)


def generate(args):
    ik_root_folder = config.main_cfg["root_folder"]
    algo_dir = os.path.join(ik_root_folder, "Plugins", "Python", args.name)

    # Create new algorithm directory
    os.makedirs(algo_dir)

    # Create source files
    open(os.path.join(algo_dir, "__init__.py"), "w+")
    open(os.path.join(algo_dir, "requirements.txt"), "w+")
    _generate_entry_point(args, algo_dir)
    _generate_process(args, algo_dir)
    _generate_widget(args, algo_dir)
    _generate_test(args, algo_dir)
    logger.info(f"Algorithm {args.name} created successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help="Algorithm name")
    parser.add_argument("--process_base", type=str, default="CWorkflowTask",
                        help="Algorithm base class from Ikomia API")
    parser.add_argument("--widget_base", type=str, default="CWorkflowTaskWidget",
                        help="Algorithm widget base class from Ikomia API")
    parser.add_argument("--qt", type=str, choices=["pyqt", "pyside"], default="pyqt",
                        help="Python Qt framework to use for widget")

    args = parser.parse_args()
    generate(args)
