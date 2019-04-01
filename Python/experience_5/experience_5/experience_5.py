#scipy音频处理
from scipy.io import wavfile
import numpy as np
from matplotlib import pyplot as plt

# 采样  Alarm01.wav为声音源文件
sample_rate,data = wavfile.read('Alarm01.wav')
print(data.dtype,data.shape)

# 显示原始音频数据
plt.title('title')
plt.plot(data)
plt.show()

# 将原文件的声音数据复制一遍
repeated = np.array(list(data)*2)
# 在将重复之后的数据写入新的wav文件中
wavfile.write('repeated.wav',sample_rate,repeated)
