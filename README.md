# create_ikomia_algorithm

Python script to create skeleton code of an Ikomia algorithm. It produces minimal code to ensure Ikomia format conformity of the future algorithm. When completed, the new algorithm can be used in **Ikomia Studio** or **Ikomia API**. Then, you have to integrate your own algorithm code, the main entry point being the *run()* function of the Python process file. Please read the [documentation](https://ikomia-dev.github.io/python-api-documentation/) for details.

## Usage
Python >= 3.7

    python create_ikomia_algorithm.py name [--process_base algo_base_class] [--qt Qt framework]

where:

- **name** (mandatory): algorithm name (must be unique). Please consult the naming convention [here](https://ikomia-dev.github.io/python-api-documentation/naming.html).
- **--process_base** (optional): Ikomia API base class from which the algorithm is derived. **Default: CWorkflowTask**. List of possible base classes [here](https://ikomia-dev.github.io/python-api-documentation/_autosummary/ikomia.dataprocess.pydataprocess.html).
- **--qt** (optional): name of the Python Qt framework. Possible values are **pyqt** (recommended) or **pyside**.
