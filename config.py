import os

PROJECT_ROOT = os.path.dirname(__file__)
OUTPUT_DIRECTORY_TOPLEVEL = os.path.join(PROJECT_ROOT, "output/")
VECTOR_OUTPUT_DIRECTORY = os.path.join(OUTPUT_DIRECTORY_TOPLEVEL, "vectors/")
DATA_FILES_DIR = os.path.join(OUTPUT_DIRECTORY_TOPLEVEL, "data/")
ML_INPUTS_PATH = os.path.join(OUTPUT_DIRECTORY_TOPLEVEL, "ml_inputs/")

ML_RETURN_DF_PATH = os.path.join(ML_INPUTS_PATH, "_ml_return.csv")
ML_PARAM_DF_PATH = os.path.join(ML_INPUTS_PATH, "_ml_param.csv")
LABEL_ENCODER_PATH = os.path.join(ML_INPUTS_PATH, "label_encoder.pkl")
DATA_FILE = os.path.join(ML_INPUTS_PATH, "_all_data.csv")
FILTERED_DATA_FILE = os.path.join(ML_INPUTS_PATH, "_data_filtered.csv")

W2V_VEC_LENGTH = 14
NUMBER_OF_TYPES = 1000

OUTPUT_EMBEDDINGS_DIRECTORY = "./resources"
W2V_MODEL_CODE_DIR = os.path.join(OUTPUT_EMBEDDINGS_DIRECTORY, "w2v_code_model.bin")
W2V_MODEL_LANGUAGE_DIR = os.path.join(
    OUTPUT_EMBEDDINGS_DIRECTORY, "w2v_language_model.bin"
)

MODEL_DIR = os.path.join(OUTPUT_DIRECTORY_TOPLEVEL, "models/")
RETURN_DATAPOINTS_X = os.path.join(VECTOR_OUTPUT_DIRECTORY, "return_datapoints_x.npy")
RETURN_DATAPOINTS_Y = os.path.join(VECTOR_OUTPUT_DIRECTORY, "return_datapoints_y.npy")
PARAM_DATAPOINTS_X = os.path.join(VECTOR_OUTPUT_DIRECTORY, "param_datapoints_x.npy")
PARAM_DATAPOINTS_Y = os.path.join(VECTOR_OUTPUT_DIRECTORY, "param_datapoints_y.npy")
