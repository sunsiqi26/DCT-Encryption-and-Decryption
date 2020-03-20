[sampledata,FS] = audioread('DCT.wav');
temp_sample = resample(sampledata,1,FS/44100);
[m,n] = size(temp_sample);
disp(m);
% disp(n);
if (n == 2)
    sample1 = temp_sample(:,1);
    sample2 = temp_sample(:,2);
else
    sample1 = temp_sample;
end

% »­Ê±Óò²¨ÐÎÍ¼
n1=length(sample1);
n2=length(sample2);
t1=(1:n1)/(FS*60);
t2=(1:n2)/(FS*60);
plot(t1,sample1);
figure;
plot(t2,sample2);
xlabel('Time(min)');
ylabel('Amplitude');

% »­ÆµÆ×Í¼
subplot(212);
[S, F, T] = spectrogram(sample1, hanning(1024), 512, 1024, FS);
% [S, F, T] = spectrogram(sample2, hanning(1024), 512, 1024, FS);
tt=T/60;
Ff=F/1000;
imagesc(tt, Ff, log10(abs(S)));
set(gca, 'YDir', 'normal');
xlabel('Time(min)');
ylabel('Frequency(kHz)');