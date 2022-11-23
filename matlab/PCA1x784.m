close all;
clc;
clear;
% load dataset
load('mnist_all.mat');

tr0 = [im2double(train0') im2double(train1') im2double(train2')];
trn = tr0(:,7004); %Bruger fjerde billede, fordi det er flåt
mu = mean(tr0')';
Sigma = cov(tr0' - mu'); 
[U S V] = svd(Sigma);

% Most important eigenvectors
M=10;
V_reduced = V(:,1:M)

z = V_reduced'*(trn-mu);
trn_mod = V_reduced * z + mu;

figure(1)
imshow(rot90(reshape(train0(4,:),[28 28]),1))
figure(2)
imshow(rot90(reshape(trn_mod(:,1),[28,28]),1))

