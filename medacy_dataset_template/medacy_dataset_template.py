from pkg_resources import resource_listdir, resource_string, resource_filename
from medacy.data import Dataset

package_name = "medacy_dataset_template"

def load():
    """

    :return: Two medaCy Dataset objects corresponding to training and evaluation data respectively and meta_data.
    """

    meta_data = {
        'entities' : ['the', 'entities', 'this', 'dataset', 'annotates'],
        'relations': ['the', 'relations', 'this', 'dataset', 'annotates'],
    }

    return get_training_dataset(),get_evaluation_dataset(), meta_data

def get_training_dataset():
    """
    :return: a medaCy Dataset object containing this Dataset's designated training data.
    """
    return Dataset(resource_filename(package_name, 'data/training'))

def get_evaluation_dataset():
    """
    :return: a medaCy Dataset object containing this Dataset's designated training data.
    """
    return Dataset(resource_filename(package_name, 'data/evaluation'))

