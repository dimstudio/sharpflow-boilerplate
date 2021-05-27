import numpy as np
import data_helper

if __name__ == "__main__":
    data_folder = "manual_sessions/"
    ignore_files = []
    to_exclude = ['OenName', 'RecordingID', 'ApplicationName']
    target_classes = ['mistake_back']
    tensor_data, annotations, attributes = data_helper.get_data_from_files(data_folder, ignore_files=ignore_files,
                                                                           res_rate=25,
                                                                           to_exclude=to_exclude)
    print("\nShape of the tensor_data is: " + str(np.shape(tensor_data)))
    print("Shape of the annotations is: " + str(np.shape(annotations)) + "\n")

    X = tensor_data
    y = annotations.reset_index(drop=True)

    df = annotations[['recordingID', 'mistake_back', 'end', 'start', 'duration']].copy()
    #df['gsr'] = np.mean(tensor_data[:, :, 1], axis=1)



















