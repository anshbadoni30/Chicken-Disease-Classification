import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from src.cnnClassifier.entity.config_entity import PrepareCallbacksconfig

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksconfig):
        self.config=config

    @property
    def _create_tb_callbacks(self):
        timestamp=time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir= os.path.join(
            self.config.tensorboard_log_dir,
            f"tb_logs_at{timestamp}", 
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    """
    It creates TensorBoard callback object
    Which will log all training progress to that folder, 
    and TensorBoard will pick it up to display graphs and plots.
    """
    

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.checkpoint_model_filepath,
            save_best_only=True
        )
    #It will save the model to checkpoint_model_filepath only when validation loss improves (save_best_only=True).
    

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]
    

