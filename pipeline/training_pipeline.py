from config.paths_config import ANIMELIST_CSV, CONFIG_PATH, PROCESSED_DIR
from src.data_processing import DataProcessor
from src.model_training import ModelTraining
from utils.common_functions import read_yaml


if __name__=="__main__":
    data_processor = DataProcessor(ANIMELIST_CSV, PROCESSED_DIR)
    data_processor.run()

    model_trainer = ModelTraining(PROCESSED_DIR)
    model_trainer.train_model()