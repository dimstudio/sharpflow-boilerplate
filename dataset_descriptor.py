import data_helper
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_folder = "manual_sessions/"
plot_folder = "plots/"
data_folder = "manual_sessions/"
ignore_files = []
to_exclude = ['OenName', 'RecordingID', 'ApplicationName']
target_classes = ['mistake_back']
tensor_data, annotations, attributes = data_helper.get_data_from_files(data_folder, ignore_files=ignore_files,
                                                                       res_rate=25,
                                                                       to_exclude=to_exclude)
print("Shape of the tensor_data is: " + str(np.shape(tensor_data)))
print("Shape of the annotation is: " + str(np.shape(annotations)))

# # class distribution
plotdf = pd.DataFrame()

for t in target_classes:
    df = pd.DataFrame()
    df = annotations[[t, 'start']].groupby([t]).count()['start'].rename(t)
    # number of occurences
    print(annotations[[t, 'start']].groupby([t]).count()['start'] )
    # percentage
    print((annotations[[t, 'start']].groupby([t]).count()['start'] / np.shape(annotations)[0]).round(4))
    plotdf = pd.concat([plotdf, df], 1)
plotdf.T.plot(kind='bar', rot=0)
plt.ylabel('Class distribution')
plt.savefig(train_folder+'/class-distribution.pdf')

# class distribution per participant
plotdf = pd.DataFrame()
for t in target_classes:
    df = pd.DataFrame()
    annotations['p_id'] = annotations.recordingID.str.slice(0, 3, 1)
    annotations[['p_id', t, 'start']].groupby(['p_id', t]).count().unstack().fillna(0)[
        'start'].plot(kind="bar")
    plt.xlabel('Participants')
    plt.ylabel('Class distribution')
    plt.savefig(plot_folder+'/participants-'+t+'-distribution.pdf')


