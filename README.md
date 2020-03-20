# DCT Encryption and Decryption

# Introduction

DCT (Discrete Cosine Transform) is mainly used to compress data or images. It can transform signals in the spatial domain to the frequency domain, and has good performance of decorrelation. The DCT transform itself is lossless, but in the fields of image coding, it creates good conditions for subsequent quantization and Huffman coding. At the same time, because the DCT transform is symmetrical, we can use the DCT inverse Transform, restore the original image information at the receiving end. DCT transform has a very wide range of applications in current image analysis compression. DCT transform is used in our common JPEG still image coding and MJPEG, MPEG dynamic coding standards.

The Audio feature analysis.m in the project is used to analyze the unknown audio to determine whether there is information hidden. If there is any hidden information, the DCT-Encryption.py file further decrypts the hidden position guessed in the previous step to obtain encryption. In the audio information, the ipynb file is responsible for encrypting the audio, and the DCT.wav file is the audio after the information is hidden.

