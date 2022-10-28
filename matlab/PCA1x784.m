close all;
clc;
clear;
% load dataset
load('mnist_all.mat');

tr8 = im2double(train8');
trn = tr8(:,4); %Bruger fjerde billede, fordi det er flåt
mu = mean(tr8')';
Sigma = cov(tr8' - mu'); 
[U S V] = svd(Sigma);

% Most important eigenvectors
M=10;
V_reduced = V(:,1:M)

z = V_reduced'*(trn-mu);
trn_mod = V_reduced * z + mu;

figure(1)
imshow(rot90(reshape(train8(4,:),[28 28]),1))
figure(2)
imshow(rot90(reshape(trn_mod(:,1),[28,28]),1))

