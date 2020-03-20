import soundfile as sf
import numpy as np
from scipy.fftpack import dct

def Decrypt(file, start, end):

    # 已知对手组将音频按长度20分段，并指定了1050个段进行信息嵌入
    k1 = 1050
    k2 = 20
    #data = AudioSegment.from_mp3(file)
    data, rate = sf.read(file)
    left, right = data.T
    l = k2 * (len(data) // k2)

    #将左右声道分段，去掉最后不足一段的剩余数据
    right = right[:l].reshape([-1, k2])
    left = left[:l].reshape([-1, k2])

    '''
    #尝试1：直接取音频前1050个段
    for i in range(k1):
        dct_left.append(dct(left[i]))
        dct_right.append(dct(right[i]))
        
    #尝试2：分别对左右声道毎段数值求和，取最小的1050个段
    sum_left = np(np.sum(left, 1))
    sum_right = np(np.sum(right, 1))
    
    #尝试3：取求和后绝对值最小的1050个段
    sum_left = np.absolute(np.sum(left, 1))
    sum_right = np.absolute(np.sum(right, 1))
    '''

    #尝试4：取平方和最小的1050个段
    sum_left = np.sum(np.square(left), 1)
    sum_right = np.sum(np.square(right),1)

    #排序，返回序列索引
    left_index = sum_left.argsort()[0:k1*k2]
    right_index = sum_right.argsort()[0:k1*k2]
    #dct变换
    dct_left = []
    dct_right = []
    for i in range(k1*k2):
        dct_left.append(dct(left[left_index[i]]))
        dct_right.append(dct(right[left_index[i]]))
    dct_left = np.array(dct_left)
    dct_right = np.array(dct_right)

    differ = np.absolute(dct_right - dct_left)
    differ[differ >= 6e-45] = 1
    #print(6e-45)
    #print(differ)
    differ=np.around(differ).astype(int)
    decrypt = differ[:, start:end].reshape([-1, ])
    #将二进制转换为ASCII字符串
    #message = trans(decrypt)
    message = trans(decrypt ^ 1) #异或
    return message

def trans(s):
    bin = ''.join(str(i) for i in s)
    bin = bin[:7 * (len(bin) // 7)]
    string = ''.join([chr(int(bin[i:i + 7], 2)) for i in range(0, len(bin), 7)])
    return string

# 遍历搜索嵌入位置
'''
for i in range(1,19):
    for j in range(i+1,20):
        message = Decrypt('DCT.wav', i, j)
        print('i=',i,', j=',j)
        print(message)
'''
#得到嵌入位置为2至7后
start = 2
end = 7
message = Decrypt('DCT.wav', start, end)
print(message)

